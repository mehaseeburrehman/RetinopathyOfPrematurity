import numpy as np
from PIL import Image
import torch
import torch.nn as nn
from torchvision import models, transforms
import os

class ROPNet(nn.Module):
    def __init__(self, num_classes=4):
        super().__init__()
        vgg = models.vgg16(pretrained=False)
        self.encoder = vgg.features
        self.decoder = nn.Sequential(
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(512, 512, 3, padding=1), nn.BatchNorm2d(512), nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, 3, padding=1), nn.BatchNorm2d(512), nn.ReLU(inplace=True),
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(512, 512, 3, padding=1), nn.BatchNorm2d(512), nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, 3, padding=1), nn.BatchNorm2d(512), nn.ReLU(inplace=True),
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(512, 256, 3, padding=1), nn.BatchNorm2d(256), nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, 3, padding=1), nn.BatchNorm2d(256), nn.ReLU(inplace=True),
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(256, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(inplace=True),
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(128, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(inplace=True)
        )
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(64, 256), nn.ReLU(inplace=True), nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return self.classifier(x)

class ModelHandler:
    def __init__(self, model_path="Vgg16+Segnet_model.pth"):
        self.model_path = model_path
        self.model = None
        # Exact same classes as your dataset prediction code
        self.classes = ['Healthy', 'RD', 'Type 1', 'Type 2']
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Exact same transform as your dataset prediction code
        self.transform = transforms.Compose([
            transforms.Resize((244, 244)),
            transforms.ToTensor(),
            transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        ])
    
    def load_model(self):
        """Load the PyTorch VGG16+SegNet model - exact same as your code"""
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        
        try:
            print(f"📂 Loading model from {self.model_path}...")
            
            # Initialize model architecture - exact same as your code
            self.model = ROPNet(num_classes=len(self.classes)).to(self.device)
            
            # Load model weights - exact same as your code
            self.model.load_state_dict(torch.load(self.model_path, map_location=self.device))
            self.model.eval()
            
            print(f"✅ Model loaded successfully!")
            print(f"🔧 Using device: {self.device}")
            print(f"📊 Model classes: {self.classes}")
            
        except Exception as e:
            raise RuntimeError(f"Error loading model: {e}")
    
    def preprocess_image(self, image):
        """Preprocess image - exact same transform as your dataset code"""
        try:
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Apply exact same transform as your dataset prediction
            img_tensor = self.transform(image).unsqueeze(0).to(self.device)  # Add batch dimension
            
            return img_tensor
            
        except Exception as e:
            raise RuntimeError(f"Error preprocessing image: {e}")
    
    def predict(self, image, return_all_probs=False):
        """Make prediction - exact same logic as your dataset prediction code"""
        if self.model is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        
        # Preprocess image
        img_tensor = self.preprocess_image(image)
        
        # Make prediction - exact same as your code
        with torch.no_grad():
            outputs = self.model(img_tensor)
            
            if return_all_probs:
                # Return all class probabilities
                probabilities = torch.softmax(outputs, dim=1)[0]  # Get probabilities for single image
                probs_dict = {}
                for i, class_name in enumerate(self.classes):
                    probs_dict[class_name] = float(probabilities[i].cpu().numpy())
                return probs_dict
            else:
                # Return predicted class and confidence - same as your code
                preds = outputs.argmax(dim=1)  # Same as your dataset code
                predicted_class_idx = preds.item()
                predicted_class = self.classes[predicted_class_idx]
                
                # Get confidence (probability of predicted class)
                probabilities = torch.softmax(outputs, dim=1)[0]
                confidence = float(probabilities[predicted_class_idx].cpu().numpy())
                
                return predicted_class, confidence
    
    def get_model_info(self):
        """Get model information"""
        if self.model is None:
            return "Model not loaded"
        
        # Count parameters
        total_params = sum(p.numel() for p in self.model.parameters())
        trainable_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        
        info = {
            "model_type": "VGG16+SegNet",
            "device": str(self.device),
            "input_size": "244x244",
            "total_params": total_params,
            "trainable_params": trainable_params,
            "classes": self.classes,
            "transform": "Resize(244,244) + Normalize(0.5,0.5,0.5)"
        }
        
        return info
