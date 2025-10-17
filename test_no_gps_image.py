#!/usr/bin/env python3
"""
Test script to verify the GPS extraction fix
Tests that images without GPS data are properly rejected
"""

import sys
import os
from PIL import Image
import numpy as np

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from services.gps_extractor import GPSExtractor

def create_test_image_without_gps(filename: str):
    """Create a simple test image without any GPS data"""
    # Create a 400x400 pixel image with some random content
    img_array = np.random.randint(0, 255, (400, 400, 3), dtype=np.uint8)
    img = Image.fromarray(img_array, 'RGB')
    img.save(filename)
    print(f"✅ Created test image: {filename}")
    return filename

def test_gps_extraction():
    """Test GPS extraction with an image that has NO GPS data"""
    
    print("\n" + "="*60)
    print("🧪 Testing GPS Extraction Fix")
    print("="*60)
    
    # Create test image
    test_image = create_test_image_without_gps("test_no_gps.jpg")
    
    # Initialize GPS extractor
    extractor = GPSExtractor()
    
    # Read image data
    with open(test_image, 'rb') as f:
        image_data = f.read()
    
    print(f"\n📷 Testing image: {test_image} ({len(image_data)} bytes)")
    print("Expected result: None (no GPS data found)")
    print("-" * 60)
    
    # Extract GPS
    result = extractor.extract_gps_coordinates(image_data)
    
    print("\n" + "="*60)
    print("📊 Test Result:")
    print("="*60)
    
    if result is None:
        print("✅ SUCCESS: System correctly rejected image without GPS data")
        print("   The fix is working! No fake coordinates were returned.")
    else:
        print("❌ FAILED: System still returning GPS data for non-GPS image!")
        print(f"   Result: {result}")
        print("   This should NOT happen - the bug is not fully fixed!")
    
    # Cleanup
    if os.path.exists(test_image):
        os.remove(test_image)
        print(f"\n🧹 Cleaned up test image: {test_image}")
    
    print("\n" + "="*60)
    return result is None

if __name__ == "__main__":
    success = test_gps_extraction()
    sys.exit(0 if success else 1)
