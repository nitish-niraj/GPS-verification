# GPS Verifier - LPU Campus Location Validation System# GPS Verifier - LPU Campus Location Validation System



<div align="center"><div align="center">



[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/nitish-niraj/GPS-verification)[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/nitish-niraj/GPS-verification)

[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)

[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)



**A modern, intelligent GPS validation system designed for Lovely Professional University (LPU) campus****A modern, intelligent GPS validation system designed for Lovely Professional University (LPU) campus**



Extract GPS coordinates from images using multiple methods and validate locations against predefined campus boundaries.Extract GPS coordinates from images using multiple methods and validate locations against predefined campus boundaries.



</div></div>



------



## 🌟 Key Features## 🌟 Key Features



- **📸 Multi-Method GPS Extraction**- **📸 Multi-Method GPS Extraction**

  - EXIF metadata reading from camera photos  - EXIF metadata reading from camera photos

  - OCR text extraction using Tesseract (for screenshots)  - OCR text extraction using Tesseract (for screenshots)

  - Pattern recognition as fallback method  - Pattern recognition as fallback method

  - WhatsApp GPS overlay detection  - WhatsApp GPS overlay detection



- **🎯 LPU Campus Validation**- **🎯 LPU Campus Validation**

  - Precise boundary validation for LPU Main Campus  - Precise boundary validation for LPU Main Campus

  - Polygon-based geofencing  - Polygon-based geofencing

  - Detailed zone information  - Detailed zone information



- **🚀 Modern Tech Stack**- **🚀 Modern Tech Stack**

  - FastAPI for high-performance REST API  - FastAPI for high-performance REST API

  - Tesseract OCR for text extraction  - Tesseract OCR for text extraction

  - Apple-inspired glassmorphism UI  - Apple-inspired glassmorphism UI

  - Real-time validation  - Real-time validation



- **📱 Filename-Independent**- **� Filename-Independent**

  - Content-based extraction only  - Content-based extraction only

  - Works with images from any source  - Works with images from any source

  - No naming conventions required  - No naming conventions required



------



## 📋 Table of Contents  - Real-time validation



- [Quick Start](#quick-start)

- [Installation](#installation)

- [Usage](#usage)- **📱 Filename-Independent**

- [API Documentation](#api-documentation)

- [Architecture](#architecture)  - Content-based extraction only## ✨ Features```

- [Configuration](#configuration)

- [Version History](#version-history)## 📋 Table of Contents

- [Contributing](#contributing)

- [Quick Start](#-quick-start)

---- [Installation](#-installation)

- [Usage](#-usage)

## 🚀 Quick Start- [API Documentation](#-api-documentation)

- [Architecture](#-architecture)

### Prerequisites- [Configuration](#-configuration)

- [Version History](#-version-history)

- Python 3.8 or higher- [Contributing](#-contributing)

- Tesseract OCR installed on your system

- Basic knowledge of REST APIs (optional)---



### Installation## 🚀 Quick Start



1. **Clone the repository**### Prerequisites



   ```bash- Python 3.8 or higher

   git clone https://github.com/nitish-niraj/GPS-verification.git- Tesseract OCR installed on your system

   cd GPS-verification- Basic knowledge of REST APIs (optional)

   ```

### Installation

2. **Install Tesseract OCR**

1. **Clone the repository**

   **Windows:**

      ```bash

   ```bash   git clone https://github.com/nitish-niraj/GPS-verification.git

   # Download from: https://github.com/UB-Mannheim/tesseract/wiki   cd GPS-verification

   # Install and note the installation path   ```

   ```

2. **Install Tesseract OCR**

   **Linux:**

      **Windows:**

   ```bash   ```bash

   sudo apt-get install tesseract-ocr   # Download from: https://github.com/UB-Mannheim/tesseract/wiki

   ```   # Install and note the installation path

      ```

   **macOS:**

      **Linux:**

   ```bash   ```bash

   brew install tesseract   sudo apt-get install tesseract-ocr

   ```   ```

   

3. **Install Python dependencies**   **macOS:**

   ```bash

   ```bash   brew install tesseract

   pip install -r backend/requirements.txt   ```

   ```

3. **Install Python dependencies**

4. **Configure Tesseract path (Windows only)**

      ```bash

   Edit `backend/services/gps_extractor.py` if needed:   pip install -r backend/requirements.txt

      ```

   ```python

   tesseract_paths = [4. **Configure Tesseract path (Windows only)**

       r"D:\OCR-System\tesseract.exe",  # Your installation path   

       r"C:\Program Files\Tesseract-OCR\tesseract.exe",   Edit `backend/services/gps_extractor.py` if needed:

   ]   ```python

   ```   tesseract_paths = [

       r"D:\OCR-System\tesseract.exe",  # Your installation path

5. **Run the application**       r"C:\Program Files\Tesseract-OCR\tesseract.exe",

   ]

   ```bash   ```

   cd backend

   python main.py5. **Run the application**

   ```

   ```bash

6. **Access the application**   cd backend

   - Web UI: <http://localhost:8000/ui>   python main.py

   - API Docs: <http://localhost:8000/docs>   ```

   - API Reference: <http://localhost:8000/redoc>

6. **Access the application**

---   - Web UI: http://localhost:8000/ui

   - API Docs: http://localhost:8000/docs

## 🎯 Usage   - API Reference: http://localhost:8000/redoc



### Web Interface---



1. Open your browser and navigate to `http://localhost:8000/ui`   pip install -r backend/requirements.txt

2. Drag and drop an image or click to browse

3. Click "Validate Location"   ```winget install --id UB-Mannheim.TesseractOCR

4. View the results with GPS coordinates and validation status



### API Usage

4. **Configure Tesseract path (Windows only)**1. **Clone the repository**```

#### Validate Image Location

   

```bash

curl -X POST "http://localhost:8000/api/v1/validate-image-location" \   Edit `backend/services/gps_extractor.py` if needed:```bash

  -F "file=@/path/to/image.jpg"

```   ```python



**Response:**   tesseract_paths = [git clone https://github.com/nitish-niraj/GPS-verification.git### 3. Run the API



```json       r"D:\OCR-System\tesseract.exe",  # Your installation path

{

  "valid": true,       r"C:\Program Files\Tesseract-OCR\tesseract.exe",cd GPS-verification```bash

  "gps": {

    "latitude": 31.2508,   ]

    "longitude": 75.7054,

    "source": "ocr",   ``````python main.py

    "confidence": 0.8

  },

  "zone": {

    "name": "LPU_Main",5. **Run the application**```

    "full_name": "Lovely Professional University - Main Campus",

    "type": "educational_institution"   ```bash

  },

  "message": "Location validated successfully"   cd backend2. **Install dependencies**

}

```   python main.py



#### Validate Coordinates Directly   ``````bashThe API will be available at: `http://localhost:8000`



```bash

curl -X POST "http://localhost:8000/api/v1/validate-coordinates" \

  -H "Content-Type: application/json" \6. **Access the application**cd backend

  -d '{"latitude": 31.2508, "longitude": 75.7054}'

```   - Web UI: http://localhost:8000/ui



#### List Available Zones   - API Docs: http://localhost:8000/docspip install -r requirements.txt## 🔌 API Endpoints



```bash   - API Reference: http://localhost:8000/redoc

curl -X GET "http://localhost:8000/api/v1/zones"

``````



#### Health Check## 🎯 Usage



```bash### Image GPS Validation

curl -X GET "http://localhost:8000/api/v1/health"

```### Web Interface



Expected response:3. **Start the server**```bash



```json1. Open your browser and navigate to `http://localhost:8000/ui`

{

  "status": "healthy",2. Drag and drop an image or click to browse```bashPOST /api/v1/validate-image-location

  "ocr_available": true,

  "zones_loaded": 1,3. Click "Validate Location"

  "tesseract_version": "5.5.0.20241111"

}4. View the results with GPS coordinates and validation statuspython main.py```

```



---

### API Usage```Upload an image to extract GPS coordinates and validate location.

## 📚 API Documentation



The API is fully documented with interactive Swagger UI and ReDoc interfaces:

#### Validate Image Location

- **Interactive API Docs (Swagger):** <http://localhost:8000/docs>

  - Test endpoints directly in browser

  - View request/response schemas

  - Try out with real images```bash4. **Access the application****Example:**



- **API Reference (ReDoc):** <http://localhost:8000/redoc>curl -X POST "http://localhost:8000/api/v1/validate-image-location" \

  - Clean, detailed documentation

  - Schema definitions  -F "file=@/path/to/image.jpg"- **Web UI**: http://localhost:8000/ui```bash

  - Code examples

```

### Available Endpoints

- **API Docs**: http://localhost:8000/docscurl -X POST http://localhost:8000/api/v1/validate-image-location \

| Method | Endpoint | Description |

|--------|----------|-------------|**Response:**

| POST | `/api/v1/validate-image-location` | Upload image for GPS extraction and validation |

| POST | `/api/v1/validate-coordinates` | Validate lat/long coordinates directly |```json- **Health Check**: http://localhost:8000/api/v1/health  -H "Content-Type: multipart/form-data" \

| GET | `/api/v1/zones` | List all configured validation zones |

| GET | `/api/v1/health` | Check API health and service status |{

| GET | `/docs` | Interactive API documentation (Swagger) |

| GET | `/redoc` | API reference documentation |  "valid": true,  -F "file=@your-image.jpg"

| GET | `/ui` | Web-based user interface |

  "gps": {

---

    "latitude": 31.2508,---```

## 🏗️ Architecture

    "longitude": 75.7054,

### System Overview

    "source": "ocr",

```

┌─────────────────────────────────────────────────────┐    "confidence": 0.8

│                   Frontend (UI)                      │

│  - Apple Liquid Design (Glassmorphism)              │  },## 📁 Project Structure### Direct Coordinate Validation

│  - Drag & Drop Image Upload                         │

│  - Real-time Validation Display                     │  "zone": {

└────────────────────┬────────────────────────────────┘

                     │    "name": "LPU_Main",```bash

                     │ HTTP/REST API

                     │    "full_name": "Lovely Professional University - Main Campus",

┌────────────────────▼────────────────────────────────┐

│              FastAPI Backend                         │    "type": "educational_institution"```POST /api/v1/validate-coordinates?latitude=31.2509&longitude=75.7054

│  ┌──────────────────────────────────────────────┐  │

│  │        GPS Extraction Layer                   │  │  },

│  │  1. EXIF Reader (Camera Metadata)            │  │

│  │  2. OCR Engine (Tesseract - Text in Images)  │  │  "message": "Location validated successfully"GPS-verification/```

│  │  3. Pattern Recognition (Fallback)           │  │

│  └──────────────────┬───────────────────────────┘  │}

│                     │                                │

│  ┌──────────────────▼───────────────────────────┐  │```├── backend/                      # Backend API server

│  │      Location Validation Layer               │  │

│  │  - Polygon-based Geofencing                  │  │

│  │  - LPU Campus Boundary Validation            │  │

│  │  - Zone Identification                       │  │#### Validate Coordinates Directly│   ├── main.py                  # FastAPI entry point### List Available Zones

│  └──────────────────────────────────────────────┘  │

└─────────────────────────────────────────────────────┘

```

```bash│   ├── requirements.txt         # Python dependencies```bash

### Directory Structure

curl -X POST "http://localhost:8000/api/v1/validate-coordinates" \

```

GPS-verification/  -H "Content-Type: application/json" \│   ├── routes/GET /api/v1/zones

├── backend/                    # Backend application

│   ├── main.py                # FastAPI application entry point  -d '{"latitude": 31.2508, "longitude": 75.7054}'

│   ├── requirements.txt       # Python dependencies

│   ├── data/                  # Configuration data```│   │   └── gps_api.py          # API endpoints```

│   │   └── ward_boundaries.json  # LPU campus boundaries

│   ├── routes/                # API endpoints

│   │   └── gps_api.py        # GPS validation routes

│   └── services/              # Business logic#### List Available Zones│   ├── services/

│       ├── gps_extractor.py  # GPS extraction service

│       └── location_validator.py  # Location validation

├── frontend/                   # Frontend application

│   ├── index.html             # Main UI page```bash│   │   ├── gps_extractor.py    # GPS extraction### Health Check

│   ├── css/

│   │   └── style.css          # Apple-inspired stylingcurl -X GET "http://localhost:8000/api/v1/zones"

│   └── js/

│       └── app.js             # Frontend logic```│   │   └── location_validator.py # Zone validation```bash

├── docs/                       # Documentation

│   ├── API_DOCUMENTATION.md   # Complete API guide

│   └── INSTALLATION.md        # Installation guide

├── requirements.txt           # Root dependencies#### Health Check│   └── data/GET /api/v1/health

├── docker-compose.yml         # Docker configuration

└── README.md                  # This file

```

```bash│       └── ward_boundaries.json # Zone definitions```

---

curl -X GET "http://localhost:8000/api/v1/health"

## ⚙️ Configuration

```│

### LPU Campus Boundaries



The system is pre-configured with **Lovely Professional University Main Campus** boundaries. The boundary data is stored in `backend/data/ward_boundaries.json`.

## 📚 API Documentation├── frontend/                     # Web UI## 📖 How It Works

**Zone Configuration:**

- **Name:** LPU_Main

- **Full Name:** Lovely Professional University - Main Campus

- **Location:** Jalandhar, Punjab, IndiaThe API is fully documented with interactive Swagger UI and ReDoc interfaces:│   ├── index.html               # Main page

- **Contact:** +91-1824-517000

- **Email:** info@lpu.co.in

- **Type:** Educational Institution

- **Interactive API Docs (Swagger):** http://localhost:8000/docs│   ├── css/style.css            # Styling### GPS Extraction Process

**To modify boundaries:**

  - Test endpoints directly in browser

Edit `backend/data/ward_boundaries.json`:

  - View request/response schemas│   └── js/app.js                # Frontend logic1. **EXIF Data**: First tries to extract GPS from image metadata

```json

{  - Try out with real images

  "educational_zones": {

    "LPU_Main": {│2. **OCR Text**: Uses Tesseract to read coordinates from text overlays

      "name": "Lovely Professional University - Main Campus",

      "boundary": [- **API Reference (ReDoc):** http://localhost:8000/redoc

        [31.26247867646305, 75.70427192645857],

        [31.2545439713566, 75.70000209962465],  - Clean, detailed documentation├── docker-compose.yml           # Docker config3. **Pattern Recognition**: Falls back to image pattern analysis

        // Add more coordinate pairs

      ]  - Schema definitions

    }

  }  - Code examples└── README.md                    # Documentation4. **WhatsApp Detection**: Specifically handles WhatsApp GPS overlay format

}

```



### Tesseract OCR Configuration### Available Endpoints```



The system automatically searches for Tesseract in common installation paths:



**Windows:**| Method | Endpoint | Description |### Location Validation

- `D:\OCR-System\tesseract.exe`

- `C:\Program Files\Tesseract-OCR\tesseract.exe`|--------|----------|-------------|

- `C:\Program Files (x86)\Tesseract-OCR\tesseract.exe`

| POST | `/api/v1/validate-image-location` | Upload image for GPS extraction and validation |---1. **Zone Matching**: Checks if coordinates fall within predefined zones

**Linux/macOS:**

- `/usr/bin/tesseract`| POST | `/api/v1/validate-coordinates` | Validate lat/long coordinates directly |

- `/usr/local/bin/tesseract`

| GET | `/api/v1/zones` | List all configured validation zones |2. **Confidence Scoring**: Calculates confidence based on distance from boundaries

---

| GET | `/api/v1/health` | Check API health and service status |

## 📊 Version History

| GET | `/docs` | Interactive API documentation (Swagger) |## 📖 Usage3. **Zone Information**: Returns detailed zone information (name, type, contact details)

| Version | Release Date | Key Changes | Status |

|---------|-------------|-------------|--------|| GET | `/redoc` | API reference documentation |

| **3.0.0** | Oct 18, 2025 | 🎉 **Major Release**<br/>✅ Added Tesseract OCR integration<br/>✅ Implemented multi-method GPS extraction<br/>✅ Fixed fake GPS coordinate bug<br/>✅ Added comprehensive API documentation<br/>✅ Redesigned UI with glassmorphism<br/>✅ LPU campus boundary validation<br/>✅ Filename-independent extraction<br/>✅ Enhanced error handling | 🟢 Current |

| **2.0.0** | Oct 15, 2025 | ✅ Migrated to FastAPI<br/>✅ Added location validation<br/>✅ Improved error handling<br/>✅ RESTful API design | 🔵 Stable || GET | `/ui` | Web-based user interface |

| **1.0.0** | Oct 10, 2025 | ✅ Initial release<br/>✅ Basic GPS extraction from EXIF | 🔵 Archived |



### Version 3.0.0 Highlights

## 🏗️ Architecture### Web Interface## 🧪 Example Response

✨ **New Features:**

- **OCR GPS Extraction:** Read GPS coordinates from screenshots and images with text overlays

- **Multi-Method Extraction:** EXIF → OCR → Pattern Recognition fallback chain

- **LPU Campus Validation:** Precise boundary validation for Lovely Professional University### System Overview

- **Interactive API Docs:** Swagger UI and ReDoc interfaces

- **Apple-Inspired UI:** Modern glassmorphism design

- **Filename Independence:** Content-based extraction only

```1. Open http://localhost:8000/ui in your browser```json

🐛 **Bug Fixes:**

- Fixed critical bug where fake GPS coordinates were returned for images without GPS data┌─────────────────────────────────────────────────────┐

- Removed hardcoded fallback coordinates

- Improved OCR text parsing with better regex patterns│                   Frontend (UI)                      │2. Drag & drop an image with GPS data{

- Fixed logging configuration timing issues

│  - Apple Liquid Design (Glassmorphism)              │

🔧 **Improvements:**

- Better error messages and user feedback│  - Drag & Drop Image Upload                         │3. Click "Validate Location"  "filename": "WhatsApp Image 2025-09-26.jpg",

- Comprehensive logging for debugging

- Optimized image preprocessing for OCR│  - Real-time Validation Display                     │

- Enhanced coordinate validation

- Production-ready deployment configuration└────────────────────┬────────────────────────────────┘4. View results with GPS coordinates and zone information  "extracted_gps": {



---                     │



## 🧪 Testing                     │ HTTP/REST API    "latitude": 31.2509,



### Manual Testing                     │



1. **Test with GPS-enabled image:**┌────────────────────▼────────────────────────────────┐### API Usage    "longitude": 75.7054,

   ```bash

   curl -X POST "http://localhost:8000/api/v1/validate-image-location" \│              FastAPI Backend                         │

     -F "file=@image_with_gps.jpg"

   ```│  ┌──────────────────────────────────────────────┐  │    "source": "whatsapp_pattern",



2. **Test with screenshot containing GPS text:**│  │        GPS Extraction Layer                   │  │

   - Take a WhatsApp location screenshot showing "Latitude" and "Longitude"

   - Upload through web UI at <http://localhost:8000/ui>│  │  1. EXIF Reader (Camera Metadata)            │  │**Validate Image:**    "confidence": 0.85,



3. **Test with non-GPS image:**│  │  2. OCR Engine (Tesseract - Text in Images)  │  │

   - Upload a regular photo without GPS data

   - Should return error: "No GPS coordinates found"│  │  3. Pattern Recognition (Fallback)           │  │```bash    "note": "Detected WhatsApp GPS overlay"



### Health Check│  └──────────────────┬───────────────────────────┘  │



```bash│                     │                                │curl -X POST "http://localhost:8000/api/v1/validate-image-location" \  },

curl http://localhost:8000/api/v1/health

```│  ┌──────────────────▼───────────────────────────┐  │



Expected response:│  │      Location Validation Layer               │  │  -F "file=@your-image.jpg"  "validation": {



```json│  │  - Polygon-based Geofencing                  │  │

{

  "status": "healthy",│  │  - LPU Campus Boundary Validation            │  │```    "status": "valid",

  "ocr_available": true,

  "zones_loaded": 1,│  │  - Zone Identification                       │  │

  "tesseract_version": "5.5.0.20241111"

}│  └──────────────────────────────────────────────┘  │    "zone_name": "Lovely Professional University - Main Campus",

```

└─────────────────────────────────────────────────────┘

---

```**Response:**    "zone_type": "educational_institution",

## 🚢 Deployment



### Production Deployment

### Directory Structure```json    "department": "University Administration",

1. **Set environment variables:**

   ```bash

   export ENVIRONMENT=production

   export LOG_LEVEL=INFO```{    "confidence": 0.72

   ```

GPS-verification/

2. **Run with Gunicorn:**

   ```bash├── backend/                    # Backend application  "filename": "whatsapp_location.jpg",  }

   gunicorn backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

   ```│   ├── main.py                # FastAPI application entry point



### Docker Deployment│   ├── requirements.txt       # Python dependencies  "extracted_gps": {}



```bash│   ├── data/                  # Configuration data

docker-compose up -d

```│   │   └── ward_boundaries.json  # LPU campus boundaries    "latitude": 31.256577,```



Access at: <http://localhost:8000/ui>│   ├── routes/                # API endpoints



### Security Considerations│   │   └── gps_api.py        # GPS validation routes    "longitude": 75.704117,



- ✅ Configure CORS origins in production│   └── services/              # Business logic

- ✅ Use HTTPS in production

- ✅ Implement rate limiting│       ├── gps_extractor.py  # GPS extraction service    "source": "pattern_recognition",## 🔧 Configuration

- ✅ Add authentication if needed

- ✅ Sanitize file uploads│       └── location_validator.py  # Location validation

- ✅ Set up proper logging

├── frontend/                   # Frontend application    "confidence": 0.6

---

│   ├── index.html             # Main UI page

## 🤝 Contributing

│   ├── css/  },### Zone Boundaries

Contributions are welcome! Please follow these guidelines:

│   │   └── style.css          # Apple-inspired styling

1. Fork the repository

2. Create a feature branch: `git checkout -b feature/amazing-feature`│   └── js/  "validation": {Edit `backend/data/ward_boundaries.json` to add or modify administrative zones:

3. Commit your changes: `git commit -m 'Add amazing feature'`

4. Push to the branch: `git push origin feature/amazing-feature`│       └── app.js             # Frontend logic

5. Open a Pull Request

├── docs/                       # Documentation    "status": "valid",

---

│   ├── API_DOCUMENTATION.md   # Complete API guide

## 📝 License

│   └── INSTALLATION.md        # Installation guide    "zone_name": "Lovely Professional University - Main Campus",```json

This project is licensed under the MIT License.

├── requirements.txt           # Root dependencies

---

├── docker-compose.yml         # Docker configuration    "confidence": 0.73{

## 🙏 Acknowledgments

└── README.md                  # This file

- **Lovely Professional University** for campus boundary data

- **Tesseract OCR** for text extraction capabilities```  }  "zones": [

- **FastAPI** for the excellent web framework

- **OpenCV** for image processing



---## ⚙️ Configuration}    {



## 📧 Contact



**Project Maintainer:** Nitish Niraj### LPU Campus Boundaries```      "id": "zone_1",



**GitHub:** [@nitish-niraj](https://github.com/nitish-niraj)



**Repository:** [GPS-verification](https://github.com/nitish-niraj/GPS-verification)The system is pre-configured with **Lovely Professional University Main Campus** boundaries. The boundary data is stored in `backend/data/ward_boundaries.json`.      "name": "Zone Name",



---



## 🆘 Support**Zone Configuration:**### Python Example      "type": "zone_type",



If you encounter any issues or have questions:- **Name:** LPU_Main



1. Check the [API Documentation](http://localhost:8000/docs)- **Full Name:** Lovely Professional University - Main Campus      "boundary": [

2. Review the [Installation Guide](docs/INSTALLATION.md)

3. Open an issue on [GitHub](https://github.com/nitish-niraj/GPS-verification/issues)- **Location:** Jalandhar, Punjab, India



---- **Contact:** +91-1824-517000```python        [longitude, latitude],



## 🎓 Use Cases- **Email:** info@lpu.co.in



- **Campus Security:** Validate student/staff locations within campus- **Type:** Educational Institutionimport requests        [longitude, latitude],

- **Attendance Systems:** Verify location-based attendance

- **Delivery Services:** Confirm delivery within campus boundaries

- **Event Management:** Validate event participation locations

- **Research:** Geographic data analysis and validation**To modify boundaries:**        ...



---



<div align="center">Edit `backend/data/ward_boundaries.json`:with open('image.jpg', 'rb') as f:      ]



**Made with ❤️ for Lovely Professional University**```json



*Last Updated: October 18, 2025 - Version 3.0.0*{    response = requests.post(    }



</div>  "educational_zones": {


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
