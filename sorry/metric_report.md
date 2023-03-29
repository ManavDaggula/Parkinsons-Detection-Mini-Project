# Metrics for each model

## Accuracy
| Model | Plain Set | Removed high Corelations | PCA | Feature Selection |
| ----- | --------- | ------------------------ | --- | ----------------- |
| Support Vector Machine | 0.897 | 0.897 | 0.795 | 0.795 |
| Logistic Regression | 0.821 | 0.821 | 0.872 | 0.795 |
| Random Forest | 0.821 | 0.872 | 0.769 | 0.769 |
| Decision Trees | 0.821 | 0.846 | 0.821 | 0.769 |

## Precision
| Model | Plain Set | Removed high Corelations | PCA | Feature Selection |
| ----- | --------- | ------------------------ | --- | ----------------- |
| Support Vector Machine | 0.886 | 0.909 | 0.848 | 0.848 |
| Logistic Regression | 0.900 | 0.875 | 0.861 | 0.871 |
| Random Forest | 0.962 | 0.964 | 0.893 | 0.867 |
| Decision Trees | 0.853 | 0.857 | 0.875 | 0.844 |

## Recall
| Model | Plain Set | Removed high Corelations | PCA | Feature Selection |
| ----- | --------- | ------------------------ | --- | ----------------- |
| Support Vector Machine | 1.000 | 0.968 | 0.903 | 0.903 |
| Logistic Regression | 0.871 | 0.903 | 1.00 | 0.871 |
| Random Forest | 0.806 | 0.871 | 0.806 | 0.839 |
| Decision Trees | 0.935 | 0.968 | 0.903 | 0.871 |

## F1 Score
| Model | Plain Set | Removed high Corelations | PCA | Feature Selection |
| ----- | --------- | ------------------------ | --- | ----------------- |
| Support Vector Machine | 0.939 | 0.937 | 0.875 | 0.905 |
| Logistic Regression | 0.885 | 0.889 | 0.925 | 0.871 |
| Random Forest | 0.877 | 0.915 | 0.847 | 0.852 |
| Decision Trees | 0.892 | 0.909 | 0.889 | 0.857 |