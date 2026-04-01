import numpy as np
import gradio as gr
from PIL import Image
from tensorflow import keras
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "densenet121_finetuned_best.keras"

LABELS = [
    "Atelectasis",
    "Cardiomegaly",
    "Consolidation",
    "Edema",
    "Pleural Effusion"
]

THRESHOLDS = {
    "Atelectasis": 0.3408,
    "Cardiomegaly": 0.1205,
    "Consolidation": 0.2335,
    "Edema": 0.3389,
    "Pleural Effusion": 0.4579,
}

BORDERLINE_MARGIN = 0.10
IMG_SIZE = (224, 224)

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = keras.models.load_model(MODEL_PATH)
preprocess_input = keras.applications.densenet.preprocess_input


def preprocess_image(image: Image.Image) -> np.ndarray:
    if image is None:
        raise ValueError("No image uploaded.")

    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)
    image = np.array(image).astype("float32")
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image


def make_decision_text(results: dict) -> str:
    positive_findings = []
    borderline_findings = []

    for label, score in results.items():
        threshold = THRESHOLDS[label]

        if score >= threshold:
            positive_findings.append(f"{label} ({score:.2f}, threshold: {threshold:.2f})")
        elif score >= max(0.0, threshold - BORDERLINE_MARGIN):
            borderline_findings.append(f"{label} ({score:.2f}, threshold: {threshold:.2f})")

    lines = []

    if positive_findings:
        lines.append("Positive findings:")
        for item in positive_findings:
            lines.append(f"- {item}")
    else:
        lines.append("No high-confidence findings.")

    if borderline_findings:
        lines.append("")
        lines.append("Possible / borderline findings:")
        for item in borderline_findings:
            lines.append(f"- {item}")

    lines.append("")
    lines.append("⚠️ This model is for research and decision support only.")
    lines.append("It must not be used as a substitute for medical diagnosis.")

    return "\n".join(lines)


def predict_xray(image: Image.Image):
    x = preprocess_image(image)
    preds = model.predict(x, verbose=0)[0]

    results = {label: float(score) for label, score in zip(LABELS, preds)}
    results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

    decision_text = make_decision_text(results)
    return results, decision_text


interface_kwargs = dict(
    fn=predict_xray,
    inputs=gr.Image(type="pil", label="Upload chest X-ray"),
    outputs=[
        gr.Label(num_top_classes=5, label="Predicted findings (probabilities)"),
        gr.Textbox(label="Model decision", lines=14)
    ],
    title="Chest X-ray Multi-label Classification",
    description="Upload a chest X-ray image to get predicted probabilities and threshold-based findings."
)

try:
    demo = gr.Interface(**interface_kwargs, flagging_mode="never")
except TypeError:
    demo = gr.Interface(**interface_kwargs)

if __name__ == "__main__":
    demo.launch(debug=True, inbrowser=True)