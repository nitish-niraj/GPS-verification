#!/usr/bin/env python3
"""
Quick test to verify GPS extraction rejects non-GPS images
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from services.gps_extractor import GPSExtractor
from PIL import Image
import io

# Create a simple test image with no GPS
img = Image.new('RGB', (100, 100), color='red')
img_bytes = io.BytesIO()
img.save(img_bytes, format='JPEG')
img_data = img_bytes.getvalue()

# Test extraction
extractor = GPSExtractor()
result = extractor.extract_gps_coordinates(img_data)

print("\n" + "="*60)
print("🧪 Quick GPS Extraction Test")
print("="*60)
print(f"\n📷 Test image: 100x100 red square (no GPS data)")
print(f"📊 Result: {result}")

if result is None:
    print("\n✅ SUCCESS! System correctly rejected image without GPS")
    print("   The bug is fixed - no fake coordinates returned!")
else:
    print("\n❌ FAILED! System returned fake GPS data:")
    print(f"   {result}")
    print("   The bug is NOT fixed!")

print("\n" + "="*60 + "\n")
