# GPS Verifier — LPU Campus Location Validation System

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/nitish-niraj/GPS-verification)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

**A modern, multi-method GPS validation system for Lovely Professional University (LPU) campus.**

Extract GPS coordinates from images (EXIF, OCR, pattern recognition, WhatsApp overlays) and validate them against predefined campus boundaries.

---

## 🌟 Key Features

* **Multi-method GPS extraction**

  * EXIF metadata reading
  * OCR (Tesseract) for text overlays and screenshots
  * Pattern recognition fallback
  * WhatsApp GPS overlay detection

* **LPU Campus validation**

  * Polygon-based geofencing
  * Precise LPU Main Campus boundary validation
  * Zone identification and metadata (contact, type, etc.)

* **Modern tech stack & UX**

  * FastAPI backend (REST)
  * Tesseract OCR + OpenCV preprocessing
  * Lightweight Web UI (glassmorphism-inspired)
  * Content-based extraction (filename-independent)

---

## 📋 Table of Contents

* [Quick Start](#quick-start)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)

  * [Web UI](#web-ui)
  * [API](#api)
* [Configuration](#configuration)
* [Architecture](#architecture)
* [Directory structure](#directory-structure)
* [API Endpoints](#api-endpoints)
* [Health check](#health-check)
* [Version history](#version-history)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## 🚀 Quick Start

1. Clone the repo:

```bash
git clone https://github.com/nitish-niraj/GPS-verification.git
cd GPS-verification
```

2. Install dependencies (use a virtualenv):

```bash
pip install -r backend/requirements.txt
```

3. Ensure Tesseract OCR is installed and available on PATH. If on Windows, note the installation path to configure in `backend/services/gps_extractor.py`.

4. Start the backend (development):

```bash
# from repository root
cd backend
python main.py
```

5. Open the UI at: `http://localhost:8000/ui`

API docs: `http://localhost:8000/docs` — Redoc: `http://localhost:8000/redoc`

---

## 🧾 Prerequisites

* Python 3.8+
* Tesseract OCR (system installer)
* Optional: Docker & docker-compose for containerized deployment

### Installing Tesseract

**Windows**: Download from UB Mannheim builds or install via winget.

**Ubuntu / Debian**:

```bash
sudo apt-get update && sudo apt-get install -y tesseract-ocr
```

**macOS**:

```bash
brew install tesseract
```

If Tesseract is installed in a non-standard location on Windows, configure `tesseract_paths` in `backend/services/gps_extractor.py`.

---

## ✅ Usage

### Web UI

1. Open `http://localhost:8000/ui` in a browser.
2. Drag & drop an image or browse to upload.
3. Click **Validate Location** and view the result (extracted GPS, source, confidence, zone info).

### API Examples

**Validate image (multipart/form-data):**

```bash
curl -X POST "http://localhost:8000/api/v1/validate-image-location" \
  -F "file=@/path/to/image.jpg"
```

**Validate coordinates (JSON):**

```bash
curl -X POST "http://localhost:8000/api/v1/validate-coordinates" \
  -H "Content-Type: application/json" \
  -d '{"latitude": 31.2508, "longitude": 75.7054}'
```

**List zones:**

```bash
curl -X GET "http://localhost:8000/api/v1/zones"
```

---

## 🏗️ Architecture

**Frontend (UI)** — Glassmorphism-inspired HTML/CSS/JS, drag & drop upload, validation display.

**FastAPI Backend** — Receives uploads, runs GPS extraction pipeline, validates coordinates using polygon geofencing.

**GPS Extraction Layer**:

* EXIF Reader
* OCR (pytesseract) with OpenCV preprocessing
* Pattern recognition (WhatsApp overlay detection)

**Location Validation Layer**:

* Shapely-based polygon containment checks
* Confidence scoring (distance from boundary, extraction source)

---

## 📁 Directory structure (high level)

```
GPS-verification/
├── backend/
│   ├── main.py                  # FastAPI entrypoint
│   ├── requirements.txt
│   ├── data/
│   │   └── ward_boundaries.json # zone definitions
│   ├── routes/
│   │   └── gps_api.py
│   └── services/
│       ├── gps_extractor.py
│       └── location_validator.py
├── frontend/
│   ├── index.html
│   ├── css/style.css
│   └── js/app.js
├── docs/
│   ├── API_DOCUMENTATION.md
│   └── INSTALLATION.md
├── docker-compose.yml
└── README.md
```

---

## 🔌 API Endpoints

| Method | Endpoint                          | Description                                  |
| ------ | --------------------------------- | -------------------------------------------- |
| POST   | `/api/v1/validate-image-location` | Upload image for GPS extraction & validation |
| POST   | `/api/v1/validate-coordinates`    | Validate latitude/longitude directly         |
| GET    | `/api/v1/zones`                   | List configured zones                        |
| GET    | `/api/v1/health`                  | Health check                                 |
| GET    | `/docs`                           | Swagger interactive docs                     |
| GET    | `/redoc`                          | ReDoc API reference                          |
| GET    | `/ui`                             | Web UI                                       |

---

## 🔍 Health check

**Endpoint:** `GET /api/v1/health`

**Example response:**

```json
{
  "status": "healthy",
  "ocr_available": true,
  "zones_loaded": 1,
  "tesseract_version": "5.5.0"
}
```

---

## ⚙️ Configuration

* Zone boundaries live at `backend/data/ward_boundaries.json`.
* On Windows, update the `tesseract_paths` list in `backend/services/gps_extractor.py` if Tesseract is not on PATH.

Example `tesseract_paths` (Python list):

```python
tesseract_paths = [
    r"D:\OCR-System\tesseract.exe",
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]
```

---

## 🧪 Testing

**Manual tests:**

1. GPS-enabled photo: should return EXIF source and high confidence.
2. WhatsApp location screenshot: OCR or pattern source, moderate-to-high confidence.
3. Non-GPS image: should return `No GPS coordinates found` with appropriate HTTP status.

---

## 📊 Version history

| Version | Release Date | Highlights                                                                                                    |
| ------: | ------------ | ------------------------------------------------------------------------------------------------------------- |
|   3.0.0 | 2025-10-18   | Added Tesseract OCR, multi-method extraction, LPU boundary validation, redesigned UI, improved error handling |
|   2.0.0 | 2025-10-15   | Migrated to FastAPI, added location validation                                                                |
|   1.0.0 | 2025-10-10   | Initial release — EXIF-based extraction                                                                       |

---

## 🤝 Contributing

Contributions are welcome. Please follow this workflow:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit with clear message
4. Push and open a Pull Request

See `CONTRIBUTING.md` (or add one) for more details.

---

## 📝 License

This project is licensed under the MIT License — see `LICENSE`.

---

## 📧 Contact

**Project maintainer:** Nitish Niraj — [GitHub @nitish-niraj](https://github.com/nitish-niraj)

For issues/questions:

1. Check API docs: `http://localhost:8000/docs`
2. Read installation guide in `/docs`
3. Open an issue: [https://github.com/nitish-niraj/GPS-verification/issues](https://github.com/nitish-niraj/GPS-verification/issues)

---

*Made with ❤️ for Lovely Professional University*

*Last updated: October 18, 2025 — Version 3.0.0*
