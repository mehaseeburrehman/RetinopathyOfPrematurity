
import tensorflow as tf
import numpy as np
from PIL import Image
from datetime import datetime

model = tf.keras.models.load_model("vgg19_rop_512x512_3.h5")
class_names = ["Healthy", "Type1", "Type2", "RD"]
PRED_LOG = "logs/predictions.csv"

def predict_rop(img: Image.Image, username="anonymous", image_name="input_image"):
    img = img.resize((512, 512)).convert("RGB")
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    preds = model.predict(img_array)[0]
    predicted_index = int(np.argmax(preds))
    predicted_class = class_names[predicted_index]
    confidence = float(preds[predicted_index])
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(PRED_LOG, "a") as f:
        f.write(f"{username},{time},{image_name},{predicted_class},{confidence:.4f}\n")
    return {class_names[i]: float(preds[i]) for i in range(4)}
