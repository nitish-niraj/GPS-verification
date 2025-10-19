#!/usr/bin/env python3
"""
GPS Verifier - Simple GPS Validation API
Clean and simple FastAPI application for GPS coordinate extraction and validation
"""

import logging
import uvicorn
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager

# Configure logging FIRST before importing routes
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG to see OCR extracted text
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import our simplified API routes (after logging is configured)
from routes.gps_api import router as gps_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown manager"""
    # Startup
    logger.info("🚀 Starting GPS Verifier API...")
    logger.info("✅ API ready to process GPS validation requests")
    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down GPS Verifier API...")

# Create FastAPI application with clean configuration
app = FastAPI(
    title="GPS Verifier API",
    description="GPS validation system for Lovely Professional University - Extract coordinates from images and validate against campus boundaries",
    version="3.0.0",
    lifespan=lifespan
)

# Enable CORS for web applications
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include our GPS validation routes
app.include_router(gps_router)

# Serve frontend static files
frontend_path = Path(__file__).parent.parent / "frontend"
if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")
    
    @app.get("/ui")
    async def serve_ui():
        """Serve the frontend UI"""
        return FileResponse(str(frontend_path / "index.html"))

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "GPS Verifier API",
        "version": "3.0.0",
        "description": "GPS validation system for Lovely Professional University",
        "ui": "http://localhost:8000/ui",
        "features": [
            "GPS extraction from image EXIF data",
            "OCR text extraction using Tesseract",
            "WhatsApp GPS overlay detection",
            "Location validation against administrative zones"
        ],
        "endpoints": {
            "web_ui": "GET /ui",
            "validate_image": "POST /api/v1/validate-image-location",
            "validate_coords": "POST /api/v1/validate-coordinates", 
            "list_zones": "GET /api/v1/zones",
            "health_check": "GET /api/v1/health",
            "documentation": "GET /docs"
        }
    }

if __name__ == "__main__":
    # Run the application directly
    import os
    
    # Use environment variable PORT or default to 7860 (Hugging Face Spaces)
    # Falls back to 8000 for local development
    port = int(os.getenv("PORT", os.getenv("SPACE_ID", "8000") and 7860 or 8000))
    
    logger.info(f"🌟 Starting GPS Verifier API server on port {port}...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=False,  # Disable reload in production
        log_level="info"
    )