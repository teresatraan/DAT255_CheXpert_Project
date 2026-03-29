# Multi-label Chest X-ray Diagnosis (DAT255)

This project is part of the course **DAT255 – Deep Learning Engineering**.

We develop a deep learning model for **multi-label classification of chest X-ray images**, using the **CheXpert dataset**. The goal is to automatically detect multiple thoracic conditions from medical images and support diagnostic decision-making.

---

## Problem Description

Chest X-ray interpretation is a complex and time-consuming task. This project aims to build a deep learning model that can:

- Analyze chest X-ray images
- Predict multiple possible diseases simultaneously (multi-label classification)
- Provide probability scores for each condition

---

## Model

We use Convolutional Neural Networks (CNNs), including:

- DenseNet121 (primary model)
- ResNet50 (comparison)
- EfficientNetB0 (comparison)

## We apply:
- Transfer learning
- Fine-tuning
- Data preprocessing and normalization

---

## Project Structure

DAT255_CheXpert_Project/
├── app/ # Gradio web application
├── data/ # Dataset (not included in repo)
├── models/ # Saved models (not included in repo)
├── notebooks/ # Jupyter notebooks for experiments
├── reports/ # Project report
├── figures/ # Plots and visualizations
├── src/ # Optional reusable code


---
 
---

## How to Run:

### 1. Install dependencies

```bash
pip install tensorflow numpy pillow gradio´
```


### 2.Run the web app: 
```bash
python app/app.py
```
---

## Web Application
We deploy the model using Gradio, allowing users to:
Upload chest X-ray images
View predicted conditions with probabilities
(Optional) Visualize model attention using Grad-CAM

## Evaluation
We evaluate the model using:
Accuracy
Precision / Recall
F1-score
ROC-AUC (important for multi-label classification)

## Dataset
We use the CheXpert dataset from Stanford ML Group:
224,000+ chest X-ray images
Multi-label annotations
Includes uncertainty labels
Dataset is not included in this repository.

### Important Notes
This project is for educational purposes only.
The model is not suitable for clinical use
Predictions should not be used for medical decisions

### Authors
- Kieu-Mi Teresa Tran
- Laiba Siddiqui Khan
- Victoria Sirisombat Johansen
- Kjetil Andre Moen Eide

## Course
DAT255 – Deep Learning Engineering
Western Norway University of Applied Sciences (HVL)
