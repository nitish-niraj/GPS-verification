# GPS Verifier - Location Validation System# GPS Verifier API



<div align="center">A simple and clean API for extracting GPS coordinates from images and validating locations against administrative zones.



![GPS Verifier](https://img.shields.io/badge/GPS-Verifier-blue)## 🚀 Features

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)

![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)- **GPS Extraction**: Extract coordinates from image EXIF data, OCR text, or pattern recognition

- **OCR Support**: Uses Tesseract OCR for reading GPS coordinates from image text overlays

**A modern web application for extracting GPS coordinates from images and validating locations against administrative zones**- **WhatsApp Detection**: Specifically detects and extracts coordinates from WhatsApp GPS overlays

- **Location Validation**: Validates coordinates against predefined administrative zones

</div>- **Simple API**: Clean REST endpoints for easy integration



---## 📁 Project Structure



## ✨ Features```

gps-verifier/

### GPS Extraction Methods├── backend/

- **EXIF Metadata**: Extracts GPS coordinates from image EXIF data│   ├── main.py                 # FastAPI application entry point

- **OCR Text Recognition**: Uses Tesseract OCR to extract visible GPS text│   ├── requirements.txt        # Python dependencies

- **Pattern Recognition**: Detects GPS coordinates using regex patterns│   ├── services/

- **WhatsApp GPS Overlay**: Specialized detection for WhatsApp location sharing images│   │   ├── gps_extractor.py   # GPS coordinate extraction (EXIF, OCR, patterns)

│   │   └── location_validator.py # Location validation against zones

### Location Validation│   ├── routes/

- **Zone Boundary Validation**: Validates coordinates against predefined administrative zones│   │   └── gps_api.py         # API endpoints

- **Multi-Zone Support**: Handles educational institutions, government zones, etc.│   └── data/

- **Confidence Scoring**: Provides validation confidence based on distance from boundaries│       └── ward_boundaries.json # Administrative zone definitions

- **Detailed Zone Information**: Returns contact details, departments, and addresses├── README.md                   # This file

└── requirements.txt           # Root dependencies

### Modern Web Interface```

- **Drag & Drop Upload**: Intuitive image upload with preview

- **Real-time Validation**: Instant GPS extraction and zone validation## 🛠️ Installation

- **Responsive Design**: Works on desktop, tablet, and mobile devices

- **Interactive Results**: Visual display of GPS coordinates and zone information### 1. Install Python Dependencies

- **Export Reports**: Download validation results as JSON```bash

cd backend

---pip install -r requirements.txt

```

## 🚀 Quick Start

### 2. Install Tesseract OCR (Windows)

### Installation```bash

winget install --id UB-Mannheim.TesseractOCR

1. **Clone the repository**```

```bash

git clone https://github.com/nitish-niraj/GPS-verification.git### 3. Run the API

cd GPS-verification```bash

```python main.py

```

2. **Install dependencies**

```bashThe API will be available at: `http://localhost:8000`

cd backend

pip install -r requirements.txt## 🔌 API Endpoints

```

### Image GPS Validation

3. **Start the server**```bash

```bashPOST /api/v1/validate-image-location

python main.py```

```Upload an image to extract GPS coordinates and validate location.



4. **Access the application****Example:**

- **Web UI**: http://localhost:8000/ui```bash

- **API Docs**: http://localhost:8000/docscurl -X POST http://localhost:8000/api/v1/validate-image-location \

- **Health Check**: http://localhost:8000/api/v1/health  -H "Content-Type: multipart/form-data" \

  -F "file=@your-image.jpg"

---```



## 📁 Project Structure### Direct Coordinate Validation

```bash

```POST /api/v1/validate-coordinates?latitude=31.2509&longitude=75.7054

GPS-verification/```

├── backend/                      # Backend API server

│   ├── main.py                  # FastAPI entry point### List Available Zones

│   ├── requirements.txt         # Python dependencies```bash

│   ├── routes/GET /api/v1/zones

│   │   └── gps_api.py          # API endpoints```

│   ├── services/

│   │   ├── gps_extractor.py    # GPS extraction### Health Check

│   │   └── location_validator.py # Zone validation```bash

│   └── data/GET /api/v1/health

│       └── ward_boundaries.json # Zone definitions```

│

├── frontend/                     # Web UI## 📖 How It Works

│   ├── index.html               # Main page

│   ├── css/style.css            # Styling### GPS Extraction Process

│   └── js/app.js                # Frontend logic1. **EXIF Data**: First tries to extract GPS from image metadata

│2. **OCR Text**: Uses Tesseract to read coordinates from text overlays

├── docker-compose.yml           # Docker config3. **Pattern Recognition**: Falls back to image pattern analysis

└── README.md                    # Documentation4. **WhatsApp Detection**: Specifically handles WhatsApp GPS overlay format

```

### Location Validation

---1. **Zone Matching**: Checks if coordinates fall within predefined zones

2. **Confidence Scoring**: Calculates confidence based on distance from boundaries

## 📖 Usage3. **Zone Information**: Returns detailed zone information (name, type, contact details)



### Web Interface## 🧪 Example Response



1. Open http://localhost:8000/ui in your browser```json

2. Drag & drop an image with GPS data{

3. Click "Validate Location"  "filename": "WhatsApp Image 2025-09-26.jpg",

4. View results with GPS coordinates and zone information  "extracted_gps": {

    "latitude": 31.2509,

### API Usage    "longitude": 75.7054,

    "source": "whatsapp_pattern",

**Validate Image:**    "confidence": 0.85,

```bash    "note": "Detected WhatsApp GPS overlay"

curl -X POST "http://localhost:8000/api/v1/validate-image-location" \  },

  -F "file=@your-image.jpg"  "validation": {

```    "status": "valid",

    "zone_name": "Lovely Professional University - Main Campus",

**Response:**    "zone_type": "educational_institution",

```json    "department": "University Administration",

{    "confidence": 0.72

  "filename": "whatsapp_location.jpg",  }

  "extracted_gps": {}

    "latitude": 31.256577,```

    "longitude": 75.704117,

    "source": "pattern_recognition",## 🔧 Configuration

    "confidence": 0.6

  },### Zone Boundaries

  "validation": {Edit `backend/data/ward_boundaries.json` to add or modify administrative zones:

    "status": "valid",

    "zone_name": "Lovely Professional University - Main Campus",```json

    "confidence": 0.73{

  }  "zones": [

}    {

```      "id": "zone_1",

      "name": "Zone Name",

### Python Example      "type": "zone_type",

      "boundary": [

```python        [longitude, latitude],

import requests        [longitude, latitude],

        ...

with open('image.jpg', 'rb') as f:      ]

    response = requests.post(    }

        'http://localhost:8000/api/v1/validate-image-location',  ]

        files={'file': f}}

    )```

    

result = response.json()### OCR Configuration

print(f"Status: {result['validation']['status']}")The system automatically detects Tesseract installation. If needed, manually configure the path in `services/gps_extractor.py`.

print(f"Zone: {result['validation']['zone_name']}")

```## 🚦 Development



---### Run in Development Mode

```bash

## 🔧 API Endpointspython main.py

```

| Method | Endpoint | Description |This starts the server with auto-reload enabled.

|--------|----------|-------------|

| GET | `/ui` | Web interface |### API Documentation

| POST | `/api/v1/validate-image-location` | Upload & validate image |Visit `http://localhost:8000/docs` for interactive API documentation.

| POST | `/api/v1/validate-coordinates` | Validate coordinates |

| GET | `/api/v1/zones` | List all zones |## 📝 License

| GET | `/api/v1/health` | Health check |

| GET | `/docs` | API documentation |This project is open source. Feel free to use and modify as needed.



---## 🤝 Contributing



## ⚙️ Configuration1. Fork the repository

2. Create a feature branch

### Add Custom Zones3. Make your changes

4. Test thoroughly

Edit `backend/data/ward_boundaries.json`:5. Submit a pull request



```json## 📞 Support

{

  "educational_zones": {For issues or questions, please check the API documentation at `/docs` or review the code comments for detailed explanations.
    "CustomZone": {
      "name": "Your Custom Zone",
      "type": "educational_institution",
      "contact": "+1-234-567-8900",
      "boundary": [
        [lat1, lon1],
        [lat2, lon2],
        ...
      ]
    }
  }
}
```

---

## 🐳 Docker Deployment

```bash
docker-compose up -d
```

Access at: http://localhost:8000/ui

---

## 🛠️ Technology Stack

**Backend:**
- FastAPI - Web framework
- Pillow - Image processing
- pytesseract - OCR
- Shapely - Geospatial calculations

**Frontend:**
- HTML5/CSS3 - Modern UI
- Vanilla JavaScript - No dependencies

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

MIT License - see LICENSE file for details.

---

## 👥 Author

**Nitish Niraj** - [@nitish-niraj](https://github.com/nitish-niraj)

---

## 📞 Support

For support, open an issue on GitHub.

---

<div align="center">

**Made with ❤️ for accurate location validation**

[⬆ Back to Top](#gps-verifier---location-validation-system)

</div>
