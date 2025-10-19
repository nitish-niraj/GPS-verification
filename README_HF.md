---
title: GPS Verifier - LPU Location Validation
emoji: 📍
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
license: mit
tags:
  - gps
  - location-validation
  - ocr
  - fastapi
  - computer-vision
---

# 📍 GPS Verifier - Location Validation System

<div align="center">

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/nitish-niraj/GPS-verification)
[![Python](https://img.shields.io/badge/python-3.9+-green.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)

**A modern, intelligent GPS validation system designed for Lovely Professional University (LPU) campus**

</div>

---

## 🌟 Features

- **📸 Multi-Method GPS Extraction**
  - EXIF metadata reading from camera photos
  - OCR text extraction using Tesseract (for screenshots)
  - Pattern recognition as fallback method
  - WhatsApp GPS overlay detection

- **🎯 LPU Campus Validation**
  - Precise boundary validation for LPU Main Campus
  - Polygon-based geofencing
  - Detailed zone information

- **🚀 Modern Tech Stack**
  - FastAPI for high-performance REST API
  - Tesseract OCR for text extraction
  - Apple-inspired glassmorphism UI
  - Real-time validation

---

## 🚀 Quick Start

### Web Interface

1. Click the **App** tab above
2. Navigate to the **Upload** section
3. Drag and drop an image with GPS data or click to browse
4. Click **"Validate Location"**
5. View results with GPS coordinates and validation status

### API Usage

#### Validate Image Location

```bash
curl -X POST "https://YOUR_USERNAME-gps-verifier-lpu.hf.space/api/v1/validate-image-location" \
  -F "file=@your_image.jpg"
```

#### Check API Health

```bash
curl "https://YOUR_USERNAME-gps-verifier-lpu.hf.space/api/v1/health"
```

---

## 📚 API Documentation

- **Interactive API Docs (Swagger)**: `/docs`
- **API Reference (ReDoc)**: `/redoc`
- **Web UI**: `/ui`

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/validate-image-location` | Upload image for GPS extraction and validation |
| POST | `/api/v1/validate-coordinates` | Validate lat/long coordinates directly |
| GET | `/api/v1/zones` | List all configured validation zones |
| GET | `/api/v1/health` | Check API health and service status |

---

## 🎯 Use Cases

- **Campus Security**: Validate student/staff locations within campus
- **Attendance Systems**: Verify location-based attendance
- **Delivery Services**: Confirm delivery within campus boundaries
- **Event Management**: Validate event participation locations
- **Research**: Geographic data analysis and validation

---

## 🏗️ Technology Stack

- **Backend**: FastAPI (Python)
- **OCR Engine**: Tesseract 5.x
- **Image Processing**: OpenCV, Pillow
- **Geospatial**: Shapely
- **Frontend**: Vanilla JavaScript with Apple-inspired design

---

## 📊 Example Response

```json
{
  "valid": true,
  "gps": {
    "latitude": 31.2508,
    "longitude": 75.7054,
    "source": "ocr",
    "confidence": 0.8
  },
  "zone": {
    "name": "LPU_Main",
    "full_name": "Lovely Professional University - Main Campus",
    "type": "educational_institution"
  },
  "message": "Location validated successfully"
}
```

---

## 📧 Contact & Support

**Project Maintainer**: Nitish Niraj

**GitHub Repository**: [GPS-verification](https://github.com/nitish-niraj/GPS-verification)

**Issues**: [Report a bug](https://github.com/nitish-niraj/GPS-verification/issues)

---

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">

**Made with ❤️ for Lovely Professional University**

*Version 3.0.0 - Deployed on Hugging Face Spaces*

</div>
