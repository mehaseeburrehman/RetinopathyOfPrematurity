import gradio as gr

class AboutUI:
    @staticmethod
    def create_about_interface():
        """Create the about interface"""
        with gr.Tab("ℹ️ About"):
            gr.Markdown("""
            ## About This Application
            
            This Eye Image Classification System uses advanced machine learning to analyze eye images and detect:
            
            - **Healthy**: Normal eye condition
            - **Retinal Detachment**: Separation of retinal layers
            - **Type 1**:Criticle immediate tretement
            - **Type 2**:Not immediate tretement
            
            ### How to Use:
            1. **Login** or **Register** a new account
            2. **Upload** an eye image in the "New Prediction" tab
            3. **View** your prediction history in the "Prediction History" tab
            4. **Download** your history as CSV for record keeping
            
            ### Important Notes:
            - This tool is for educational/research purposes only
            - Always consult healthcare professionals for medical diagnosis
            - Supported formats: JPG, PNG, JPEG
            - Maximum file size: 10MB
            """)
