# 🚀 Hugging Face Deployment Guide

## Quick Deployment Steps

### 1. Create Hugging Face Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Fill in:
   - **Space name**: `gps-verifier-lpu`
   - **License**: MIT
   - **SDK**: Docker
   - **Space hardware**: CPU basic (free)
3. Click **Create Space**

### 2. Clone Your Space

```powershell
# Clone the empty space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/gps-verifier-lpu
cd gps-verifier-lpu
```

### 3. Copy Project Files

```powershell
# Copy from your GPS Verifier project
Copy-Item -Recurse E:\gps verifier\backend .
Copy-Item -Recurse "E:\gps verifier\frontend" .
Copy-Item "E:\gps verifier\Dockerfile" .
Copy-Item "E:\gps verifier\.dockerignore" .
Copy-Item "E:\gps verifier\.gitattributes" .
Copy-Item "E:\gps verifier\README_HF.md" README.md
```

### 4. Initialize Git LFS (if needed)

```powershell
git lfs install
```

### 5. Commit and Push

```powershell
# Add all files
git add .

# Commit
git commit -m "Deploy GPS Verifier v3.0.0 to Hugging Face Spaces"

# Push to Hugging Face
git push
```

### 6. Monitor Build

1. Go to your Space: `https://huggingface.co/spaces/YOUR_USERNAME/gps-verifier-lpu`
2. Click **"Build"** tab
3. Wait for Docker build (5-10 minutes first time)
4. Check for errors in logs

### 7. Test Your Deployment

Once deployed, test:

**Web UI**: `https://YOUR_USERNAME-gps-verifier-lpu.hf.space/ui`

**API Health**:
```bash
curl https://YOUR_USERNAME-gps-verifier-lpu.hf.space/api/v1/health
```

**API Docs**: `https://YOUR_USERNAME-gps-verifier-lpu.hf.space/docs`

---

## Alternative: Using Hugging Face CLI

### Install Hugging Face CLI

```powershell
pip install huggingface-hub
```

### Login

```powershell
huggingface-cli login
```

### Create and Push

```powershell
# Create space
huggingface-cli repo create gps-verifier-lpu --type space --space-sdk docker

# Clone and add files
git clone https://huggingface.co/spaces/YOUR_USERNAME/gps-verifier-lpu
cd gps-verifier-lpu

# Copy files (same as above)
# Then commit and push
```

---

## Troubleshooting

### Build Fails

**Check**: Dockerfile syntax and dependencies
**Fix**: Review build logs in Space's Build tab

### Port Issues

**Check**: App should use port 7860
**Fix**: Verify Dockerfile `EXPOSE 7860` and main.py port config

### OCR Not Working

**Check**: Tesseract installation in Dockerfile
**Fix**: Ensure `tesseract-ocr` is in apt-get install

### Static Files 404

**Check**: Frontend files copied correctly
**Fix**: Verify path in main.py: `Path(__file__).parent.parent / "frontend"`

---

## Files Prepared for Deployment

✅ `Dockerfile` - Docker configuration for Hugging Face
✅ `README_HF.md` - Hugging Face Space README with metadata
✅ `.dockerignore` - Files to exclude from Docker build
✅ `.gitattributes` - Git LFS configuration
✅ `backend/main.py` - Updated for flexible port (7860/8000)
✅ `backend/requirements.txt` - Updated to opencv-python-headless

---

## Next Steps

1. Create your Hugging Face account (if not already)
2. Create a new Space with Docker SDK
3. Follow the deployment steps above
4. Test your deployed application
5. Share your Space URL!

---

**Your Space will be live at**:
`https://YOUR_USERNAME-gps-verifier-lpu.hf.space`

Good luck! 🚀
