// ========================================
// GPS Verifier - Frontend Application
// ========================================

// Configuration
const API_BASE_URL = 'http://127.0.0.1:8000';
const API_ENDPOINT = `${API_BASE_URL}/api/v1/validate-image-location`;

// DOM Elements
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const previewSection = document.getElementById('previewSection');
const imagePreview = document.getElementById('imagePreview');
const fileName = document.getElementById('fileName');
const fileSize = document.getElementById('fileSize');
const validateBtn = document.getElementById('validateBtn');
const clearBtn = document.getElementById('clearBtn');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');
const newValidationBtn = document.getElementById('newValidationBtn');
const retryBtn = document.getElementById('retryBtn');
const downloadBtn = document.getElementById('downloadBtn');

// State
let selectedFile = null;
let validationResults = null;

// ========================================
// Event Listeners
// ========================================

// Drop zone click
dropZone.addEventListener('click', () => {
    fileInput.click();
});

// File input change
fileInput.addEventListener('change', (e) => {
    handleFileSelect(e.target.files[0]);
});

// Drag and drop
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('drag-over');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('drag-over');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('drag-over');
    
    const file = e.dataTransfer.files[0];
    handleFileSelect(file);
});

// Button clicks
clearBtn.addEventListener('click', resetUI);
validateBtn.addEventListener('click', validateImage);
newValidationBtn.addEventListener('click', resetUI);
retryBtn.addEventListener('click', resetUI);
downloadBtn.addEventListener('click', downloadReport);

// ========================================
// File Handling
// ========================================

function handleFileSelect(file) {
    // Validate file
    if (!file) return;
    
    if (!file.type.startsWith('image/')) {
        showError('Invalid file type', 'Please select an image file (JPG, PNG, WEBP)');
        return;
    }
    
    if (file.size > 10 * 1024 * 1024) { // 10MB
        showError('File too large', 'Please select an image smaller than 10MB');
        return;
    }
    
    selectedFile = file;
    
    // Display preview
    const reader = new FileReader();
    reader.onload = (e) => {
        imagePreview.src = e.target.result;
        fileName.textContent = file.name;
        fileSize.textContent = formatFileSize(file.size);
        
        // Show preview section
        dropZone.style.display = 'none';
        previewSection.style.display = 'block';
        resultsSection.style.display = 'none';
        errorSection.style.display = 'none';
    };
    reader.readAsDataURL(file);
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

// ========================================
// Validation
// ========================================

async function validateImage() {
    if (!selectedFile) return;
    
    // Show loading state
    const btnText = validateBtn.querySelector('.btn-text');
    const btnLoader = validateBtn.querySelector('.btn-loader');
    btnText.style.display = 'none';
    btnLoader.style.display = 'block';
    validateBtn.disabled = true;
    
    try {
        // Create form data
        const formData = new FormData();
        formData.append('file', selectedFile);
        
        // Make API request
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.detail || 'Validation failed');
        }
        
        // Check if GPS coordinates were found
        if (data.error) {
            showError(
                data.error,
                'Please try another image',
                data.suggestions || []
            );
            return;
        }
        
        // Display results
        displayResults(data);
        
    } catch (error) {
        console.error('Validation error:', error);
        showError(
            'Connection Error',
            'Failed to connect to the validation server. Please ensure the backend is running.',
            ['Make sure the API server is running on http://127.0.0.1:8000', 'Check your internet connection', 'Try again in a few moments']
        );
    } finally {
        // Reset button state
        btnText.style.display = 'block';
        btnLoader.style.display = 'none';
        validateBtn.disabled = false;
    }
}

// ========================================
// Display Results
// ========================================

function displayResults(data) {
    validationResults = data;
    
    // Update status badge
    const statusBadge = document.getElementById('statusBadge');
    const status = data.validation.status;
    statusBadge.textContent = status.toUpperCase();
    statusBadge.className = `status-badge ${status}`;
    
    // Update GPS coordinates
    document.getElementById('latitude').textContent = data.extracted_gps.latitude.toFixed(6) + '° N';
    document.getElementById('longitude').textContent = data.extracted_gps.longitude.toFixed(6) + '° E';
    document.getElementById('source').textContent = formatSource(data.extracted_gps.source);
    document.getElementById('confidence').textContent = (data.extracted_gps.confidence * 100).toFixed(0) + '%';
    
    // Update zone information
    const zoneInfo = document.getElementById('zoneInfo');
    if (status === 'valid') {
        zoneInfo.style.display = 'block';
        document.getElementById('zoneName').textContent = data.validation.zone_name || 'N/A';
        document.getElementById('zoneType').textContent = formatZoneType(data.validation.zone_type) || 'N/A';
        document.getElementById('department').textContent = data.validation.department || 'N/A';
        document.getElementById('contact').textContent = data.validation.contact || 'N/A';
        document.getElementById('email').textContent = data.validation.email || 'N/A';
    } else {
        zoneInfo.style.display = 'none';
    }
    
    // Update map link
    const mapLink = document.getElementById('mapLink');
    const lat = data.extracted_gps.latitude;
    const lon = data.extracted_gps.longitude;
    mapLink.href = `https://www.google.com/maps?q=${lat},${lon}`;
    
    // Show results section
    previewSection.style.display = 'none';
    resultsSection.style.display = 'block';
    errorSection.style.display = 'none';
    
    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function formatSource(source) {
    const sourceMap = {
        'exif': 'EXIF Metadata',
        'ocr': 'OCR Text Extraction',
        'pattern_recognition': 'Pattern Recognition',
        'whatsapp_pattern': 'WhatsApp GPS Overlay'
    };
    return sourceMap[source] || source;
}

function formatZoneType(type) {
    return type.split('_').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
}

// ========================================
// Error Handling
// ========================================

function showError(title, message, suggestions = []) {
    document.getElementById('errorMessage').textContent = message;
    
    const suggestionsList = document.getElementById('errorSuggestions');
    suggestionsList.innerHTML = '';
    
    if (suggestions.length > 0) {
        suggestions.forEach(suggestion => {
            const li = document.createElement('li');
            li.textContent = suggestion;
            suggestionsList.appendChild(li);
        });
        suggestionsList.style.display = 'block';
    } else {
        suggestionsList.style.display = 'none';
    }
    
    // Show error section
    previewSection.style.display = 'none';
    resultsSection.style.display = 'none';
    errorSection.style.display = 'block';
    
    // Scroll to error
    errorSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ========================================
// UI Reset
// ========================================

function resetUI() {
    selectedFile = null;
    validationResults = null;
    fileInput.value = '';
    
    dropZone.style.display = 'block';
    previewSection.style.display = 'none';
    resultsSection.style.display = 'none';
    errorSection.style.display = 'none';
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ========================================
// Download Report
// ========================================

function downloadReport() {
    if (!validationResults) return;
    
    const report = {
        filename: selectedFile.name,
        timestamp: new Date().toISOString(),
        gps_coordinates: validationResults.extracted_gps,
        validation: validationResults.validation
    };
    
    const blob = new Blob([JSON.stringify(report, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `gps-validation-report-${Date.now()}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// ========================================
// Smooth Scroll for Navigation
// ========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ========================================
// Initialize
// ========================================

console.log('GPS Verifier UI initialized');
console.log('API Endpoint:', API_ENDPOINT);
