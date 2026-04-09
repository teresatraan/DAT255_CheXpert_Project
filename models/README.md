# Models

This folder contains selected trained models used in the project.

---

## Included models

- `baseline_cnn_best.keras`  
  A baseline CNN trained from scratch.  
  This model is included to ensure reproducibility and to satisfy the course requirement of training at least one model without transfer learning.

---

## DenseNet121 (final model)

The main model of this project is **DenseNet121**, which is also used in the deployed application.

However, the full DenseNet121 model file is **not included in this repository** due to file size limitations.

Instead, it is available through the deployed demo:

https://huggingface.co/spaces/teresatraan/chexpert-xray-demo

---

## Notes

- DenseNet121 is the model used for:
  - final evaluation
  - threshold tuning
  - deployment

- The repository focuses on:
  - reproducibility (baseline model included)
  - transparency (evaluation results stored in `results/`)
  - clarity (training pipeline documented in notebooks)

- Full training and evaluation details can be found in the `notebooks/` folder.

---

## Important

This separation (including the baseline model but not the full DenseNet121 model) is intentional:

- to keep the repository lightweight  
- to comply with storage limitations  
- while still demonstrating a complete deep learning pipeline
