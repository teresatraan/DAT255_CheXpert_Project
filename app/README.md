# Application (Gradio Demo)

This folder contains the deployed web application for the project.

The app is built using **Gradio** and hosted on **Hugging Face Spaces**, allowing users to interact with the model directly in the browser.

---

## Purpose

The application demonstrates the **end-to-end pipeline**:

1. Upload a chest X-ray image  
2. Preprocess the image  
3. Run inference using the trained model (DenseNet121)  
4. Apply threshold-based decision logic  
5. Present results in a human-readable format  

---

## Model used

The app uses the **DenseNet121 model**, which is the final selected model of the project.

- Model file: `densenet121_finetuned_best.keras`
- Preprocessing: `keras.applications.densenet.preprocess_input`
- Output: multi-label probabilities for 5 conditions

---

## Decision logic

Predictions are not interpreted using a fixed threshold (e.g. 0.5).

Instead, we use **label-specific thresholds**, tuned during evaluation:

```python
THRESHOLDS = {
    "Atelectasis": 0.3408,
    "Cardiomegaly": 0.1205,
    "Consolidation": 0.2335,
    "Edema": 0.3389,
    "Pleural Effusion": 0.4579,
}
