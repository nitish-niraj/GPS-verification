#!/usr/bin/env python3
"""
GPS Validation API Routes - Simple REST endpoints for GPS validation
Provides clean API endpoints for GPS coordinate extraction and validation
"""

import logging
from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import Dict

# Import our simplified services
from services.gps_extractor import GPSExtractor
from services.location_validator import LocationValidator

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(prefix="/api/v1", tags=["GPS Validation"])

# Initialize services
gps_extractor = GPSExtractor()
location_validator = LocationValidator()

@router.post("/validate-image-location")
async def validate_image_location(file: UploadFile = File(...)) -> Dict:
    """
    Extract GPS coordinates from uploaded image and validate location
    
    This endpoint:
    1. Extracts GPS coordinates from image (EXIF, OCR, or pattern recognition)
    2. Validates coordinates against administrative zones
    3. Returns validation result with zone information
    
    Args:
        file: Uploaded image file (JPG, PNG, etc.)
        
    Returns:
        JSON response with GPS coordinates and validation status
    """
    try:
        # Validate file type
        if not file.content_type or not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Read image data
        image_data = await file.read()
        logger.info(f"Processing image: {file.filename} ({len(image_data)} bytes)")
        
        # Step 1: Extract GPS coordinates from image
        gps_result = gps_extractor.extract_gps_coordinates(image_data)
        
        if not gps_result:
            logger.warning(f"No GPS coordinates found in {file.filename}")
            return {
                "filename": file.filename,
                "error": "No GPS coordinates found in image",
                "suggestions": [
                    "Ensure image has GPS location data",
                    "Check if image has visible GPS coordinates",
                    "Verify image is not corrupted"
                ]
            }
        
        # Step 2: Validate coordinates against zones
        latitude = gps_result['latitude']
        longitude = gps_result['longitude']
        
        validation_result = location_validator.validate_coordinates(latitude, longitude)
        
        # Step 3: Build response
        response = {
            "filename": file.filename,
            "extracted_gps": {
                "latitude": latitude,
                "longitude": longitude,
                "source": gps_result['source'],
                "confidence": gps_result['confidence'],
                "note": gps_result.get('note', '')
            },
            "validation": validation_result,
            "processing_method": gps_result['source']
        }
        
        # Log result
        status = validation_result['status']
        zone_name = validation_result.get('zone_name', 'Unknown')
        logger.info(f"✅ Image validation: {file.filename} -> {status} ({zone_name})")
        
        return response
        
    except Exception as e:
        logger.error(f"❌ Error processing {file.filename}: {e}")
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@router.post("/validate-coordinates")
async def validate_coordinates(latitude: float, longitude: float) -> Dict:
    """
    Validate GPS coordinates directly (without image)
    
    Args:
        latitude: GPS latitude coordinate (-90 to 90)
        longitude: GPS longitude coordinate (-180 to 180)
        
    Returns:
        JSON response with validation status and zone information
    """
    try:
        # Validate coordinate ranges
        if not (-90 <= latitude <= 90):
            raise HTTPException(status_code=400, detail="Latitude must be between -90 and 90")
        
        if not (-180 <= longitude <= 180):
            raise HTTPException(status_code=400, detail="Longitude must be between -180 and 180")
        
        # Validate coordinates
        validation_result = location_validator.validate_coordinates(latitude, longitude)
        
        logger.info(f"✅ Coordinate validation: {latitude}, {longitude} -> {validation_result['status']}")
        
        return {
            "coordinates": {
                "latitude": latitude,
                "longitude": longitude
            },
            "validation": validation_result
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error validating coordinates {latitude}, {longitude}: {e}")
        raise HTTPException(status_code=500, detail=f"Validation error: {str(e)}")

@router.get("/zones")
async def list_zones() -> Dict:
    """
    Get list of all available administrative zones
    
    Returns:
        JSON response with list of zones and their basic information
    """
    try:
        zones = location_validator.list_available_zones()
        
        return {
            "total_zones": len(zones),
            "zones": zones
        }
        
    except Exception as e:
        logger.error(f"❌ Error listing zones: {e}")
        raise HTTPException(status_code=500, detail=f"Error retrieving zones: {str(e)}")

@router.get("/zones/{zone_id}")
async def get_zone_info(zone_id: str) -> Dict:
    """
    Get detailed information about a specific zone
    
    Args:
        zone_id: Unique identifier for the zone
        
    Returns:
        JSON response with detailed zone information
    """
    try:
        zone_info = location_validator.get_zone_info(zone_id)
        
        if not zone_info:
            raise HTTPException(status_code=404, detail=f"Zone '{zone_id}' not found")
        
        return zone_info
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error getting zone info for {zone_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Error retrieving zone info: {str(e)}")

@router.get("/health")
async def health_check() -> Dict:
    """
    Simple health check endpoint
    
    Returns:
        System status and component availability
    """
    return {
        "status": "healthy",
        "components": {
            "gps_extractor": "ready",
            "location_validator": "ready",
            "ocr_available": gps_extractor.ocr_available,
            "zones_loaded": len(location_validator.zones)
        },
        "message": "GPS Validation API is running"
    }