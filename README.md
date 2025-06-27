# 🔬 Retinopathy of Prematurity (ROP) Classification System

A comprehensive web application for classifying eye images to detect Retinopathy of Prematurity using VGG16+SegNet deep learning model with user authentication and prediction history.

## 🌟 Features

- **🤖 AI-Powered Classification**: VGG16+SegNet model for accurate ROP detection
- **🔐 User Authentication**: Secure login/signup with password hashing
- **📊 Prediction History**: Track and download your prediction history
- **🖼️ Sample Images**: Pre-loaded sample images for quick testing
- **💾 Data Export**: Download prediction history as CSV
- **🎨 Modern UI**: Clean, responsive Gradio interface

## 🏥 Medical Classifications

The system classifies eye images into 4 categories:
- **Healthy**: Normal retina condition
- **RD**: Retinal Detachment
- **Type 1**: Mild Retinopathy of Prematurity
- **Type 2**: Severe Retinopathy of Prematurity

## 📁 Project Structure

\`\`\`
ROP-Classification-System/
├── app.py                    # Main application entry point
├── auth.py                   # User authentication system
├── database.py               # Database operations (SQLite)
├── model_handler.py          # ML model loading and prediction
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation
├── setup.py                  # Installation script
├── ui_components/            # UI modules
│   ├── __init__.py
│   ├── login_ui.py          # Login/Register interface
│   ├── prediction_ui.py     # Prediction interface
│   ├── history_ui.py        # History management
│   └── about_ui.py          # About page
├── sample/                   # Sample images (create this folder)
│   ├── healthy.jpg          # Healthy retina sample
│   ├── type1.jpg            # Type 1 ROP sample
│   ├── type2.jpg            # Type 2 ROP sample
│   └── rd.jpg               # Retinal Detachment sample
├── models/                   # Model files (create this folder)
│   └── vgg16_Segnet.pth     # Your trained model (download separately)
└── docs/                     # Documentation
    ├── installation.md
    ├── usage.md
    └── model_info.md
\`\`\`

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- higher then i5 2nd gen
- 4GB+ RAM
- Internet connection for initial setup

### 1. Clone Repository

\`\`\`
https://github.com/mehaseeburrehman/RetinopathyOfPrematurity.git
\`\`\`

### 2. Download Required Files

#### Download Trained Model
\`\`\`
# Create models directory
mkdir models

 # manually download model from:

https://drive.google.com/file/d/12nBZuHOqeJZm_ykhC4nSzYr5wHgPV2x_/view?usp=sharing

# Download  images from the dataset or use your own

https://drive.google.com/file/d/1Bn37j9GG7JW9RoVzMQd_aex_dvAf2lHR/view?usp=sharing

# Place 4 sample images: healthy.jpg, type1.jpg, type2.jpg, rd.jpg
\`\`\`

### 3. Install Dependencies

#### Option A: Using pip
\`\`\`
pip install -r requirements.txt
\`\`\`

#### Option B: Using setup script
\`\`\`
python setup.py install
\`\`\`

### 4. Run the Application

\`\`\`
python app.py
\`\`\`

The application will start and display:
\`\`\`
🚀 Starting Retinopathy of prematurity App...
📊 Initializing database...
✅ Database initialized successfully
🤖 Loading ML model...
✅ Model loaded successfully!
✅ App ready!
Running on local URL: http://127.0.0.1:7860
\`\`\`

### 5. Access the Application

Open your web browser and navigate to:
- **Local**: http://localhost:7860
- **Network**: Use the public URL if share=True

## 📖 Detailed Installation Guide

### System Requirements

#### Minimum Requirements:
- **OS**: Windows 10, macOS 10.14, or Ubuntu 18.04+
- **Python**: 3.8+
- **RAM**: 4GB
- **Storage**: 2GB free space
- **GPU**: Optional (CPU inference supported)

#### Recommended Requirements:
- **RAM**: 8GB+
- **GPU**: NVIDIA GPU with 4GB+ VRAM
- **Storage**: 5GB+ free space

### Step-by-Step Installation

#### 1. Environment Setup

**Windows:**
\`\`\`cmd
# Install Python from python.org
# Open Command Prompt as Administrator

# Clone repository
git clone https://github.com/yourusername/ROP-Classification-System.git
cd ROP-Classification-System

# Create a virtual environment
python -m venv rop_env
rop_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
\`\`\`

# Clone repository
https://github.com/mehaseeburrehman/RetinopathyOfPrematurity.git
cd ROP-Classification-System

# Create a virtual environment
python3 -m venv rop_env
source rop_env/bin/activate

# Install dependencies
pip install -r requirements.txt
\`\`\`

# Add your sample images with these exact names:
 - healthy.jpg (normal retina)
 - type1.jpg (mild ROP)
 - type2.jpg (severe ROP) 
 - rd.jpg (retinal detachment)
\`\`\`

#### 4. Configuration (Optional)

Create `config.py` for custom settings:
```python
# config.py
MODEL_PATH = "models/vgg16_Segnet.pth"
SAMPLE_DIR = "sample/"
DATABASE_PATH = "predictions.db"
USERS_DB_PATH = "users.db"
HOST = "127.0.0.1"
PORT = 7860
