import gradio as gr
import os
from PIL import Image
from auth import AuthManager
from database import DatabaseManager
from model_handler import ModelHandler
from ui_components import LoginUI, PredictionUI, HistoryUI, AboutUI

# Initialize components
auth_manager = AuthManager()
db_manager = DatabaseManager()
model_handler = ModelHandler()

# Initialize UI components
login_ui = LoginUI(auth_manager)
prediction_ui = PredictionUI(model_handler, db_manager)
history_ui = HistoryUI(db_manager)
about_ui = AboutUI()

# Create Gradio interface
with gr.Blocks(title="Retinopathy of prematurity App") as app:
    gr.HTML("""
<style>
.short-btn {
    width: 120px !important;
    min-width: 80px !important;
    max-width: 150px !important;
    margin-left: auto;
    margin-right: 0;
}
.sample-desc {
    font-size: 12px !important;
    text-align: center !important;
    margin-top: 5px !important;
    color: #666 !important;
}
</style>
""")
    

    gr.Markdown("<h1 style='text-align: center;'>Retinopathy of prematurity System</h1>")
    
    # Create login interface
    (login_interface, login_username, login_password, login_btn, 
     reg_username, reg_password, reg_confirm, register_btn, auth_message) = login_ui.create_login_interface()
    
    # Main Application Interface
    with gr.Column(visible=False) as main_interface:
        with gr.Row():
            gr.HTML("<h2>Welcome to Retinopathy of prematurity</h2>")
            logout_btn = gr.Button("Logout", elem_classes="short-btn")
        
        # Create prediction interface
        input_image, predict_btn, prediction_result, prediction_message, sample_buttons = prediction_ui.create_prediction_interface()
        
        # Create history interface
        history_btn, download_btn, history_display, download_file = history_ui.create_history_interface()
        
        # Create about interface
        about_ui.create_about_interface()
    
    # Event handlers
    login_btn.click(
        login_ui.login_user,
        inputs=[login_username, login_password],
        outputs=[login_interface, main_interface, auth_message, login_password]
    )
    
    register_btn.click(
        login_ui.register_user,
        inputs=[reg_username, reg_password, reg_confirm],
        outputs=[auth_message]
    )
    
    logout_btn.click(
        login_ui.logout_user,
        outputs=[login_interface, main_interface, auth_message]
    )
    
    predict_btn.click(
        lambda image: prediction_ui.predict_image(image, login_ui.current_user),
        inputs=[input_image],
        outputs=[prediction_result, prediction_message]
    )
    
    # Sample image button handlers
    def load_sample_to_input(sample_path):
        """Load sample image to the input area"""
        try:
            if os.path.exists(sample_path):
                return Image.open(sample_path)
            else:
                return None
        except Exception as e:
            print(f"Error loading sample: {e}")
            return None
    
    # Connect each sample button to load its image
    for sample_btn, sample_path in sample_buttons:
        sample_btn.click(
            lambda path=sample_path: load_sample_to_input(path),
            outputs=[input_image]
        )
    
    history_btn.click(
        lambda: history_ui.get_prediction_history(login_ui.current_user),
        outputs=[history_display]
    )
    
    download_btn.click(
        lambda: history_ui.download_history(login_ui.current_user),
        outputs=[download_file]
    )

if __name__ == "__main__":
    print("🚀 Starting Retinopathy of prematurity App...")
    print("📊 Initializing database...")
    db_manager.init_db()
    print("🤖 Loading ML model...")
    model_handler.load_model()
    print("✅ App ready!")
    
    app.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=True,
        show_error=True
    )
