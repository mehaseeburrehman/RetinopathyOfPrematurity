# 🔬 ROP Image Classification Web App

A complete machine learning web application for classifying ROP images with user authentication, prediction history, and easy deployment capabilities.

## 🌟 Features

- **🔐 User Authentication**: Secure login/signup with password hashing
- **🤖 AI Prediction**: Classify ROP images into 4 categories:
  - Healthy
  - Retinal Detachment  
  - Type 1 (Diabetic Retinopathy - Mild/Moderate)
  - Type 2 (Diabetic Retinopathy - Severe/Proliferative)
- **📊 Prediction History**: View and download your prediction history
- **💾 Data Export**: Download history as CSV
- **🎨 Modern UI**: Clean, responsive interface with Gradio
- **🗄️ SQLite Database**: Lightweight, file-based storage

## 🚀 Quick Start

### Local Installation

1. **Clone or download the project files**

2. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Add your Keras model:**
   - Place your trained `.h5` model file in the project directory
   - Rename it to `ROP_classification_model.h5`
   - Or update the model path in `model_handler.py`

4. **Run the application:**
   \`\`\`bash
   python app.py
   \`\`\`

5. **Open your browser:**
   - Go to `http://localhost:7860`
   - Create an account and start classifying!

### 🌐 Deploy on Hugging Face Spaces

1. **Create a new Space on [Hugging Face](https://huggingface.co/spaces)**
   - Choose "Gradio" as the SDK
   - Set visibility to "Public" or "Private"

2. **Upload files:**
   - Upload all Python files (`app.py`, `auth.py`, `database.py`, `model_handler.py`)
   - Upload `requirements.txt`
   - Upload your trained model file (`ROP_classification_model.h5`)

3. **Your app will automatically deploy!**
   - HF Spaces will install dependencies and start the app
   - Access via your Space URL

### 🔄 Deploy on Replit

1. **Create a new Repl**
   - Choose "Python" template

2. **Upload project files**
   - Upload all Python files and requirements.txt
   - Upload your model file

3. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run:**
   \`\`\`bash
   python app.py
   \`\`\`

## 📁 Project Structure

\`\`\`
ROP-classification-app/
├── app.py                 # Main Gradio application
├── auth.py               # User authentication logic
├── database.py           # Database operations
├── model_handler.py      # ML model loading and prediction
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── ROP_classification_model.h5  # Your trained model (add this)
├── users.db             # SQLite database (created automatically)
└── predictions.db       # Predictions database (created automatically)
\`\`\`

## 🔧 Configuration

### Model Configuration
Edit `model_handler.py` to customize:
- Model file path
- Input image size
- Class names
- Preprocessing steps

### Database Configuration
Edit `database.py` and `auth.py` to customize:
- Database file paths
- Table schemas
- Data retention policies

### UI Configuration
Edit `app.py` to customize:
- Interface layout
- Styling (CSS)
- Tab organization
- Messages and text

## 🧪 Testing

### Demo Credentials
The app creates accounts dynamically. For testing:

1. **Register a new account:**
   - Username: `demo_user`
   - Password: `demo123`

2. **Test the prediction:**
   - Upload any ROP image
   - View the prediction result
   - Check prediction history

### Model Testing
If you don't have a trained model yet:
- The app includes a dummy model for demonstration
- It will make random predictions for testing purposes
- Replace with your actual trained model for real predictions

## 🔒 Security Features

- **Password Hashing**: Uses bcrypt for secure password storage
- **SQL Injection Protection**: Parameterized queries
- **Input Validation**: Image format and size validation
- **Session Management**: Secure user session handling

## 📊 Database Schema

### Users Table
\`\`\`sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
\`\`\`

### Predictions Table
\`\`\`sql
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    image_data TEXT NOT NULL,
    prediction TEXT NOT NULL,
    confidence REAL NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
\`\`\`

## 🚨 Important Notes

- **Medical Disclaimer**: This tool is for educational/research purposes only
- **Always consult healthcare professionals** for medical diagnosis
- **Data Privacy**: User data is stored locally in SQLite databases
- **Model Performance**: Accuracy depends on your trained model quality

## 🛠️ Troubleshooting

### Common Issues

1. **Model not loading:**
   - Check if `ROP_classification_model.h5` exists
   - Verify model file is not corrupted
   - Check TensorFlow version compatibility

2. **Database errors:**
   - Ensure write permissions in project directory
   - Check if SQLite is properly installed

3. **Gradio not starting:**
   - Check if port 7860 is available
   - Try different port: `app.launch(server_port=7861)`

4. **Dependencies issues:**
   - Update pip: `pip install --upgrade pip`
   - Install in virtual environment
   - Check Python version (3.8+ recommended)

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed correctly
3. Ensure your model file is compatible with TensorFlow/Keras
4. Test with the dummy model first

## 📈 Future Enhancements

Potential improvements:
- [ ] Add image preprocessing options
- [ ] Implement batch prediction
- [ ] Add prediction confidence visualization
- [ ] Include model performance metrics
- [ ] Add data export in multiple formats
- [ ] Implement user roles and permissions
- [ ] Add prediction analytics dashboard

## 📄 License

This project is open source. Please ensure compliance with your model's licensing terms.

---

**Ready to classify ROP images with AI! 🚀**
\`\`\`

Let's also create a simple deployment script:

```python file="deploy.py"
#!/usr/bin/env python3
"""
Deployment helper script for ROP Image Classification App
"""

import os
import sys
import subprocess
import shutil

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'auth.py', 
        'database.py',
        'model_handler.py',
        'requirements.txt'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found")
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def check_model():
    """Check if model file exists"""
    model_files = ['ROP_classification_model.h5', 'model.h5', 'ROP_model.h5']
    
    for model_file in model_files:
        if os.path.exists(model_file):
            print(f"✅ Found model file: {model_file}")
            return True
    
    print("⚠️  No model file found. App will use dummy model for demonstration.")
    print("   Add your trained model file (ROP_classification_model.h5) to enable real predictions.")
    return False

def run_app():
    """Run the application"""
    print("🚀 Starting ROP Image Classification App...")
    try:
        subprocess.run([sys.executable, 'app.py'])
    except KeyboardInterrupt:
        print("\n👋 App stopped by user")
    except Exception as e:
        print(f"❌ Error running app: {e}")

def main():
    """Main deployment function"""
    print("🔬 ROP Image Classification App - Deployment Helper")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check model
    check_model()
    
    # Run app
    print("\n" + "=" * 50)
    run_app()

if __name__ == "__main__":
    main()
