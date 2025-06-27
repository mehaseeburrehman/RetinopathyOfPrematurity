# 📦 Detailed Installation Guide

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10, macOS 10.14, Ubuntu 18.04+
- **Python**: 3.8 or higher
- **RAM**: 4GB
- **Storage**: 2GB free space
- **Internet**: Required for initial setup

### Recommended Requirements
- **RAM**: 8GB or higher
- **GPU**: NVIDIA GPU with 4GB+ VRAM (for faster inference)
- **Storage**: 5GB+ free space

## Installation Methods

### Method 1: Automated Setup (Recommended)

\`\`\`bash
# Clone repository
git clone https://github.com/yourusername/ROP-Classification-System.git
cd ROP-Classification-System

# Run automated setup
python setup.py
\`\`\`

### Method 2: Manual Installation

#### Step 1: Environment Setup
\`\`\`bash
# Create virtual environment
python -m venv rop_env

# Activate environment
# Windows:
rop_env\Scripts\activate
# macOS/Linux:
source rop_env/bin/activate
\`\`\`

#### Step 2: Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

#### Step 3: Download Model
\`\`\`bash
# Create models directory
mkdir models

# Download model (replace with actual URL)
wget -O models/vgg16_Segnet.pth "YOUR_MODEL_URL"
\`\`\`

#### Step 4: Setup Sample Images
\`\`\`bash
# Create sample directory
mkdir sample

# Add sample images:
# - healthy.jpg
# - type1.jpg  
# - type2.jpg
# - rd.jpg
\`\`\`

## Platform-Specific Instructions

### Windows

\`\`\`cmd
# Install Git for Windows
# Download from: https://git-scm.com/download/win

# Install Python
# Download from: https://python.org/downloads/

# Open Command Prompt as Administrator
git clone https://github.com/yourusername/ROP-Classification-System.git
cd ROP-Classification-System
python setup.py
\`\`\`

### macOS

\`\`\`bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and Git
brew install python git

# Clone and setup
git clone https://github.com/yourusername/ROP-Classification-System.git
cd ROP-Classification-System
python3 setup.py
\`\`\`

### Ubuntu/Linux

\`\`\`bash
# Update system
sudo apt update
sudo apt install python3 python3-pip python3-venv git

# Clone and setup
git clone https://github.com/yourusername/ROP-Classification-System.git
cd ROP-Classification-System
python3 setup.py
\`\`\`

## GPU Setup (Optional)

### NVIDIA GPU Setup

\`\`\`bash
# Check NVIDIA driver
nvidia-smi

# Install CUDA-enabled PyTorch
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Verify CUDA
python -c "import torch; print(torch.cuda.is_available())"
\`\`\`

## Troubleshooting Installation

### Common Issues

1. **Python Version Error**
   \`\`\`bash
   # Check Python version
   python --version
   # Should be 3.8+
   \`\`\`

2. **Permission Denied**
   \`\`\`bash
   # Windows: Run as Administrator
   # macOS/Linux: Use sudo for system-wide installation
   sudo python3 setup.py
   \`\`\`

3. **Network Issues**
   \`\`\`bash
   # Use proxy if behind firewall
   pip install --proxy http://proxy.server:port -r requirements.txt
   \`\`\`

4. **Space Issues**
   \`\`\`bash
   # Check available space
   df -h  # Linux/macOS
   dir    # Windows
