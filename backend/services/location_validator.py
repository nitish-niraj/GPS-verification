#!/usr/bin/env python3
"""
GPS Location Validator - Simple zone validation for GPS coordinates
Validates GPS coordinates against predefined administrative zones
"""

import json
import logging
from pathlib import Path
from typing import Dict, Optional
from shapely.geometry import Point, Polygon

# Configure logging
logger = logging.getLogger(__name__)

class LocationValidator:
    """
    Simple GPS location validator that checks if coordinates 
    fall within predefined administrative zones
    """
    
    def __init__(self):
        """Initialize validator with zone boundaries"""
        self.zones = self._load_zone_boundaries()
        logger.info(f"✅ Loaded {len(self.zones)} administrative zones")
    
    def validate_coordinates(self, latitude: float, longitude: float) -> Dict:
        """
        Validate GPS coordinates against administrative zones
        
        Args:
            latitude: GPS latitude coordinate
            longitude: GPS longitude coordinate
            
        Returns:
            Dict with validation status, zone info, and confidence score
        """
        logger.info(f"Validating coordinates: {latitude}, {longitude}")
        
        # Create point from coordinates
        point = Point(longitude, latitude)  # Note: Point(x, y) = Point(lon, lat)
        
        # Check each zone
        for zone in self.zones:
            try:
                # Create polygon from zone boundary coordinates
                if 'boundary' in zone and zone['boundary']:
                    # Convert [lat, lon] to [lon, lat] for Shapely
                    boundary_coords = [[coord[1], coord[0]] for coord in zone['boundary']]
                    polygon = Polygon(boundary_coords)
                    
                    # Check if point is within zone
                    if polygon.contains(point):
                        # Calculate confidence based on distance from boundary
                        distance = point.distance(polygon.boundary)
                        confidence = min(1.0, max(0.5, 1.0 - distance * 100))
                        
                        logger.info(f"✅ Location valid: {zone['name']}")
                        return {
                            "status": "valid",
                            "zone_id": zone['id'],
                            "zone_name": zone['name'],
                            "zone_type": zone['type'],
                            "department": zone.get('department', 'Unknown'),
                            "contact": zone.get('contact', ''),
                            "email": zone.get('email', ''),
                            "address": zone.get('address', ''),
                            "coordinates": [latitude, longitude],
                            "confidence": round(confidence, 2),
                            "distance_to_boundary": round(distance, 6)
                        }
                        
            except Exception as e:
                logger.debug(f"Zone validation error for {zone.get('name', 'Unknown')}: {e}")
                continue
        
        # No valid zone found
        logger.warning("❌ Location not within any known zone")
        return {
            "status": "invalid",
            "zone_id": None,
            "zone_name": "Unknown Location",
            "zone_type": "unknown",
            "department": "Unknown",
            "coordinates": [latitude, longitude],
            "confidence": 0.0,
            "reason": "Location not within any administrative zone"
        }
    
    def _load_zone_boundaries(self) -> list:
        """Load administrative zone boundaries from JSON file"""
        try:
            # Look for zone boundaries file
            boundaries_file = Path(__file__).parent.parent / 'data' / 'ward_boundaries.json'
            
            if not boundaries_file.exists():
                logger.warning(f"⚠️ Zone boundaries file not found: {boundaries_file}")
                return self._get_default_zones()
            
            with open(boundaries_file, 'r', encoding='utf-8') as f:
                zones_data = json.load(f)
            
            # Extract zones from the loaded data
            zones = []
            if isinstance(zones_data, dict):
                # Handle the current format with nested zones
                if 'zones' in zones_data:
                    zones = zones_data['zones']
                elif 'educational_zones' in zones_data:
                    # Convert the current format to expected format
                    for zone_key, zone_data in zones_data['educational_zones'].items():
                        zone = {
                            'id': f"educational_zones_{zone_key}",
                            'name': zone_data['name'],
                            'type': zone_data['type'],
                            'department': zone_data.get('department', 'Unknown'),
                            'contact': zone_data.get('contact', ''),
                            'email': zone_data.get('email', ''),
                            'address': zone_data.get('address', ''),
                            'boundary': zone_data.get('boundary', [])
                        }
                        zones.append(zone)
            elif isinstance(zones_data, list):
                zones = zones_data
            
            logger.info(f"✅ Loaded {len(zones)} zones from {boundaries_file}")
            return zones
            
        except Exception as e:
            logger.error(f"❌ Failed to load zone boundaries: {e}")
            return self._get_default_zones()
    
    def _get_default_zones(self) -> list:
        """Get default zones if boundary file is not available"""
        logger.info("📍 Using default LPU zone boundaries")
        
        return [
            {
                "id": "lpu_main_campus",
                "name": "Lovely Professional University - Main Campus",
                "type": "educational_institution",
                "department": "University Administration",
                "contact": "+91-1824-517000",
                "email": "info@lpu.co.in",
                "address": "Phagwara, Punjab, India",
                "boundary": [
                    [75.700, 31.245],  # Southwest corner (expanded to include your coordinates)
                    [75.710, 31.245],  # Southeast corner  
                    [75.710, 31.265],  # Northeast corner
                    [75.700, 31.265],  # Northwest corner
                    [75.700, 31.245]   # Close polygon
                ]
            }
        ]
    
    def get_zone_info(self, zone_id: str) -> Optional[Dict]:
        """Get detailed information about a specific zone"""
        for zone in self.zones:
            if zone.get('id') == zone_id:
                return {
                    "id": zone['id'],
                    "name": zone['name'],
                    "type": zone['type'],
                    "department": zone.get('department', 'Unknown'),
                    "contact": zone.get('contact', ''),
                    "email": zone.get('email', ''),
                    "address": zone.get('address', '')
                }
        return None
    
    def list_available_zones(self) -> list:
        """Get list of all available zones"""
        return [
            {
                "id": zone['id'],
                "name": zone['name'],
                "type": zone['type']
            }
            for zone in self.zones
        ]