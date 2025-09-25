# GPS Verifier API

A simple and clean API for extracting GPS coordinates from images and validating locations against administrative zones.

## 🚀 Features

- **GPS Extraction**: Extract coordinates from image EXIF data, OCR text, or pattern recognition
- **OCR Support**: Uses Tesseract OCR for reading GPS coordinates from image text overlays
- **WhatsApp Detection**: Specifically detects and extracts coordinates from WhatsApp GPS overlays
- **Location Validation**: Validates coordinates against predefined administrative zones
- **Simple API**: Clean REST endpoints for easy integration

## 📁 Project Structure

```
gps-verifier/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── services/
│   │   ├── gps_extractor.py   # GPS coordinate extraction (EXIF, OCR, patterns)
│   │   └── location_validator.py # Location validation against zones
│   ├── routes/
│   │   └── gps_api.py         # API endpoints
│   └── data/
│       └── ward_boundaries.json # Administrative zone definitions
├── README.md                   # This file
└── requirements.txt           # Root dependencies
```

## 🛠️ Installation

### 1. Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Install Tesseract OCR (Windows)
```bash
winget install --id UB-Mannheim.TesseractOCR
```

### 3. Run the API
```bash
python main.py
```

The API will be available at: `http://localhost:8000`

## 🔌 API Endpoints

### Image GPS Validation
```bash
POST /api/v1/validate-image-location
```
Upload an image to extract GPS coordinates and validate location.

**Example:**
```bash
curl -X POST http://localhost:8000/api/v1/validate-image-location \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your-image.jpg"
```

### Direct Coordinate Validation
```bash
POST /api/v1/validate-coordinates?latitude=31.2509&longitude=75.7054
```

### List Available Zones
```bash
GET /api/v1/zones
```

### Health Check
```bash
GET /api/v1/health
```

## 📖 How It Works

### GPS Extraction Process
1. **EXIF Data**: First tries to extract GPS from image metadata
2. **OCR Text**: Uses Tesseract to read coordinates from text overlays
3. **Pattern Recognition**: Falls back to image pattern analysis
4. **WhatsApp Detection**: Specifically handles WhatsApp GPS overlay format

### Location Validation
1. **Zone Matching**: Checks if coordinates fall within predefined zones
2. **Confidence Scoring**: Calculates confidence based on distance from boundaries
3. **Zone Information**: Returns detailed zone information (name, type, contact details)

## 🧪 Example Response

```json
{
  "filename": "WhatsApp Image 2025-09-26.jpg",
  "extracted_gps": {
    "latitude": 31.2509,
    "longitude": 75.7054,
    "source": "whatsapp_pattern",
    "confidence": 0.85,
    "note": "Detected WhatsApp GPS overlay"
  },
  "validation": {
    "status": "valid",
    "zone_name": "Lovely Professional University - Main Campus",
    "zone_type": "educational_institution",
    "department": "University Administration",
    "confidence": 0.72
  }
}
```

## 🔧 Configuration

### Zone Boundaries
Edit `backend/data/ward_boundaries.json` to add or modify administrative zones:

```json
{
  "zones": [
    {
      "id": "zone_1",
      "name": "Zone Name",
      "type": "zone_type",
      "boundary": [
        [longitude, latitude],
        [longitude, latitude],
        ...
      ]
    }
  ]
}
```

### OCR Configuration
The system automatically detects Tesseract installation. If needed, manually configure the path in `services/gps_extractor.py`.

## 🚦 Development

### Run in Development Mode
```bash
python main.py
```
This starts the server with auto-reload enabled.

### API Documentation
Visit `http://localhost:8000/docs` for interactive API documentation.

## 📝 License

This project is open source. Feel free to use and modify as needed.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues or questions, please check the API documentation at `/docs` or review the code comments for detailed explanations.