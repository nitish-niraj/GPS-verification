# GPS Verifier - LPU Campus Location Validation System# GPS Verifier - Location Validation System# GPS Verifier API



[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/nitish-niraj/GPS-verification)

[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)<div align="center">A simple and clean API for extracting GPS coordinates from images and validating locations against administrative zones.

[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)



A modern, intelligent GPS validation system designed for **Lovely Professional University (LPU)** campus. This system extracts GPS coordinates from images using multiple methods and validates locations against predefined campus boundaries.

![GPS Verifier](https://img.shields.io/badge/GPS-Verifier-blue)## 🚀 Features

## 🌟 Key Features

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)

- **📸 Multi-Method GPS Extraction**

  - EXIF metadata reading from camera photos![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)- **GPS Extraction**: Extract coordinates from image EXIF data, OCR text, or pattern recognition

  - OCR text extraction using Tesseract (for screenshots)

  - Pattern recognition as fallback method- **OCR Support**: Uses Tesseract OCR for reading GPS coordinates from image text overlays



- **🎯 LPU Campus Validation****A modern web application for extracting GPS coordinates from images and validating locations against administrative zones**- **WhatsApp Detection**: Specifically detects and extracts coordinates from WhatsApp GPS overlays

  - Precise boundary validation for LPU Main Campus

  - Polygon-based geofencing- **Location Validation**: Validates coordinates against predefined administrative zones

  - Detailed zone information

</div>- **Simple API**: Clean REST endpoints for easy integration

- **🚀 Modern Tech Stack**

  - FastAPI for high-performance REST API

  - Tesseract OCR for text extraction

  - Apple-inspired glassmorphism UI---## 📁 Project Structure

  - Real-time validation



- **📱 Filename-Independent**

  - Content-based extraction only## ✨ Features```

  - Works with images from any source

  - No naming conventions requiredgps-verifier/



## 📋 Table of Contents### GPS Extraction Methods├── backend/



- [Quick Start](#-quick-start)- **EXIF Metadata**: Extracts GPS coordinates from image EXIF data│   ├── main.py                 # FastAPI application entry point

- [Installation](#-installation)

- [Usage](#-usage)- **OCR Text Recognition**: Uses Tesseract OCR to extract visible GPS text│   ├── requirements.txt        # Python dependencies

- [API Documentation](#-api-documentation)

- [Architecture](#-architecture)- **Pattern Recognition**: Detects GPS coordinates using regex patterns│   ├── services/

- [Configuration](#-configuration)

- [Version History](#-version-history)- **WhatsApp GPS Overlay**: Specialized detection for WhatsApp location sharing images│   │   ├── gps_extractor.py   # GPS coordinate extraction (EXIF, OCR, patterns)

- [Contributing](#-contributing)

│   │   └── location_validator.py # Location validation against zones

## 🚀 Quick Start

### Location Validation│   ├── routes/

### Prerequisites

- **Zone Boundary Validation**: Validates coordinates against predefined administrative zones│   │   └── gps_api.py         # API endpoints

- Python 3.8 or higher

- Tesseract OCR installed on your system- **Multi-Zone Support**: Handles educational institutions, government zones, etc.│   └── data/

- Basic knowledge of REST APIs (optional)

- **Confidence Scoring**: Provides validation confidence based on distance from boundaries│       └── ward_boundaries.json # Administrative zone definitions

### Installation

- **Detailed Zone Information**: Returns contact details, departments, and addresses├── README.md                   # This file

1. **Clone the repository**

   ```bash└── requirements.txt           # Root dependencies

   git clone https://github.com/nitish-niraj/GPS-verification.git

   cd GPS-verification### Modern Web Interface```

   ```

- **Drag & Drop Upload**: Intuitive image upload with preview

2. **Install Tesseract OCR**

   - **Real-time Validation**: Instant GPS extraction and zone validation## 🛠️ Installation

   **Windows:**

   ```bash- **Responsive Design**: Works on desktop, tablet, and mobile devices

   # Download from: https://github.com/UB-Mannheim/tesseract/wiki

   # Install and note the installation path- **Interactive Results**: Visual display of GPS coordinates and zone information### 1. Install Python Dependencies

   ```

   - **Export Reports**: Download validation results as JSON```bash

   **Linux:**

   ```bashcd backend

   sudo apt-get install tesseract-ocr

   ```---pip install -r requirements.txt

   

   **macOS:**```

   ```bash

   brew install tesseract## 🚀 Quick Start

   ```

### 2. Install Tesseract OCR (Windows)

3. **Install Python dependencies**

   ```bash### Installation```bash

   pip install -r backend/requirements.txt

   ```winget install --id UB-Mannheim.TesseractOCR



4. **Configure Tesseract path (Windows only)**1. **Clone the repository**```

   

   Edit `backend/services/gps_extractor.py` if needed:```bash

   ```python

   tesseract_paths = [git clone https://github.com/nitish-niraj/GPS-verification.git### 3. Run the API

       r"D:\OCR-System\tesseract.exe",  # Your installation path

       r"C:\Program Files\Tesseract-OCR\tesseract.exe",cd GPS-verification```bash

   ]

   ``````python main.py



5. **Run the application**```

   ```bash

   cd backend2. **Install dependencies**

   python main.py

   ``````bashThe API will be available at: `http://localhost:8000`



6. **Access the application**cd backend

   - Web UI: http://localhost:8000/ui

   - API Docs: http://localhost:8000/docspip install -r requirements.txt## 🔌 API Endpoints

   - API Reference: http://localhost:8000/redoc

```

## 🎯 Usage

### Image GPS Validation

### Web Interface

3. **Start the server**```bash

1. Open your browser and navigate to `http://localhost:8000/ui`

2. Drag and drop an image or click to browse```bashPOST /api/v1/validate-image-location

3. Click "Validate Location"

4. View the results with GPS coordinates and validation statuspython main.py```



### API Usage```Upload an image to extract GPS coordinates and validate location.



#### Validate Image Location



```bash4. **Access the application****Example:**

curl -X POST "http://localhost:8000/api/v1/validate-image-location" \

  -F "file=@/path/to/image.jpg"- **Web UI**: http://localhost:8000/ui```bash

```

- **API Docs**: http://localhost:8000/docscurl -X POST http://localhost:8000/api/v1/validate-image-location \

**Response:**

```json- **Health Check**: http://localhost:8000/api/v1/health  -H "Content-Type: multipart/form-data" \

{

  "valid": true,  -F "file=@your-image.jpg"

  "gps": {

    "latitude": 31.2508,---```

    "longitude": 75.7054,

    "source": "ocr",

    "confidence": 0.8

  },## 📁 Project Structure### Direct Coordinate Validation

  "zone": {

    "name": "LPU_Main",```bash

    "full_name": "Lovely Professional University - Main Campus",

    "type": "educational_institution"```POST /api/v1/validate-coordinates?latitude=31.2509&longitude=75.7054

  },

  "message": "Location validated successfully"GPS-verification/```

}

```├── backend/                      # Backend API server



#### Validate Coordinates Directly│   ├── main.py                  # FastAPI entry point### List Available Zones



```bash│   ├── requirements.txt         # Python dependencies```bash

curl -X POST "http://localhost:8000/api/v1/validate-coordinates" \

  -H "Content-Type: application/json" \│   ├── routes/GET /api/v1/zones

  -d '{"latitude": 31.2508, "longitude": 75.7054}'

```│   │   └── gps_api.py          # API endpoints```



#### List Available Zones│   ├── services/



```bash│   │   ├── gps_extractor.py    # GPS extraction### Health Check

curl -X GET "http://localhost:8000/api/v1/zones"

```│   │   └── location_validator.py # Zone validation```bash



#### Health Check│   └── data/GET /api/v1/health



```bash│       └── ward_boundaries.json # Zone definitions```

curl -X GET "http://localhost:8000/api/v1/health"

```│



## 📚 API Documentation├── frontend/                     # Web UI## 📖 How It Works



The API is fully documented with interactive Swagger UI and ReDoc interfaces:│   ├── index.html               # Main page



- **Interactive API Docs (Swagger):** http://localhost:8000/docs│   ├── css/style.css            # Styling### GPS Extraction Process

  - Test endpoints directly in browser

  - View request/response schemas│   └── js/app.js                # Frontend logic1. **EXIF Data**: First tries to extract GPS from image metadata

  - Try out with real images

│2. **OCR Text**: Uses Tesseract to read coordinates from text overlays

- **API Reference (ReDoc):** http://localhost:8000/redoc

  - Clean, detailed documentation├── docker-compose.yml           # Docker config3. **Pattern Recognition**: Falls back to image pattern analysis

  - Schema definitions

  - Code examples└── README.md                    # Documentation4. **WhatsApp Detection**: Specifically handles WhatsApp GPS overlay format



### Available Endpoints```



| Method | Endpoint | Description |### Location Validation

|--------|----------|-------------|

| POST | `/api/v1/validate-image-location` | Upload image for GPS extraction and validation |---1. **Zone Matching**: Checks if coordinates fall within predefined zones

| POST | `/api/v1/validate-coordinates` | Validate lat/long coordinates directly |

| GET | `/api/v1/zones` | List all configured validation zones |2. **Confidence Scoring**: Calculates confidence based on distance from boundaries

| GET | `/api/v1/health` | Check API health and service status |

| GET | `/docs` | Interactive API documentation (Swagger) |## 📖 Usage3. **Zone Information**: Returns detailed zone information (name, type, contact details)

| GET | `/redoc` | API reference documentation |

| GET | `/ui` | Web-based user interface |



## 🏗️ Architecture### Web Interface## 🧪 Example Response



### System Overview



```1. Open http://localhost:8000/ui in your browser```json

┌─────────────────────────────────────────────────────┐

│                   Frontend (UI)                      │2. Drag & drop an image with GPS data{

│  - Apple Liquid Design (Glassmorphism)              │

│  - Drag & Drop Image Upload                         │3. Click "Validate Location"  "filename": "WhatsApp Image 2025-09-26.jpg",

│  - Real-time Validation Display                     │

└────────────────────┬────────────────────────────────┘4. View results with GPS coordinates and zone information  "extracted_gps": {

                     │

                     │ HTTP/REST API    "latitude": 31.2509,

                     │

┌────────────────────▼────────────────────────────────┐### API Usage    "longitude": 75.7054,

│              FastAPI Backend                         │

│  ┌──────────────────────────────────────────────┐  │    "source": "whatsapp_pattern",

│  │        GPS Extraction Layer                   │  │

│  │  1. EXIF Reader (Camera Metadata)            │  │**Validate Image:**    "confidence": 0.85,

│  │  2. OCR Engine (Tesseract - Text in Images)  │  │

│  │  3. Pattern Recognition (Fallback)           │  │```bash    "note": "Detected WhatsApp GPS overlay"

│  └──────────────────┬───────────────────────────┘  │

│                     │                                │curl -X POST "http://localhost:8000/api/v1/validate-image-location" \  },

│  ┌──────────────────▼───────────────────────────┐  │

│  │      Location Validation Layer               │  │  -F "file=@your-image.jpg"  "validation": {

│  │  - Polygon-based Geofencing                  │  │

│  │  - LPU Campus Boundary Validation            │  │```    "status": "valid",

│  │  - Zone Identification                       │  │

│  └──────────────────────────────────────────────┘  │    "zone_name": "Lovely Professional University - Main Campus",

└─────────────────────────────────────────────────────┘

```**Response:**    "zone_type": "educational_institution",



### Directory Structure```json    "department": "University Administration",



```{    "confidence": 0.72

GPS-verification/

├── backend/                    # Backend application  "filename": "whatsapp_location.jpg",  }

│   ├── main.py                # FastAPI application entry point

│   ├── requirements.txt       # Python dependencies  "extracted_gps": {}

│   ├── data/                  # Configuration data

│   │   └── ward_boundaries.json  # LPU campus boundaries    "latitude": 31.256577,```

│   ├── routes/                # API endpoints

│   │   └── gps_api.py        # GPS validation routes    "longitude": 75.704117,

│   └── services/              # Business logic

│       ├── gps_extractor.py  # GPS extraction service    "source": "pattern_recognition",## 🔧 Configuration

│       └── location_validator.py  # Location validation

├── frontend/                   # Frontend application    "confidence": 0.6

│   ├── index.html             # Main UI page

│   ├── css/  },### Zone Boundaries

│   │   └── style.css          # Apple-inspired styling

│   └── js/  "validation": {Edit `backend/data/ward_boundaries.json` to add or modify administrative zones:

│       └── app.js             # Frontend logic

├── docs/                       # Documentation    "status": "valid",

│   ├── API_DOCUMENTATION.md   # Complete API guide

│   └── INSTALLATION.md        # Installation guide    "zone_name": "Lovely Professional University - Main Campus",```json

├── requirements.txt           # Root dependencies

├── docker-compose.yml         # Docker configuration    "confidence": 0.73{

└── README.md                  # This file

```  }  "zones": [



## ⚙️ Configuration}    {



### LPU Campus Boundaries```      "id": "zone_1",



The system is pre-configured with **Lovely Professional University Main Campus** boundaries. The boundary data is stored in `backend/data/ward_boundaries.json`.      "name": "Zone Name",



**Zone Configuration:**### Python Example      "type": "zone_type",

- **Name:** LPU_Main

- **Full Name:** Lovely Professional University - Main Campus      "boundary": [

- **Location:** Jalandhar, Punjab, India

- **Contact:** +91-1824-517000```python        [longitude, latitude],

- **Email:** info@lpu.co.in

- **Type:** Educational Institutionimport requests        [longitude, latitude],



**To modify boundaries:**        ...



Edit `backend/data/ward_boundaries.json`:with open('image.jpg', 'rb') as f:      ]

```json

{    response = requests.post(    }

  "educational_zones": {

    "LPU_Main": {        'http://localhost:8000/api/v1/validate-image-location',  ]

      "name": "Lovely Professional University - Main Campus",

      "boundary": [        files={'file': f}}

        [31.26247867646305, 75.70427192645857],

        [31.2545439713566, 75.70000209962465],    )```

        // Add more coordinate pairs

      ]    

    }

  }result = response.json()### OCR Configuration

}

```print(f"Status: {result['validation']['status']}")The system automatically detects Tesseract installation. If needed, manually configure the path in `services/gps_extractor.py`.



### Tesseract OCR Configurationprint(f"Zone: {result['validation']['zone_name']}")



The system automatically searches for Tesseract in common installation paths:```## 🚦 Development



**Windows:**

- `D:\OCR-System\tesseract.exe`

- `C:\Program Files\Tesseract-OCR\tesseract.exe`---### Run in Development Mode

- `C:\Program Files (x86)\Tesseract-OCR\tesseract.exe`

```bash

**Linux/macOS:**

- `/usr/bin/tesseract`## 🔧 API Endpointspython main.py

- `/usr/local/bin/tesseract`

```

## 📊 Version History

| Method | Endpoint | Description |This starts the server with auto-reload enabled.

| Version | Release Date | Key Changes | Status |

|---------|-------------|-------------|---------||--------|----------|-------------|

| **3.0.0** | Oct 18, 2025 | 🎉 **Major Release**<br/>✅ Added Tesseract OCR integration<br/>✅ Implemented multi-method GPS extraction<br/>✅ Fixed fake GPS coordinate bug<br/>✅ Added comprehensive API documentation<br/>✅ Redesigned UI with glassmorphism<br/>✅ LPU campus boundary validation<br/>✅ Filename-independent extraction<br/>✅ Enhanced error handling | 🟢 Current |

| **2.0.0** | Oct 15, 2025 | ✅ Migrated to FastAPI<br/>✅ Added location validation<br/>✅ Improved error handling<br/>✅ RESTful API design | 🔵 Stable || GET | `/ui` | Web interface |### API Documentation

| **1.0.0** | Oct 10, 2025 | ✅ Initial release<br/>✅ Basic GPS extraction from EXIF | 🔵 Archived |

| POST | `/api/v1/validate-image-location` | Upload & validate image |Visit `http://localhost:8000/docs` for interactive API documentation.

### Version 3.0.0 Highlights

| POST | `/api/v1/validate-coordinates` | Validate coordinates |

✨ **New Features:**

- **OCR GPS Extraction:** Read GPS coordinates from screenshots and images with text overlays| GET | `/api/v1/zones` | List all zones |## 📝 License

- **Multi-Method Extraction:** EXIF → OCR → Pattern Recognition fallback chain

- **LPU Campus Validation:** Precise boundary validation for Lovely Professional University| GET | `/api/v1/health` | Health check |

- **Interactive API Docs:** Swagger UI and ReDoc interfaces

- **Apple-Inspired UI:** Modern glassmorphism design| GET | `/docs` | API documentation |This project is open source. Feel free to use and modify as needed.

- **Filename Independence:** Content-based extraction only



🐛 **Bug Fixes:**

- Fixed critical bug where fake GPS coordinates were returned for images without GPS data---## 🤝 Contributing

- Removed hardcoded fallback coordinates

- Improved OCR text parsing with better regex patterns

- Fixed logging configuration timing issues

## ⚙️ Configuration1. Fork the repository

🔧 **Improvements:**

- Better error messages and user feedback2. Create a feature branch

- Comprehensive logging for debugging

- Optimized image preprocessing for OCR### Add Custom Zones3. Make your changes

- Enhanced coordinate validation

- Production-ready deployment configuration4. Test thoroughly



## 🧪 TestingEdit `backend/data/ward_boundaries.json`:5. Submit a pull request



### Manual Testing



1. **Test with GPS-enabled image:**```json## 📞 Support

   ```bash

   curl -X POST "http://localhost:8000/api/v1/validate-image-location" \{

     -F "file=@image_with_gps.jpg"

   ```  "educational_zones": {For issues or questions, please check the API documentation at `/docs` or review the code comments for detailed explanations.

    "CustomZone": {

2. **Test with screenshot containing GPS text:**      "name": "Your Custom Zone",

   - Take a WhatsApp location screenshot showing "Latitude" and "Longitude"      "type": "educational_institution",

   - Upload through web UI at http://localhost:8000/ui      "contact": "+1-234-567-8900",

      "boundary": [

3. **Test with non-GPS image:**        [lat1, lon1],

   - Upload a regular photo without GPS data        [lat2, lon2],

   - Should return error: "No GPS coordinates found"        ...

      ]

### Health Check    }

  }

```bash}

curl http://localhost:8000/api/v1/health```

```

---

Expected response:

```json## 🐳 Docker Deployment

{

  "status": "healthy",```bash

  "ocr_available": true,docker-compose up -d

  "zones_loaded": 1,```

  "tesseract_version": "5.5.0.20241111"

}Access at: http://localhost:8000/ui

```

---

## 🚢 Deployment

## 🛠️ Technology Stack

### Production Deployment

**Backend:**

1. **Set environment variables:**- FastAPI - Web framework

   ```bash- Pillow - Image processing

   export ENVIRONMENT=production- pytesseract - OCR

   export LOG_LEVEL=INFO- Shapely - Geospatial calculations

   ```

**Frontend:**

2. **Run with Gunicorn:**- HTML5/CSS3 - Modern UI

   ```bash- Vanilla JavaScript - No dependencies

   gunicorn backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

   ```---



### Security Considerations## 🤝 Contributing



- ✅ Configure CORS origins in production1. Fork the repository

- ✅ Use HTTPS in production2. Create feature branch (`git checkout -b feature/AmazingFeature`)

- ✅ Implement rate limiting3. Commit changes (`git commit -m 'Add AmazingFeature'`)

- ✅ Add authentication if needed4. Push to branch (`git push origin feature/AmazingFeature`)

- ✅ Sanitize file uploads5. Open Pull Request

- ✅ Set up proper logging

---

## 🤝 Contributing

## 📝 License

Contributions are welcome! Please follow these guidelines:

MIT License - see LICENSE file for details.

1. Fork the repository

2. Create a feature branch: `git checkout -b feature/amazing-feature`---

3. Commit your changes: `git commit -m 'Add amazing feature'`

4. Push to the branch: `git push origin feature/amazing-feature`## 👥 Author

5. Open a Pull Request

**Nitish Niraj** - [@nitish-niraj](https://github.com/nitish-niraj)

## 📝 License

---

This project is licensed under the MIT License.

## 📞 Support

## 🙏 Acknowledgments

For support, open an issue on GitHub.

- **Lovely Professional University** for campus boundary data

- **Tesseract OCR** for text extraction capabilities---

- **FastAPI** for the excellent web framework

- **OpenCV** for image processing<div align="center">



## 📧 Contact**Made with ❤️ for accurate location validation**



**Project Maintainer:** Nitish Niraj  [⬆ Back to Top](#gps-verifier---location-validation-system)

**GitHub:** [@nitish-niraj](https://github.com/nitish-niraj)  

**Repository:** [GPS-verification](https://github.com/nitish-niraj/GPS-verification)</div>


## 🆘 Support

If you encounter any issues or have questions:

1. Check the [API Documentation](http://localhost:8000/docs)
2. Review the [Installation Guide](docs/INSTALLATION.md)
3. Open an issue on [GitHub](https://github.com/nitish-niraj/GPS-verification/issues)

## 🎓 Use Cases

- **Campus Security:** Validate student/staff locations within campus
- **Attendance Systems:** Verify location-based attendance
- **Delivery Services:** Confirm delivery within campus boundaries
- **Event Management:** Validate event participation locations
- **Research:** Geographic data analysis and validation

---

**Made with ❤️ for Lovely Professional University**

*Last Updated: October 18, 2025 - Version 3.0.0*
