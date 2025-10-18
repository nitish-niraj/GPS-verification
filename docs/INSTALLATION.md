# Installation Guide - GPS Verifier

This guide provides detailed installation instructions for the GPS Verifier system.

## Table of Contents

- [System Requirements](#system-requirements)
- [Windows Installation](#windows-installation)
- [Linux Installation](#linux-installation)
- [macOS Installation](#macos-installation)
- [Docker Installation](#docker-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements

- **OS:** Windows 10/11, Ubuntu 20.04+, macOS 11+
- **Python:** 3.8 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Disk Space:** 500MB for dependencies
- **Internet:** Required for initial setup

### Required Software

1. **Python 3.8+**
2. **Tesseract OCR 5.0+**
3. **pip** (Python package manager)
4. **Git** (for cloning repository)

## Windows Installation

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important:** Check "Add Python to PATH"
4. Verify installation:
   ```powershell
   python --version
   ```

### Step 2: Install Tesseract OCR

1. Download Tesseract installer from:
   https://github.com/UB-Mannheim/tesseract/wiki

2. Run the installer (e.g., `tesseract-ocr-w64-setup-5.5.0.20241111.exe`)

3. Note the installation path (default: `C:\Program Files\Tesseract-OCR`)

4. Verify installation:
   ```powershell
   tesseract --version
   ```

### Step 3: Clone Repository

```powershell
git clone https://github.com/nitish-niraj/GPS-verification.git
cd GPS-verification
```

### Step 4: Install Python Dependencies

```powershell
pip install -r backend/requirements.txt
```

### Step 5: Configure Tesseract Path

Edit `backend/services/gps_extractor.py` if Tesseract is not in the default location:

```python
tesseract_paths = [
    r"C:\Your\Custom\Path\tesseract.exe",  # Add your path
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
]
```

### Step 6: Run the Application

```powershell
cd backend
python main.py
```

Access the application at: http://localhost:8000/ui

## Linux Installation

### Step 1: Install Python

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**CentOS/RHEL:**
```bash
sudo yum install python3 python3-pip
```

Verify installation:
```bash
python3 --version
```

### Step 2: Install Tesseract OCR

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

**CentOS/RHEL:**
```bash
sudo yum install epel-release
sudo yum install tesseract tesseract-devel
```

Verify installation:
```bash
tesseract --version
```

### Step 3: Clone Repository

```bash
git clone https://github.com/nitish-niraj/GPS-verification.git
cd GPS-verification
```

### Step 4: Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 5: Install Python Dependencies

```bash
pip install -r backend/requirements.txt
```

### Step 6: Run the Application

```bash
cd backend
python main.py
```

Access the application at: http://localhost:8000/ui

## macOS Installation

### Step 1: Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install Python

```bash
brew install python@3.11
```

Verify installation:
```bash
python3 --version
```

### Step 3: Install Tesseract OCR

```bash
brew install tesseract
```

Verify installation:
```bash
tesseract --version
```

### Step 4: Clone Repository

```bash
git clone https://github.com/nitish-niraj/GPS-verification.git
cd GPS-verification
```

### Step 5: Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 6: Install Python Dependencies

```bash
pip install -r backend/requirements.txt
```

### Step 7: Run the Application

```bash
cd backend
python main.py
```

Access the application at: http://localhost:8000/ui

## Docker Installation

### Prerequisites

- Docker installed
- Docker Compose installed

### Step 1: Clone Repository

```bash
git clone https://github.com/nitish-niraj/GPS-verification.git
cd GPS-verification
```

### Step 2: Build and Run with Docker Compose

```bash
docker-compose up -d
```

### Step 3: Access the Application

- Web UI: http://localhost:8000/ui
- API Docs: http://localhost:8000/docs

### Step 4: View Logs

```bash
docker-compose logs -f
```

### Step 5: Stop the Application

```bash
docker-compose down
```

## Verification

After installation, verify the system is working correctly:

### 1. Check Health Endpoint

```bash
curl http://localhost:8000/api/v1/health
```

Expected response:
```json
{
  "status": "healthy",
  "ocr_available": true,
  "zones_loaded": 1,
  "tesseract_version": "5.5.0.20241111"
}
```

### 2. Test Web UI

1. Open http://localhost:8000/ui in your browser
2. You should see the GPS Verifier interface
3. Try uploading a test image

### 3. Test API Endpoints

```bash
# Test zones endpoint
curl http://localhost:8000/api/v1/zones

# Test coordinate validation
curl -X POST "http://localhost:8000/api/v1/validate-coordinates" \
  -H "Content-Type: application/json" \
  -d '{"latitude": 31.2508, "longitude": 75.7054}'
```

## Troubleshooting

### Common Issues

#### 1. Tesseract Not Found

**Error:** `⚠️ Tesseract executable not found`

**Solution:**
- Windows: Ensure Tesseract is installed and path is correctly configured in `gps_extractor.py`
- Linux/macOS: Install tesseract using package manager

#### 2. Module Import Errors

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
pip install -r backend/requirements.txt
```

#### 3. Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Find process using port 8000
# Windows:
netstat -ano | findstr :8000

# Linux/macOS:
lsof -i :8000

# Kill the process or use a different port
# Edit backend/main.py and change the port:
uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
```

#### 4. Permission Denied

**Error:** `Permission denied`

**Solution:**
- Linux/macOS: Use `sudo` or fix file permissions
- Windows: Run terminal as Administrator

#### 5. OCR Not Working

**Error:** GPS not extracted from images with text

**Solution:**
1. Verify Tesseract installation:
   ```bash
   tesseract --version
   ```
2. Check Tesseract path in `backend/services/gps_extractor.py`
3. Ensure image has clear, readable GPS text
4. Check logs for OCR errors

### Getting Help

If you encounter issues:

1. Check the [README.md](../README.md) for general information
2. Review logs in terminal output
3. Check [API Documentation](API_DOCUMENTATION.md)
4. Open an issue on [GitHub](https://github.com/nitish-niraj/GPS-verification/issues)

## Development Setup

For development, install additional dependencies:

```bash
# Install dev dependencies
pip install pytest pytest-cov black flake8

# Run tests (if available)
pytest backend/tests/

# Format code
black backend/

# Lint code
flake8 backend/
```

## Production Deployment

For production deployment:

1. Use Gunicorn or similar WSGI server
2. Set up reverse proxy (nginx/Apache)
3. Configure SSL/TLS certificates
4. Set up monitoring and logging
5. Implement rate limiting
6. Configure proper CORS settings

See deployment guide for detailed instructions.

---

**Installation complete!** You can now start using GPS Verifier.

*Last Updated: October 18, 2025 - Version 3.0.0*
