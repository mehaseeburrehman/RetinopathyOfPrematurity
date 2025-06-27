# 🤖 Model Information

## Architecture Overview

### VGG16 + SegNet Architecture

The ROP Classification System uses a hybrid architecture combining:

1. **VGG16 Encoder**: Feature extraction from retinal images
2. **SegNet Decoder**: Upsampling and feature refinement  
3. **Classification Head**: Final classification into 4 classes

### Model Specifications

- **Input Size**: 244 × 244 × 3 (RGB images)
- **Output Classes**: 4 (Healthy, RD, Type 1, Type 2)
- **Parameters**: ~15M trainable parameters
- **Model Size**: ~100MB (.pth file)
- **Framework**: PyTorch

### Architecture Details

```python
ROPNet(
  (encoder): VGG16 Features (512 channels)
  (decoder): Sequential(
    Upsample layers with Conv2d + BatchNorm + ReLU
    Final output: 64 channels
  )
  (classifier): Sequential(
    AdaptiveAvgPool2d(1, 1)
    Flatten()
    Linear(64 → 256) + ReLU + Dropout(0.5)
    Linear(256 → 4)
  )
)
