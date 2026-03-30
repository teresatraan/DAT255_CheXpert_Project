import numpy as np
import gradio as gr
from PIL import Image
from tensorflow import keras

MODEL_PATH = "models/densenet121_finetuned_best.keras"

LABELS = [
    "Atelectasis",
    "Cardiomegaly",
    "Consolidation",
    "Edema",
    "Pleural Effusion"
]

IMG_SIZE = (224, 224)

model = keras.models.load_model(MODEL_PATH)
preprocess_input = keras.applications.densenet.preprocess_input


def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)
    image = np.array(image).astype("float32")
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image


def predict_xray(image: Image.Image):
    x = preprocess_image(image)
    preds = model.predict(x, verbose=0)[0]

    results = {}
    for label, score in zip(LABELS, preds):
        results[label] = float(score)

    return results


demo = gr.Interface(
    fn=predict_xray,
    inputs=gr.Image(type="pil", label="Upload chest X-ray"),
    outputs=gr.Label(num_top_classes=5, label="Predicted conditions"),
    title="Chest X-ray Multi-label Classification",
    description="Upload a chest X-ray image to get predicted probabilities for 5 thoracic conditions."
)

if __name__ == "__main__":
    demo.launch()
