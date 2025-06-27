import gradio as gr
import pandas as pd
import os

class HistoryUI:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def get_prediction_history(self, current_user):
        """Get user's prediction history"""
        if not current_user["logged_in"]:
            return "Please login first!"
        
        history = self.db_manager.get_user_history(current_user["username"])
        
        if not history:
            return "No prediction history found."
        
        # Format history for display
        history_text = "## Your Prediction History\n\n"
        for record in history:
            history_text += f"**Date:** {record['timestamp']}\n"
            history_text += f"**Prediction:** {record['prediction']}\n"
            history_text += f"**Confidence:** {record['confidence']:.2%}\n"
            history_text += "---\n"
        
        return history_text

    def download_history(self, current_user):
        """Download prediction history as CSV"""
        if not current_user["logged_in"]:
            return None
        
        history = self.db_manager.get_user_history(current_user["username"])
        
        if not history:
            return None
        
        try:
            # Convert to DataFrame
            df = pd.DataFrame(history)
            df = df.drop('image_data', axis=1)  # Remove image data for CSV
            
            # Create filename with absolute path
            filename = f"{current_user['username']}_prediction_history.csv"
            filepath = os.path.abspath(filename)
            
            # Save to CSV
            df.to_csv(filepath, index=False)
            
            # Return the filepath for Gradio to serve
            return filepath
            
        except Exception as e:
            print(f"Error creating CSV: {e}")
            return None
    
    def create_history_interface(self):
        """Create the history interface"""
        with gr.Tab("📊 Prediction History"):
            with gr.Row():
                history_btn = gr.Button("Load History", variant="primary")
                download_btn = gr.Button("Download CSV", variant="secondary")
            
            history_display = gr.Markdown(label="Your History")
            download_file = gr.File(label="Download Your History", visible=True)
        
        return history_btn, download_btn, history_display, download_file
