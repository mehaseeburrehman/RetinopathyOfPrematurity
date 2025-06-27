import gradio as gr

class LoginUI:
    def __init__(self, auth_manager):
        self.auth_manager = auth_manager
        self.current_user = {"username": None, "logged_in": False}
    
    def login_user(self, username, password):
        """Handle user login"""
        if self.auth_manager.verify_user(username, password):
            self.current_user["username"] = username
            self.current_user["logged_in"] = True
            return (
                gr.update(visible=False),  # Hide login
                gr.update(visible=True),   # Show main app
                f"Welcome back, {username}!",
                gr.update(value="")  # Clear password
            )
        else:
            return (
                gr.update(visible=True),   # Keep login visible
                gr.update(visible=False),  # Keep main app hidden
                "Invalid username or password!",
                gr.update(value="")  # Clear password
            )

    def register_user(self, username, password, confirm_password):
        """Handle user registration"""
        if password != confirm_password:
            return "Passwords do not match!"
        
        if len(password) < 6:
            return "Password must be at least 6 characters long!"
        
        if self.auth_manager.create_user(username, password):
            return f"Account created successfully for {username}! You can now login."
        else:
            return "Username already exists!"

    def logout_user(self):
        """Handle user logout"""
        self.current_user["username"] = None
        self.current_user["logged_in"] = False
        return (
            gr.update(visible=True),   # Show login
            gr.update(visible=False),  # Hide main app
            "Logged out successfully!"
        )
    
    def create_login_interface(self):
        """Create the login/register interface"""
        with gr.Column(visible=True) as login_interface:
            gr.HTML("<h2>Login or Register</h2>")
            
            with gr.Tab("Login"):
                with gr.Row():
                    with gr.Column():
                        login_username = gr.Textbox(label="Username", placeholder="Enter your username")
                        login_password = gr.Textbox(label="Password", type="password", placeholder="Enter your password")
                        login_btn = gr.Button("Login", variant="primary")
            
            with gr.Tab("Register"):
                with gr.Row():
                    with gr.Column():
                        reg_username = gr.Textbox(label="Username", placeholder="Choose a username")
                        reg_password = gr.Textbox(label="Password", type="password", placeholder="Choose a password (min 6 chars)")
                        reg_confirm = gr.Textbox(label="Confirm Password", type="password", placeholder="Confirm your password")
                        register_btn = gr.Button("Register", variant="secondary")
            
            auth_message = gr.Textbox(label="Message", interactive=False)
        
        return login_interface, login_username, login_password, login_btn, reg_username, reg_password, reg_confirm, register_btn, auth_message
