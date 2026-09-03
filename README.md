# 🚀 Project Progress

The project has evolved from raw industrial pump acoustic recordings into an end-to-end **predictive maintenance decision-support system**, combining acoustic feature engineering, machine learning, explainable AI, economic risk analysis, and Mixed-Integer Linear Programming (MILP).

---

## ✅ 1. Project Setup & Data Validation

- Established a modular and reproducible Python project structure.
- Configured Git/GitHub and a virtual environment.
- Validated the industrial pump acoustic dataset.
- Processed **868 acoustic recordings** from **4 pump IDs**.
- Identified **412 normal** and **456 abnormal** recordings.
- Verified recording integrity, sampling rate, duration, and signal readability.

---

## ✅ 2. Acoustic Feature Engineering

Converted raw acoustic recordings into structured numerical features using **Librosa**.

### Extracted Features

- Root Mean Square (RMS) Energy
- Zero Crossing Rate (ZCR)
- Spectral Centroid
- Spectral Bandwidth
- Spectral Roll-off
- 13 MFCC features

### Completed

- Built a reusable feature extraction pipeline.
- Extracted acoustic features from all **868 recordings**.
- Generated and exported the processed feature dataset for machine learning.
- Performed signal-level validation and inspection.

---

## ✅ 3. Exploratory Data Analysis

Performed statistical and visual analysis to understand the relationship between acoustic characteristics and pump operating conditions.

### Analysis Performed

- Dataset structure and data-quality checks
- Missing-value and duplicate checks
- Descriptive statistics
- Feature distributions and skewness analysis
- Outlier analysis using boxplots
- Normal vs. abnormal condition comparison
- Feature correlation analysis
- Correlation heatmaps

The analysis showed meaningful differences in acoustic characteristics between normal and abnormal operating conditions, supporting their use for predictive modeling.

---

## ✅ 4. Machine Learning & Model Optimization

Developed supervised machine learning models for pump failure prediction.

### Completed

- Prepared features and target labels.
- Applied train-test splitting and preprocessing.
- Evaluated multiple classification approaches.
- Addressed class imbalance using **SMOTE**.
- Compared model performance using:
  - Precision
  - Recall
  - F1-score
  - ROC-AUC
- Selected **Random Forest** as the primary predictive model.
- Performed **GridSearchCV-based hyperparameter optimization**.
- Optimized the prediction threshold to support maintenance-oriented decision making.

---

## ✅ 5. Explainable AI

Applied **SHAP (SHapley Additive exPlanations)** to understand how acoustic features influence model predictions.

### Completed

- Global feature importance analysis
- SHAP summary analysis
- Feature interaction analysis
- Feature dependence analysis
- Interpretation of individual model predictions

This provides greater transparency into why the model assigns higher failure probabilities to specific pumps.

---

## ✅ 6. Predictive Maintenance & Risk Analysis

Converted model predictions into actionable maintenance priorities.

### Completed

- Generated failure probabilities for individual pumps.
- Classified pumps according to risk level.
- Created maintenance priority scores.
- Estimated expected failure losses.
- Incorporated maintenance costs and maintenance duration.
- Calculated expected economic benefit for maintenance decisions.

This connects **machine learning predictions with operational and economic considerations**, rather than treating failure prediction as a standalone classification problem.

---

## ✅ 7. MILP-Based Maintenance Optimization

Developed a **Mixed-Integer Linear Programming (MILP)** framework to select the maintenance portfolio under limited maintenance capacity.

### Optimization Objective

The optimization framework considers:

- Failure probability
- Expected failure loss
- Maintenance cost
- Maintenance duration
- Risk constraints
- Available maintenance capacity

### Current Optimization Result

| Metric | Result |
|---|---:|
| Pumps Evaluated | **174** |
| Pumps Selected | **37** |
| Maintenance Capacity | **148 hours** |
| Capacity Utilization | **100%** |
| Actual Failures Available | **83** |
| Actual Failures Covered | **36** |
| Actual Failure Coverage | **43.37%** |
| Expected Failure Loss | **₹33.54 lakh** |
| Maintenance Cost | **₹2.96 lakh** |
| Expected Net Benefit | **₹30.58 lakh** |
| Net Benefit per Hour | **₹20,662/hour** |

The optimized portfolio is compared against alternative maintenance strategies, including ML risk ranking and economic ranking.

---

## 🚧 8. Interactive Decision-Support Dashboard

A **Streamlit dashboard** has been developed to present the predictive maintenance results in an engineering-friendly format.

### Dashboard Components

- Executive maintenance KPIs
- Recommended maintenance strategy
- Strategy comparison
- Pump risk profile
- Selected maintenance portfolio
- Expected economic benefits
- Maintenance capacity utilization
- Downloadable portfolio results

The dashboard provides a visual interface for interpreting the output of the ML and optimization pipeline.

---

## 🔄 9. Project Finalization

Current work is focused on improving the presentation and reproducibility of the completed system.

### Remaining Tasks

- Finalize dashboard presentation
- Improve README and project documentation
- Organize repository structure
- Clean and document reusable code
- Prepare the project for portfolio/deployment presentation

---

# 🎯 End-to-End System

```text
Industrial Pump Acoustic Recordings
                │
                ▼
        Data Validation
                │
                ▼
      Signal Inspection
                │
                ▼
     Acoustic Feature Extraction
                │
                ▼
          EDA & Analysis
                │
                ▼
      Data Preprocessing
                │
                ▼
     Machine Learning Models
                │
                ▼
   Random Forest + Optimization
                │
                ▼
       Failure Probability
                │
                ▼
       Risk & Economic Analysis
                │
                ▼
       MILP Maintenance Optimization
                │
                ▼
     Optimized Maintenance Portfolio
                │
                ▼
       Streamlit Dashboard
                │
                ▼
 Predictive Maintenance Decision Support
```
