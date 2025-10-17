# GPS Verifier - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Start the Server
```bash
cd backend
python main.py
```

You should see:
```
✅ API ready to process GPS validation requests
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Open the Web Interface
Open your browser and go to:
```
http://localhost:8000/ui
```

### Step 3: Upload and Validate
1. Drag & drop an image with GPS data (or click to browse)
2. Click "Validate Location"
3. View your results!

---

## 📱 Supported Image Types

✅ **WhatsApp GPS Screenshots** - Automatically detected  
✅ **Photos with EXIF GPS** - From cameras and phones  
✅ **Images with visible GPS text** - Extracted via OCR  

---

## 🧪 Quick API Test

Test the API with curl:
```bash
curl -X POST "http://localhost:8000/api/v1/validate-image-location" \
  -F "file=@your-image.jpg"
```

---

## 🔗 Important Links

- **Web UI**: http://localhost:8000/ui
- **API Docs**: http://localhost:8000/docs  
- **Health Check**: http://localhost:8000/api/v1/health

---

## ❓ Troubleshooting

**Server won't start?**
- Make sure port 8000 is available
- Check if all dependencies are installed: `pip install -r requirements.txt`

**No GPS coordinates found?**
- Ensure image contains GPS data
- Try a WhatsApp location sharing screenshot
- Check if image is not corrupted

**Validation shows "invalid"?**
- Coordinates might be outside defined zones
- Add custom zones in `backend/data/ward_boundaries.json`

---

## 📚 Need More Help?

Check the full [README.md](README.md) for detailed documentation.
