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

 [Watch the demo video](https://youtu.be/fPE2sQRADvQ)

---

## Key Results

- Final model: **DenseNet121 (transfer learning)**
- Task: Multi-label classification (5 conditions)
- Primary metric: **ROC-AUC**
- Additional metrics: Precision, Recall, F1-score

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

- **DenseNet121** (final + deployed model)
- ResNet50 (comparison)
- EfficientNetB0 (comparison)
- Custom baseline CNN (trained from scratch)

### Methods used

- Transfer learning  
- Fine-tuning  
- Data preprocessing and normalization  
- Threshold tuning for multi-label prediction  

---

## Model Selection

Although multiple models were evaluated, **DenseNet121** was selected as the final and deployed model.

It is important to note:

- The **Baseline CNN achieved the best validation scores on some metrics** (e.g. ROC-AUC and validation loss)
- However, **DenseNet121 was chosen deliberately**, based on a broader engineering and domain-specific assessment

### Why DenseNet121?

The decision was based on several factors:

- **Architecture suited for medical imaging**  
  DenseNet reuses features across layers, which is beneficial for detecting subtle patterns in chest X-rays.

- **Transfer learning advantage**  
  Pretraining provides a stronger starting point than a model trained from scratch.

- **Small performance differences**  
  The gap between models is relatively small, meaning model choice should not rely solely on a single validation metric.

- **Better alignment with deployment pipeline**  
  The entire inference system is built around DenseNet121:
  - preprocessing uses `keras.applications.densenet.preprocess_input`
  - the deployed model is `densenet121_finetuned_best.keras`
  - class-specific thresholds are tuned specifically for this model

- **End-to-end system consistency**  
  DenseNet121 is the model for which the full pipeline (training → evaluation → thresholding → deployment) is most complete and consistent.

- **Relevance to domain and literature**  
  DenseNet architectures are commonly used in medical imaging tasks, including the original CheXpert benchmark.

### Summary

The final model choice reflects a **trade-off between performance, robustness, domain suitability, and deployment consistency**, rather than selecting the model with the highest score on a single metric.

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
- Generate human-readable decision summaries  
- Apply **threshold-based classification logic**  
- Visualize model attention using Grad-CAM  

---

## Project Structure

```bash
DAT255_CheXpert_Project/
├── app/        # Gradio web application
├── models/     # Saved models and notes
├── notebooks/  # Experiments and training
├── results/    # Evaluation outputs and comparisons
├── figures/    # Visualizations
├── README.md
└── requirements.txt
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


