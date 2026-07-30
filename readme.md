# Kidney Stone Detection Using Machine Learning

Early detection of kidney stones from urinalysis data using classical machine learning models, developed as part of an MSc Computer Science dissertation at York St John University.

## Overview

Kidney stones are a common and increasingly prevalent urological condition. Traditional diagnostic methods (X-ray, ultrasound, CT scans, lab tests) can be slow, imprecise, or expensive. This project explores whether simple urinalysis measurements can be used to predict the presence of kidney stones using machine learning, and packages the best-performing model behind a web application built with Django.

The project analyzes six urinary characteristics:

• Gravity — specific gravity of urine
• pH — acidity/alkalinity of urine
• Osmolarity (osmo) — concentration of solutes in urine
• Conductivity (cond) — electrical conductivity of urine
• Urea concentration (urea)
• Calcium level (calc)

and predicts a binary target: presence (1) or absence (0) of a kidney stone.

## Models

Four classification algorithms were trained and compared on a 70/30 train-test split:
| Model | Accuracy | Precision | Recall | F1-Score |
|-------------------------------|----------|-----------|--------|----------|
| Logistic Regression | 87.50% | 0.80 | 0.89 | 0.84 |
| Random Forest | 83.33% | 0.73 | 0.89 | 0.80 |
| Decision Tree | 70.83% | 0.58 | 0.78 | 0.67 |
| Support Vector Machine (SVM) | 58.33% | 0.00 | 0.00 | 0.00 |

## Methodology

**Data Collection** — Dataset sourced from Kaggle, containing urinalysis records with the six features above.
**Preprocessing** — Checked for missing values and duplicates (none found in this dataset); no scaling/normalization was required.
**Train/Test Split** — 70% training, 30% testing (random_state=10).
**Model Training** — Logistic Regression, Random Forest, Decision Tree, and SVM trained using scikit-learn defaults (Random Forest tuned with max_depth=10, n_estimators=50).
**Evaluation** — Accuracy, precision, recall, F1-score, and confusion matrices computed for each model.
**Feature Importance** — Logistic Regression coefficients used to rank feature influence.
**Deployment** — Best model (Logistic Regression) serialized with joblib to savedModels/model.joblib for use in the Django web app.

## Libraries Used

**NumPy & Pandas** — data loading and manipulation
**Matplotlib & Seaborn** — data visualization (histograms, correlation heatmap, feature importance)
**Scikit-learn** — model training (LogisticRegression, RandomForestClassifier, DecisionTreeClassifier, SVC) and evaluation (classification_report, confusion_matrix, accuracy_score)
**Joblib** — model serialization

## Disclaimer

This project is an academic research prototype. It is not a certified medical diagnostic tool and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
