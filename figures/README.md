# Figures

This folder contains plots and visualizations used to support model analysis, evaluation, and interpretation.

The figures are used both for **quantitative comparison** and **qualitative understanding** of model behaviour.

---

## Contents

- **ROC and PR curves**  
  Used to evaluate model performance across different decision thresholds, especially important for multi-label classification.

- **Training and validation curves**  
  Show loss and performance over time, helping to identify:
  - convergence behaviour  
  - overfitting / underfitting  
  - training stability  

- **Dataset distribution plots**  
  Provide insight into class imbalance, which is a key challenge in medical datasets like CheXpert.

- **Grad-CAM visualizations**  
  Used for interpretability, showing which regions of the X-ray contribute most to the model’s predictions.

---

## Purpose

The figures in this folder are used to:

- compare model performance beyond single metrics  
- support the model selection process  
- analyse strengths and weaknesses across labels  
- provide interpretability and transparency  

---

## Notes

All figures are generated from the notebooks in the `notebooks/` folder and are referenced in the project report.

They are included to ensure that the project is not only evaluated numerically, but also visually and qualitatively.
