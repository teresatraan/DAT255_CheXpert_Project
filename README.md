# Multi-label Chest X-ray Diagnosis (DAT255)

This project was developed as part of **DAT255 – Deep Learning Engineering** at the Western Norway University of Applied Sciences (HVL).

The goal of this project is to build a deep learning system for **multi-label classification of chest X-ray images** using the **CheXpert dataset**. The model predicts multiple thoracic conditions from a single image.

---

## Demo

Try the deployed web application here:

https://huggingface.co/spaces/teresatraan/chexpert-xray-demo

The app allows users to upload a chest X-ray image and receive model predictions directly in the browser.

---

## Video Demo

Watch a demonstration of the system here:

👉 *insert link*

---

## Key Results

- Best model: **DenseNet121 (transfer learning)**
- Task: Multi-label classification (5 conditions)
- Evaluation metric: **ROC-AUC (primary)**
- Additional metrics: Precision, Recall, F1-score

DenseNet121 was selected due to it´s strong and consistent performance, robustness, and suitability for medical imaging tasks.

---

## Problem Description

Chest X-ray interpretation is a complex and time-consuming task. This project investigates whether deep learning models can assist by automatically identifying multiple findings in radiographs.

The system is designed to:

- Analyze chest X-ray images  
- Predict multiple conditions simultaneously (multi-label classification)  
- Output probability scores for each condition  

---

## Dataset

We use the **CheXpert dataset** from Stanford ML Group:

- 224,000+ chest X-ray images  
- Multi-label annotations  
- Includes **uncertain labels**  

**Note:** The dataset is **not included** in this repository.

---

## Models

We experiment with several convolutional neural network architectures:

- **DenseNet121** (final model)
- ResNet50 (comparison)
- EfficientNetB0 (comparison)
- Custom baseline CNN (trained from scratch)

### Methods used

- Transfer learning  
- Fine-tuning  
- Data preprocessing and normalization  

---

## Model Selection

Although multiple models were evaluated, **DenseNet121** was selected as the final deployed model.

While the baseline CNN and ResNet50 achieved competitive or slightly higher validation scores, DenseNet121 was chosen due to:

- Strong and consistent performance across labels  
- Better generalization  
- Proven effectiveness in medical imaging  
- Alignment with architectures used in the CheXpert benchmark  

---

## Evaluation

We evaluate the models using metrics suitable for multi-label classification:

- Accuracy  
- Precision / Recall  
- F1-score  
- **ROC-AUC (primary metric)**  

---

## Project Workflow

Run the notebooks in the following order:

1. `01_setup_and_data_overview.ipynb`
2. `02_preprocessing_and_data_pipeline.ipynb`
3. `03_model_training_baselines.ipynb`
4. `04_transfer_learning_densenet121.ipynb`
5. `05_transfer_learning_resnet50.ipynb`
6. `06_model_interpretability.ipynb`
7. `07_transfer_learning_efficientnetb0.ipynb`

---

## Web Application

The model is deployed using **Gradio** and hosted on **Hugging Face Spaces**.

The app allows users to:

- Upload chest X-ray images  
- View predicted conditions with probabilities  
- Visualize model attention using Grad-CAM  

---

## Project Structure

```bash
DAT255_CheXpert_Project/
├── app/        # Gradio web application
├── data/       # Dataset (not included)
├── models/     # Saved models (not included)
├── notebooks/  # Experiments and training
├── reports/    # Project report
├── figures/    # Visualizations
└── src/        # Reusable code
```

---
## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Important Notes

This project is for educational purposes only
It is not suitable for clinical use
Predictions must not be used for medical decision-making

---

## Course

DAT255 – Deep Learning Engineering
Western Norway University of Applied Sciences (HVL)
