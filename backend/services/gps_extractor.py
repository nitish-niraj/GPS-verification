#!/usr/bin/env python3
"""
GPS Coordinate Extractor - Unified GPS extraction from images
Supports multiple extraction methods with Tesseract OCR integration
"""

import re
import logging
import io
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import numpy as np
from typing import Dict, Optional, Tuple

# Configure logging
logger = logging.getLogger(__name__)

class GPSExtractor:
    """
    Unified GPS coordinate extractor that handles:
    1. EXIF GPS data extraction
    2. OCR text extraction using Tesseract
    3. WhatsApp GPS overlay detection
    4. Pattern recognition fallback
    """
    
    def __init__(self):
        """Initialize the GPS extractor with OCR capabilities"""
        # GPS coordinate patterns for text extraction
        self.coordinate_patterns = [
            # WhatsApp/Google Maps format: "Latitude 31.2509° N Longitude 75.7054° E"
            r'Latitude\s*([+-]?\d+\.?\d*)[°]?\s*[NS]?\s*.*?Longitude\s*([+-]?\d+\.?\d*)[°]?\s*[EW]?',
            
            # Standard format: "Lat: 31.256577° Long: 75.704117°"
            r'(?:Lat|at|bat):\s*([+-]?\d+\.?\d*)[°]?\s*[NS]?\s*.*?(?:Long?|ong|tong):\s*([+-]?\d+\.?\d*)[°]?\s*[EW]?',
            
            # Decimal format: "31.256577, 75.704117"
            r'([+-]?\d+\.\d+)\s*,\s*([+-]?\d+\.\d+)',
            
            # Direction format: "31.256577° N, 75.704117° E"
            r'([+-]?\d+\.?\d*)[°]?\s*[NS]\s*,?\s*([+-]?\d+\.?\d*)[°]?\s*[EW]',
        ]
        
        # Check if OCR is available
        self.ocr_available = self._setup_ocr()
        if self.ocr_available:
            logger.info("✅ GPS Extractor initialized with OCR support")
        else:
            logger.warning("⚠️ GPS Extractor initialized WITHOUT OCR support")
    
    def extract_gps_coordinates(self, image_data: bytes) -> Optional[Dict]:
        """
        Main method to extract GPS coordinates from image
        
        Args:
            image_data: Image file data as bytes
            
        Returns:
            Dict with latitude, longitude, source, confidence, and metadata
        """
        logger.info("Starting GPS coordinate extraction")
        
        # Method 1: Try EXIF GPS data first (most accurate)
        exif_result = self._extract_from_exif(image_data)
        if exif_result:
            logger.info("✅ GPS extracted from EXIF data")
            return exif_result
        
        # Method 2: Try OCR text extraction
        if self.ocr_available:
            logger.info("🔍 Attempting OCR extraction...")
            ocr_result = self._extract_from_ocr(image_data)
            if ocr_result:
                logger.info("✅ GPS extracted using OCR")
                return ocr_result
            logger.warning("❌ OCR extraction found no coordinates")
        else:
            logger.warning("⚠️ OCR not available - skipping OCR extraction")
        
        # Method 3: Pattern recognition fallback
        pattern_result = self._extract_from_patterns(image_data)
        if pattern_result:
            logger.info("✅ GPS extracted using pattern recognition")
            return pattern_result
        
        logger.warning("❌ No GPS coordinates found in image")
        return None
    
    def _setup_ocr(self) -> bool:
        """Setup and verify OCR capabilities"""
        try:
            import pytesseract
            import cv2
            import os
            
            # Configure Tesseract path
            tesseract_paths = [
                os.getenv('TESSERACT_CMD'),  # Environment variable (Docker/HF)
                '/usr/bin/tesseract',  # Linux default (Docker/HF)
                r"D:\OCR-System\tesseract.exe",  # User's custom installation
                r"C:\Program Files\Tesseract-OCR\tesseract.exe",  # Windows
                r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",  # Windows x86
            ]
            
            # Filter out None values
            tesseract_paths = [p for p in tesseract_paths if p]
            
            for path in tesseract_paths:
                if os.path.exists(path):
                    pytesseract.pytesseract.tesseract_cmd = path
                    logger.info(f"✅ Found Tesseract at: {path}")
                    break
            else:
                logger.warning("⚠️ Tesseract executable not found")
                return False
            
            # Test OCR functionality
            version = pytesseract.get_tesseract_version()
            logger.info(f"✅ OCR ready: Tesseract {version}")
            return True
            
        except Exception as e:
            logger.warning(f"⚠️ OCR not available: {e}")
            return False
    
    def _extract_from_exif(self, image_data: bytes) -> Optional[Dict]:
        """Extract GPS coordinates from EXIF metadata"""
        try:
            image = Image.open(io.BytesIO(image_data))
            exif_data = image._getexif()
            
            if not exif_data:
                return None
            
            # Look for GPS info in EXIF
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    gps_data = {}
                    for gps_tag_id, gps_value in value.items():
                        gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                        gps_data[gps_tag] = gps_value
                    
                    # Convert GPS coordinates
                    lat = self._convert_gps_coordinate(
                        gps_data.get('GPSLatitude'),
                        gps_data.get('GPSLatitudeRef', 'N')
                    )
                    lon = self._convert_gps_coordinate(
                        gps_data.get('GPSLongitude'),
                        gps_data.get('GPSLongitudeRef', 'E')
                    )
                    
                    if lat is not None and lon is not None:
                        return {
                            "latitude": lat,
                            "longitude": lon,
                            "source": "exif",
                            "confidence": 0.95,
                            "note": "Extracted from image EXIF metadata"
                        }
            
            return None
            
        except Exception as e:
            logger.debug(f"EXIF extraction failed: {e}")
            return None
    
    def _extract_from_ocr(self, image_data: bytes) -> Optional[Dict]:
        """Extract GPS coordinates using OCR text recognition"""
        try:
            import pytesseract
            import cv2
            
            # Convert image data to OpenCV format
            nparr = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Preprocess image for better OCR
            processed_image = self._preprocess_for_ocr(image)
            
            # Extract text using OCR
            text = pytesseract.image_to_string(processed_image)
            logger.debug(f"OCR extracted text: {repr(text)}")
            
            # Parse coordinates from extracted text
            coordinates = self._parse_coordinates_from_text(text)
            
            if coordinates:
                lat, lon = coordinates
                return {
                    "latitude": lat,
                    "longitude": lon,
                    "source": "ocr",
                    "confidence": 0.8,
                    "note": "Extracted using Tesseract OCR"
                }
            
            return None
            
        except Exception as e:
            logger.debug(f"OCR extraction failed: {e}")
            return None
    
    def _extract_from_patterns(self, image_data: bytes) -> Optional[Dict]:
        """
        Extract GPS coordinates using pattern recognition
        
        This method attempts to find GPS coordinates by analyzing the image structure
        and extracting coordinates from specific regions where GPS text typically appears.
        
        IMPORTANT: Only returns coordinates if actually found in the image.
        Does NOT return fake/hardcoded coordinates as fallback.
        """
        try:
            # Convert image data to PIL Image for analysis
            image = Image.open(io.BytesIO(image_data))
            width, height = image.size
            
            logger.debug(f"Pattern recognition: Analyzing {width}x{height} image")
            
            # Try to detect and extract GPS coordinates from overlay regions
            # Focus on common GPS overlay positions (top/bottom of image)
            
            # Check top 15% of image (common GPS overlay position)
            top_region = image.crop((0, 0, width, int(height * 0.15)))
            top_coords = self._extract_coords_from_region(top_region, "top")
            if top_coords:
                logger.info("✅ Found GPS coordinates in top region")
                return top_coords
            
            # Check bottom 15% of image (another common position)
            bottom_region = image.crop((0, int(height * 0.85), width, height))
            bottom_coords = self._extract_coords_from_region(bottom_region, "bottom")
            if bottom_coords:
                logger.info("✅ Found GPS coordinates in bottom region")
                return bottom_coords
            
            # If no coordinates found in specific regions, return None
            logger.debug("Pattern recognition: No GPS coordinates found in overlay regions")
            logger.warning("❌ No GPS coordinates found using pattern recognition")
            return None
            
        except Exception as e:
            logger.debug(f"Pattern recognition failed: {e}")
            return None
    
    def _extract_coords_from_region(self, region: Image, region_name: str) -> Optional[Dict]:
        """
        Extract GPS coordinates from a specific image region
        
        Uses basic OCR without requiring Tesseract installation
        by checking for GPS coordinate patterns in the pixel data
        """
        try:
            # Convert region to text-searchable format
            # Look for coordinate patterns in the region
            
            # For now, attempt simple pattern matching
            # This is a placeholder for more sophisticated pattern recognition
            # In a production system, this would use computer vision to detect
            # GPS coordinate text in the image region
            
            logger.debug(f"Checking {region_name} region for GPS coordinates")
            
            # Without OCR available, pattern recognition alone cannot reliably
            # extract text-based coordinates. Return None to indicate no detection.
            return None
            
        except Exception as e:
            logger.debug(f"Region extraction failed for {region_name}: {e}")
            return None
    
    def _preprocess_for_ocr(self, image):
        """Preprocess image to improve OCR accuracy"""
        try:
            import cv2
            
            # Convert to grayscale for better text recognition
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Enhance contrast to make text clearer
            enhanced = cv2.convertScaleAbs(gray, alpha=1.5, beta=30)
            
            # Apply threshold to create clear black/white text
            _, thresh = cv2.threshold(enhanced, 127, 255, cv2.THRESH_BINARY)
            
            return thresh
            
        except Exception as e:
            logger.debug(f"Image preprocessing failed: {e}")
            return image
    
    def _parse_coordinates_from_text(self, text: str) -> Optional[Tuple[float, float]]:
        """Parse GPS coordinates from extracted text"""
        if not text:
            return None
        
        # Clean up text and fix common OCR errors
        text = text.replace('\n', ' ').replace('\r', ' ')
        # Fix spaces in decimal numbers: "75. 704117" -> "75.704117"
        text = re.sub(r'(\d+)\.\s+(\d+)', r'\1.\2', text)
        # Fix common OCR character mistakes
        text = text.replace('ers:', 'GPS:').replace('ars:', 'GPS:').replace('tong:', 'Long:')
        
        logger.debug(f"Cleaned text: {repr(text)}")
        
        # Try each coordinate pattern
        for pattern in self.coordinate_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    lat_str = match.group(1).replace(' ', '')
                    lon_str = match.group(2).replace(' ', '')
                    
                    lat = float(lat_str)
                    lon = float(lon_str)
                    
                    # Fix common OCR digit errors (9 -> 3)
                    if lat > 90:
                        if lat_str.startswith('9'):
                            corrected_lat = float('3' + lat_str[1:])
                            if -90 <= corrected_lat <= 90:
                                lat = corrected_lat
                                logger.info(f"OCR correction: {lat_str} -> 3{lat_str[1:]}")
                    
                    # Validate coordinates
                    if -90 <= lat <= 90 and -180 <= lon <= 180:
                        logger.info(f"Found coordinates: {lat}, {lon}")
                        return (lat, lon)
                        
                except (ValueError, IndexError) as e:
                    logger.debug(f"Failed to parse match {match.groups()}: {e}")
                    continue
        
        return None
    
    def _is_whatsapp_gps_image(self, image: Image) -> bool:
        """
        Detect WhatsApp GPS overlay images
        
        ❌ DEPRECATED: This function is no longer used for GPS extraction.
        It was previously used to return hardcoded coordinates, which was wrong.
        Keeping it here for reference but it should not be called.
        """
        try:
            width, height = image.size
            
            # WhatsApp images are typically 832x1600
            if width == 832 and height == 1600:
                logger.debug(f"Found WhatsApp dimensions: {width}x{height}")
                
                # Check for green overlay in bottom portion (GPS info area)
                bottom_crop = image.crop((0, int(height * 0.85), width, height))
                pixels = np.array(bottom_crop)
                
                if len(pixels.shape) == 3:
                    # Count green-dominant pixels (Google Maps style)
                    green_channel = pixels[:, :, 1]
                    red_channel = pixels[:, :, 0]
                    blue_channel = pixels[:, :, 2]
                    
                    # Find green-dominant pixels
                    green_dominant = (green_channel > red_channel + 20) & (green_channel > blue_channel + 20)
                    green_count = np.sum(green_dominant)
                    total_pixels = green_channel.size
                    
                    logger.debug(f"Green pixels: {green_count}/{total_pixels} ({green_count/total_pixels*100:.1f}%)")
                    
                    # 4% threshold for green overlay detection
                    if green_count > total_pixels * 0.04:
                        logger.info("✅ Detected WhatsApp GPS overlay")
                        return True
            
            return False
            
        except Exception as e:
            logger.debug(f"WhatsApp detection error: {e}")
            return False
    
    def _is_lpu_campus_image(self, image: Image) -> bool:
        """
        Detect general LPU campus images
        
        ❌ DEPRECATED: This function is no longer used for GPS extraction.
        The logic (checking if >10% pixels are dark) is meaningless and was causing the system
        to accept ANY image with some dark areas and return fake GPS coordinates.
        Keeping it here for reference but it should not be called.
        """
        try:
            width, height = image.size
            
            # Check for typical characteristics of LPU campus images
            # This is a simple heuristic based on image properties
            
            # Check for dark overlay areas (typical of GPS overlays)
            gray = image.convert('L')
            pixels = np.array(gray)
            dark_pixels = np.sum(pixels < 100)
            
            # If significant dark areas, might be GPS overlay
            if dark_pixels > pixels.size * 0.1:
                logger.debug("Found overlay characteristics suggesting LPU campus")
                return True
            
            return False
            
        except Exception as e:
            logger.debug(f"LPU campus detection error: {e}")
            return False
    
    def _convert_gps_coordinate(self, coord_data, direction):
        """Convert GPS coordinate from EXIF format to decimal degrees"""
        if not coord_data:
            return None
        
        try:
            degrees = float(coord_data[0])
            minutes = float(coord_data[1])
            seconds = float(coord_data[2])
            
            # Convert to decimal degrees
            decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
            
            # Apply direction (South/West are negative)
            if direction in ['S', 'W']:
                decimal = -decimal
            
            return decimal
            
        except (IndexError, ValueError, TypeError):
            return None