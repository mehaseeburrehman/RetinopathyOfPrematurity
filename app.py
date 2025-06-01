
import gradio as gr
import pandas as pd
from auth import login, signup
from model_handler import predict_rop

session = {"user": None}

def try_login(username, password):
    message, success = login(username, password)
    if success:
        session["user"] = username
        return gr.update(visible=False), gr.update(visible=True), message
    return gr.update(visible=True), gr.update(visible=False), message

def try_signup(username, password):
    return signup(username, password)

def predict_with_user(image):
    return predict_rop(image, username=session["user"], image_name="input_image")

def show_user_logs():
    df = pd.read_csv("logs/predictions.csv")
    if session["user"]:
        df = df[df["username"] == session["user"]]
    return df.tail(10)

def logout_user():
    session["user"] = None
    return gr.update(visible=True), gr.update(visible=False), ""

with gr.Blocks() as app:
    gr.Markdown("## 🧠 ROP Detection System")

    with gr.Column(visible=True) as login_section:
        gr.Markdown("### 🔐 Login or Sign Up")
        username = gr.Textbox(label="Username")
        password = gr.Textbox(label="Password", type="password")
        login_btn = gr.Button("Login")
        signup_btn = gr.Button("Sign Up")
        login_status = gr.Textbox(label="Status", interactive=False)

    with gr.Column(visible=False) as predict_section:
        gr.Markdown("### Welcome! Upload a Retina Image")
        image_input = gr.Image(type="pil")
        predict_btn = gr.Button("Predict")
        prediction_output = gr.Label(num_top_classes=4)
        predict_btn.click(fn=predict_with_user, inputs=image_input, outputs=prediction_output)

        gr.Markdown("### Your Recent Predictions")
        logs_btn = gr.Button("Refresh History")
        history_table = gr.Dataframe()
        logs_btn.click(fn=show_user_logs, outputs=history_table)

        logout_btn = gr.Button("Logout")
        logout_btn.click(fn=logout_user, outputs=[login_section, predict_section, login_status])

    login_btn.click(fn=try_login, inputs=[username, password],
                    outputs=[login_section, predict_section, login_status])
    signup_btn.click(fn=try_signup, inputs=[username, password], outputs=[login_status])

if __name__ == "__main__":
    app.launch()
