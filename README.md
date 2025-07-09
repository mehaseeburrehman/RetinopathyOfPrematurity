# 🔬 Retinopathy of Prematurity (ROP) Classification System

A web-based AI application for classifying eye images to detect Retinopathy of Prematurity using a VGG16+SegNet deep learning model.

## 🏥 Medical Classifications

The system classifies retinal images into 4 categories:  
- **Healthy**: Normal retina condition  
- **RD**: Retinal Detachment  
- **Type 1**: Mild Retinopathy of Prematurity  
- **Type 2**: Severe Retinopathy of Prematurity  

## 🌟 Features

- **🤖 AI-Powered Classification**: VGG16+SegNet model for ROP detection  
- **🔐 User Authentication**: Secure login/signup system  
- **📊 Prediction History**: Track and download prediction history as CSV  
- **🖼️ Sample Images**: Pre-loaded sample images for testing  
- **🎨 Modern UI**: Clean Gradio web interface  

## 📁 Project Structure

```plaintext
RetinopathyOfPrematurity/
├── app.py                    # Main application file
├── auth.py                   # User authentication system
├── database.py               # Database operations
├── model_handler.py          # ML model loading and prediction
├── requirements.txt          # Python dependencies
├── ui_components/            # UI modules
│   ├── __init__.py
│   ├── login_ui.py
│   ├── prediction_ui.py
│   ├── history_ui.py
│   └── about_ui.py
├── sample/                   # Sample images folder (create manually)
└── models/                   # Model files folder (create manually)
```

## 🚀 Installation & Setup (Windows)

### Prerequisites
- **Windows 10/11**  
- **Python 3.8 or higher** — [Download from python.org](https://www.python.org/downloads/)  
- **VS Code** — [Download from code.visualstudio.com](https://code.visualstudio.com/)
- **MODEL** — https://drive.google.com/file/d/12nBZuHOqeJZm_ykhC4nSzYr5wHgPV2x_/view?usp=sharing
- **Dataset** — https://drive.google.com/file/d/1Bn37j9GG7JW9RoVzMQd_aex_dvAf2lHR/view?usp=sharing

### Step 1: Clone the Repository

Open **Command Prompt** or **PowerShell** and run:

```cmd
git clone https://github.com/mehaseeburrehman/RetinopathyOfPrematurity.git
cd RetinopathyOfPrematurity
```

### Step 2: Open in VS Code
### Step 3: Create Virtual Environment

In VS Code terminal (Terminal → New Terminal):

```
python -m venv rop_env
```

### Step 4: Activate Virtual Environment

```
rop_env\Scripts\activate
```

You should see `(rop_env)` at the beginning of your command prompt.

### Step 5: Install Dependencies

```
pip install -r requirements.txt
```

### Step 6: Create Required Folders

```cmd
mkdir models
mkdir sample
```

### Step 7: Download Model File

1. Download your trained model file `vgg16_Segnet.pth`  
2. Place it in the `models/` folder  
3. The path should be: `models/vgg16_Segnet.pth`  

## 🏃‍♂️ Running the Application

### Method 1: Run from VS Code

1. Make sure virtual environment is activated: `(rop_env)` should be visible  
2. In VS Code terminal, run:

```
python app.py
```

### Method 2: Run from Command Prompt

1. Navigate to project folder:

```
cd path\to\ROP-Classification-System
```

2. Activate virtual environment:

```
rop_env\Scripts\activate
```

3. Run the application:

```
python app.py
```

### Expected Output

You should see:

```
🚀 Starting Retinopathy of Prematurity App...
📊 Initializing database...
✅ Database initialized successfully
🤖 Loading ML model...
✅ Model loaded successfully!
✅ App ready!
Running on local URL: http://127.0.0.1:7860
```

### Access the Application

Open your web browser and go to: **http://localhost:7860**

## 📖 How to Use

### 1. Create Account

- Click **"Register"** tab  
- Enter username and password (minimum 6 characters)  
- Click **"Register"**

### 2. Login

- Enter your credentials  
- Click **"Login"**

### 3. Make Predictions

- **Upload Image:** Click "Upload Eye Image" and select a retinal image  
- **Use Samples:** Click any sample image to load it  
- **Analyze:** Click "Analyze Image" button  
- **View Results:** See confidence percentages for each class  

### 4. View History

- Go to **"Prediction History"** tab  
- Click **"Load History"** to see past predictions  
- Click **"Download CSV"** to export your data  

## 🔧 Troubleshooting

### Common Issues

**1. Python not found**

```
'python' is not recognized as an internal or external command
```

**Solution:** Install Python from python.org and make sure "Add to PATH" is checked during installation.

**2. Virtual environment activation fails**

```
cannot be loaded because running scripts is disabled on this system
```

**Solution:** Run PowerShell as Administrator and execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
