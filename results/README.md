# Results

This folder contains the key evaluation outputs used for **model comparison, analysis, and final model selection**.

The structure is designed to make the results transparent, reproducible, and easy to interpret.

---

## Structure

### model_comparison/
Contains aggregated comparisons across all models:

- `ALL_MODELS_COMPARISON.csv`  
  → Summary of all models using key validation metrics

- `baseline_vs_densenet121_comparison.csv`  
  → Direct comparison between baseline CNN and DenseNet121

- `baseline_vs_densenet121_per_label_auc.csv`  
  → Per-label comparison between the two main models

---

### evaluation/
Contains overall evaluation metrics for each model:

- validation loss  
- binary accuracy  
- ROC-AUC  
- PR-AUC  

Each file corresponds to one trained model:
- baseline CNN  
- DenseNet121  
- ResNet50  
- EfficientNetB0  

---

### per_label/
Contains detailed performance for individual labels:

- `densenet121_per_label_auc.json`

This is important because performance varies across medical conditions, and overall metrics may hide these differences.

---

### thresholds/
Contains threshold tuning results for the deployed DenseNet121 model:

- `densenet121_best_thresholds.json`  
  → Optimal decision thresholds per label

- `densenet121_threshold_metrics.csv`  
  → Performance after applying tuned thresholds

Threshold tuning is critical in multi-label classification, where a fixed threshold (e.g. 0.5) is often suboptimal.

---

## Model selection context

Although the baseline CNN achieved the strongest validation metrics in some comparisons, DenseNet121 was selected as the final model.

The results in this folder support this decision by enabling:

- comparison across models  
- per-label performance analysis  
- threshold-based evaluation  
- inspection of trade-offs between models  

---

## Notes

Only the most relevant results are included to keep the repository clean and focused, while still supporting the conclusions presented in the project report.
