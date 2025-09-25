#!/usr/bin/env python3
"""
GPS Verifier - Simple GPS Validation API
Clean and simple FastAPI application for GPS coordinate extraction and validation
"""

import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Import our simplified API routes
from routes.gps_api import router as gps_router

# Configure logging with clear, readable format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

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
    description="Simple API for extracting GPS coordinates from images and validating locations",
    version="2.0.0",
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

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "GPS Verifier API",
        "version": "2.0.0",
        "description": "Extract GPS coordinates from images and validate locations",
        "features": [
            "GPS extraction from image EXIF data",
            "OCR text extraction using Tesseract",
            "WhatsApp GPS overlay detection",
            "Location validation against administrative zones"
        ],
        "endpoints": {
            "validate_image": "POST /api/v1/validate-image-location",
            "validate_coords": "POST /api/v1/validate-coordinates", 
            "list_zones": "GET /api/v1/zones",
            "health_check": "GET /api/v1/health",
            "documentation": "GET /docs"
        }
    }

if __name__ == "__main__":
    # Run the application directly
    logger.info("🌟 Starting GPS Verifier API server...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )