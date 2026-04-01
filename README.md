# Multi-label Chest X-ray Diagnosis (DAT255)

This project was developed as part of **DAT255 – Deep Learning Engineering** at the Western Norway University of Applied Sciences (HVL).

The goal of this project is to build a deep learning system for **multi-label classification of chest X-ray images** using the **CheXpert dataset**. The model predicts multiple thoracic conditions from a single image.

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
- Includes uncertainty labels

**Note:** The dataset is **not included** in this repository.

---

## Models

We experiment with several convolutional neural network architectures:

- DenseNet121 (primary model)
- ResNet50 (comparison)
- EfficientNetB0 (comparison)
- A custom baseline CNN trained from scratch

### Methods used

- Transfer learning
- Fine-tuning
- Data preprocessing and normalization

---

## Model Selection

Although multiple models were evaluated, **DenseNet121** was selected as the final deployed model.

While the baseline CNN and ResNet50 achieved competitive or slightly higher validation scores, DenseNet121 was chosen due to:

- strong and consistent performance across labels  
- robustness and better generalization  
- widespread use in medical imaging  
- alignment with architectures used in the CheXpert benchmark  

This makes DenseNet121 a more reliable and interpretable choice for this task.

---

## Deployment Model

The deployed web application uses **DenseNet121**.

The model predicts the following five conditions:

- Atelectasis  
- Cardiomegaly  
- Consolidation  
- Edema  
- Pleural Effusion  

The output consists of probability scores for each label, using a multi-label classification setup (sigmoid activation).

---

## Evaluation

We evaluate the models using metrics suitable for multi-label classification:

- Accuracy  
- Precision / Recall  
- F1-score  
- ROC-AUC (most important metric)

---

## Web Application

We deploy the model using **Gradio**.

The app allows users to:

- Upload chest X-ray images  
- View predicted conditions with probabilities  
- (Optional) Visualize model attention using Grad-CAM  

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
└── src/        # Optional reusable code

```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
## Important Notes
- This project is for educational purposes only
- It is not suitable for clinical use
- Predictions must not be used for medical decision-making
```

---

## Course
DAT255 – Deep Learning Engineering
Western Norway University of Applied Sciences (HVL)
