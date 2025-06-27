import gradio as gr
import base64
from io import BytesIO
import os
from PIL import Image

class PredictionUI:
    def __init__(self, model_handler, db_manager):
        self.model_handler = model_handler
        self.db_manager = db_manager
        
        # Sample images with correct paths
        self.sample_images = [
            {
                "name": "Healthy",
                "path": "sample/healthy.jpg",
                "description": "Normal retina"
            },
            {
                "name": "Type 1",
                "path": "sample/type1.jpg",
                "description": "Mild ROP"
            },
            {
                "name": "Type 2", 
                "path": "sample/type2.jpg",
                "description": "Severe ROP"
            },
            {
                "name": "RD",
                "path": "sample/rd.jpg", 
                "description": "Retinal Detachment"
            }
        ]
    
    def predict_image(self, image, current_user):
        """Handle image prediction"""
        if not current_user["logged_in"]:
            return {}, "Please login first!"
        
        if image is None:
            return {}, "Please upload an image!"
        
        try:
            # Get prediction from model
            prediction_result = self.model_handler.predict(image, return_all_probs=True)
            
            # Format for single prediction display
            if isinstance(prediction_result, tuple):
                # Convert tuple format to dictionary for gr.Label
                prediction, confidence = prediction_result
                prediction_result = {prediction: confidence}
            
            # Convert image to base64 for storage
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            # Save prediction to database (use highest confidence class for DB)
            if isinstance(prediction_result, dict):
                top_class = max(prediction_result.items(), key=lambda x: x[1])
                self.db_manager.save_prediction(
                    current_user["username"],
                    img_str,
                    top_class[0],  # Class name
                    top_class[1]   # Confidence
                )
            
            return prediction_result, f"Prediction saved to your history!"
            
        except Exception as e:
            return {}, f"Error processing image: {str(e)}"
    
    def load_sample_image(self, sample_path):
        """Load a sample image and return it as PIL Image"""
        try:
            if os.path.exists(sample_path):
                return Image.open(sample_path)
            else:
                print(f"Sample image not found: {sample_path}")
                return None
        except Exception as e:
            print(f"Error loading sample image: {e}")
            return None
    
    def create_prediction_interface(self):
        """Create the prediction interface with sample images"""
        with gr.Tab("🔍 New Prediction"):
            with gr.Row():
                with gr.Column(scale=1):
                    input_image = gr.Image(
                        label="Upload Eye Image",
                        type="pil",
                        height=300
                    )
                    predict_btn = gr.Button("Analyze Image", variant="primary", size="lg")
                
                with gr.Column(scale=1):
                    prediction_result = gr.Label(label="Prediction Result", num_top_classes=4)
            
            prediction_message = gr.Textbox(label="Status", interactive=False)
            
            # Sample Images Section
            gr.Markdown("### 📋 Sample Images - Click to Test")
            
            # All sample images in one row
            with gr.Row():
                sample_buttons = []
                for sample in self.sample_images:
                    with gr.Column(scale=1):
                        # Check if sample image exists and display it
                        if os.path.exists(sample["path"]):
                            sample_img = gr.Image(
                                value=sample["path"],
                                label=sample["name"],
                                height=150,
                                width=150,
                                interactive=False,
                                show_label=True
                            )
                        else:
                            # Show placeholder if image doesn't exist
                            sample_img = gr.HTML(
                                f"""<div style='height:150px; width:150px; border:2px dashed #ccc; 
                                display:flex; align-items:center; justify-content:center; 
                                text-align:center; color:#666;'>
                                {sample['name']}<br>Not Found</div>"""
                            )
                        
                        # Create button to load this sample
                        sample_btn = gr.Button(
                            f"Use {sample['name']}", 
                            size="sm",
                            variant="secondary"
                        )
                        sample_buttons.append((sample_btn, sample["path"]))
                        
                        # Add description
                        gr.Markdown(f"*{sample['description']}*", elem_classes="sample-desc")
        
        return input_image, predict_btn, prediction_result, prediction_message, sample_buttons
