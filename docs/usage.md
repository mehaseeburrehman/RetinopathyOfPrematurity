# 📖 Usage Guide

## Getting Started

### 1. Starting the Application

\`\`\`bash
# Navigate to project directory
cd ROP-Classification-System

# Activate virtual environment (if using)
source rop_env/bin/activate  # macOS/Linux
# or
rop_env\Scripts\activate     # Windows

# Start the application
python app.py
\`\`\`

### 2. Accessing the Interface

Open your web browser and go to:
- **Local Access**: http://localhost:7860
- **Network Access**: Use the public URL shown in terminal

## User Authentication

### Creating an Account

1. Click the **"Register"** tab
2. Enter a unique username
3. Create a password (minimum 6 characters)
4. Confirm your password
5. Click **"Register"**

### Logging In

1. Enter your username and password
2. Click **"Login"**
3. You'll be redirected to the main interface

## Making Predictions

### Method 1: Upload Your Own Image

1. **Click "Upload Eye Image"**
2. **Select an image file** (JPG, PNG, JPEG)
   - Recommended size: 244x244 pixels or larger
   - File size: Under 10MB
3. **Click "Analyze Image"**
4. **View results** with confidence percentages

### Method 2: Use Sample Images

1. **Click any sample image** below the upload area
   - Healthy: Normal retina
   - Type 1: Mild ROP
   - Type 2: Severe ROP  
   - RD: Retinal Detachment
2. **Image loads automatically** into upload area
3. **Click "Analyze Image"**
4. **View results**

## Understanding Results

### Prediction Output

The system shows confidence percentages for all 4 classes:

\`\`\`
Healthy: 85.2%
Type 1: 8.1%
Type 2: 4.3%
RD: 2.4%
\`\`\`

### Interpretation

- **Highest percentage** = Most likely diagnosis
- **Confidence > 70%** = High confidence
- **Confidence 50-70%** = Moderate confidence  
- **Confidence < 50%** = Low confidence, consider retesting

## Managing Prediction History

### Viewing History

1. Go to **"Prediction History"** tab
2. Click **"Load History"**
3. View your past predictions with timestamps

### Downloading History

1. In the **"Prediction History"** tab
2. Click **"Download CSV"**
3. Save the file to your computer
4. Open with Excel, Google Sheets, etc.

### CSV Format

The downloaded file contains:
- **ID**: Unique prediction identifier
- **Prediction**: Classification result
- **Confidence**: Confidence score (0-1)
- **Timestamp**: Date and time of prediction

## Best Practices

### Image Quality Guidelines

1. **Resolution**: Minimum 244x244 pixels
2. **Format**: JPG, PNG, or JPEG
3. **Quality**: Clear, well-lit images
4. **Focus**: Retina should be clearly visible
5. **Angle**: Frontal view preferred

### For Accurate Results

1. **Use high-quality images**
2. **Ensure proper lighting**
3. **Avoid blurry or distorted images**
4. **Test with multiple images** if uncertain
5. **Consider professional medical evaluation**

## Keyboard Shortcuts

- **Ctrl+U**: Upload new image
- **Enter**: Analyze current image
- **Ctrl+H**: View history
- **Ctrl+D**: Download history
- **Ctrl+L**: Logout

## Mobile Usage

The interface is responsive and works on mobile devices:

1. **Touch to upload** images
2. **Tap sample images** to select
3. **Swipe** to navigate between tabs
4. **Pinch to zoom** on results

## Troubleshooting Usage

### Image Upload Issues

**Problem**: Image won't upload
**Solutions**:
- Check file format (JPG, PNG, JPEG only)
- Reduce file size (under 10MB)
- Try a different browser
- Clear browser cache

### Prediction Errors

**Problem**: "Error processing image"
**Solutions**:
- Ensure image is not corrupted
- Try a different image format
- Check internet connection
- Restart the application

### Login Issues

**Problem**: Can't login
**Solutions**:
- Check username/password spelling
- Ensure account was created successfully
- Try registering again with different username
- Clear browser cookies

### Slow Performance

**Problem**: App is slow
**Solutions**:
- Close other browser tabs
- Restart the application
- Check system resources
- Use smaller image files

## Advanced Features

### Batch Processing (Future Feature)

Upload multiple images at once for batch analysis.

### Model Comparison (Future Feature)

Compare results from different model versions.

### Export Options (Future Feature)

Export results in PDF format with detailed reports.
