# 🚀 Project Progress

The project has evolved from raw industrial pump acoustic recordings into an end-to-end **predictive maintenance decision-support system**, combining acoustic feature engineering, machine learning, explainable AI, economic risk analysis, and Mixed-Integer Linear Programming (MILP).

---

## ✅ 1. Project Setup & Data Validation

The project was initialized as a structured and reproducible machine learning engineering workflow for developing an industrial pump predictive maintenance system. The first stage focused on organizing the development environment and validating the raw acoustic dataset before performing any signal processing or machine learning.

### Project Environment Setup

A modular project structure was created to separate different components of the development workflow and make the project easier to maintain, reproduce, and extend.

The repository was organized into dedicated directories for:

- **Data** – raw and processed datasets.
- **Notebooks** – exploratory analysis, experimentation, and the end-to-end development workflow.
- **Source Code (`src/`)** – reusable Python functions and processing modules.
- **Models** – trained and optimized machine learning models.
- **Results** – model outputs, predictions, evaluation results, and optimization results.
- **Reports** – analysis outputs and project documentation.
- **Images** – visualizations generated during analysis and modeling.

Git and GitHub were configured for version control so that changes to the project could be tracked throughout development. A dedicated Python virtual environment was also created to isolate the project's dependencies and maintain a consistent execution environment.

An end-to-end project notebook was created to document the complete workflow, from raw acoustic data processing through predictive modeling and maintenance decision analysis.

---

### Dataset Validation

Before feature engineering, the raw industrial pump acoustic dataset was systematically inspected to verify that the available recordings were correctly organized and suitable for further analysis.

The validation process included:

- Verifying the dataset directory structure.
- Identifying all available pump IDs.
- Checking the number of acoustic recordings associated with the pumps.
- Identifying the operating-condition labels.
- Counting recordings belonging to normal and abnormal operating conditions.
- Checking the consistency and integrity of the available recordings.
- Confirming that the recordings could be loaded successfully for subsequent signal processing.

This step was important because errors in the raw dataset structure, missing recordings, incorrect labels, or unreadable audio files could propagate into the feature engineering and machine learning stages.

---

### Dataset Summary

| Metric | Value |
|--------|------:|
| Pump IDs | **4** |
| Total Audio Recordings | **868** |
| Normal Recordings | **412** |
| Abnormal Recordings | **456** |

The dataset therefore contains acoustic observations from both normal and abnormal operating conditions, providing the labelled data required to investigate whether acoustic characteristics can be used to distinguish healthy and faulty pump operation.

---

### Validation Outcome

The development environment and raw dataset were successfully organized and validated before downstream processing.

At the end of this stage:

- The project had a structured and reproducible development environment.
- The complete set of **868 acoustic recordings** was identified.
- Normal and abnormal operating conditions were verified.
- The available pump IDs and dataset structure were confirmed.
- The recordings were confirmed to be suitable for acoustic signal inspection and feature extraction.

This established the data and engineering foundation for the next stage: **converting the raw acoustic signals into machine-learning-ready features**.

## ✅ 2. Acoustic Feature Engineering

The raw pump recordings contain acoustic signals in the form of time-series audio data. Machine learning models cannot directly use these raw audio signals efficiently as structured predictors, so the next stage was to transform the recordings into meaningful numerical characteristics that describe the acoustic behavior of the pumps.

The objective of this stage was to capture different aspects of the pump sound, including signal energy, temporal behavior, and frequency characteristics, and convert them into a structured feature matrix suitable for statistical analysis and machine learning.

<img width="1255" height="392" alt="waveform_sample_pump" src="https://github.com/user-attachments/assets/1e1d7ba0-4eac-430f-a34a-07471f8caa85" />

The waveform illustrates the amplitude variation of a representative pump
acoustic recording over time. This provides an initial view of the temporal
behavior of the recorded signal before numerical acoustic features are
extracted.

### Feature Extraction Pipeline

A reusable acoustic feature extraction pipeline was developed using **Librosa**. Each of the **868 audio recordings** was loaded and processed individually, and a fixed set of acoustic features was calculated for every recording.

The resulting feature representation contains:

- **5 time/frequency-domain acoustic features**
- **13 MFCC features**
- **18 numerical predictors in total**

This transformed the raw audio dataset into a structured tabular dataset that could be used in the subsequent EDA and machine learning stages.

---

### Extracted Acoustic Features

#### 1. Root Mean Square (RMS) Energy

RMS measures the average energy or amplitude of the acoustic signal.

It provides an indication of how strong the recorded pump sound is over time. Changes in vibration, mechanical activity, or abnormal operating conditions can alter the energy characteristics of the signal.

**Purpose:** Capture the overall energy level of the pump's acoustic signal.

---

#### 2. Zero Crossing Rate (ZCR)

Zero Crossing Rate measures how frequently the audio signal changes sign, or crosses the zero-amplitude axis.

It provides information about the temporal characteristics of the signal and can help distinguish signals with different levels of rapid oscillation or noisiness.

**Purpose:** Capture changes in the temporal characteristics of the acoustic signal.

---

#### 3. Spectral Centroid

Spectral Centroid represents the weighted mean frequency of the signal's frequency spectrum.

It can be interpreted as an indicator of where the majority of the signal's spectral energy is concentrated. Changes in pump operating conditions can result in shifts in this frequency distribution.

**Purpose:** Capture the overall spectral position or "center of mass" of the pump sound.

---

#### 4. Spectral Bandwidth

Spectral Bandwidth measures the spread of frequencies around the spectral centroid.

A narrow bandwidth indicates that the signal is concentrated around a smaller frequency range, while a wider bandwidth indicates a more dispersed frequency distribution.

**Purpose:** Capture the spread and variability of the pump's frequency content.

---

#### 5. Spectral Roll-off

Spectral Roll-off identifies the frequency below which a specified proportion of the total spectral energy is contained.

This feature helps describe the distribution of energy between lower and higher frequency components of the acoustic signal.

**Purpose:** Capture changes in the high-frequency characteristics of pump sound.

---

#### 6. Mel-Frequency Cepstral Coefficients (MFCCs)

Thirteen MFCCs were extracted from each recording.

MFCCs provide a compact representation of the spectral characteristics of an audio signal by representing its frequency structure on the Mel scale. They are widely used for characterizing audio patterns and were included here to capture additional information from the spectral shape of pump recordings.

The extracted coefficients were represented as:

```text
MFCC_1, MFCC_2, ..., MFCC_13
```
## Feature Summary

| Feature Group | Features                      | Number of Features |
| ------------- | ----------------------------- | -----------------: |
| Energy        | RMS                           |                  1 |
| Temporal      | ZCR                           |                  1 |
| Spectral      | Centroid, Bandwidth, Roll-off |                  3 |
| Cepstral      | MFCCs                         |                 13 |
| **Total**     |                               |             **18** |

<img width="1989" height="1769" alt="acoustic_feature_distributions" src="https://github.com/user-attachments/assets/d90f1b97-cb4d-4a49-a20d-a989e99402c0" />
The distributions show the statistical spread of the extracted acoustic
features across the 868 recordings. The features exhibit different ranges,
scales, and distribution shapes, which were examined before downstream
statistical analysis and machine learning.

## Processing Workflow

Each recording followed the same feature extraction procedure to maintain consistency across the dataset.

Raw Audio Recording
        │
        ▼
Load Audio Signal
        │
        ▼
Signal Processing
        │
        ├── RMS Energy
        ├── Zero Crossing Rate
        ├── Spectral Centroid
        ├── Spectral Bandwidth
        ├── Spectral Roll-off
        └── 13 MFCCs
        │
        ▼
18-Dimensional Feature Vector
        │
        ▼
Structured Feature Dataset

Applying the same extraction procedure to every recording ensures that the resulting feature vectors have a consistent structure and can be directly compared across operating conditions.

## Dataset Transformation
The feature extraction stage converted the original audio recordings into a tabular machine-learning dataset.

868 Raw Audio Recordings
          │
          ▼
Acoustic Feature Extraction
          │
          ▼
868 Samples × 18 Acoustic Features
          │
          ▼
Machine-Learning-Ready Dataset

The processed feature dataset was exported in CSV format for analysis and downstream machine learning workflows. A Pickle version was also saved to allow efficient loading of the processed data during subsequent experimentation.

## Outcome

The raw acoustic recordings were successfully transformed into a structured dataset containing 18 acoustic features per recording.

This feature representation provides multiple perspectives on pump acoustic behavior:

- Signal energy through RMS
- Temporal characteristics through ZCR
- Frequency distribution through spectral features
- Detailed spectral patterns through MFCCs

The resulting dataset forms the foundation for the next stage, Exploratory Data Analysis (EDA), where these features are statistically and visually examined to determine their relationship with normal and abnormal pump operating conditions.

## ✅ 3. Exploratory Data Analysis (EDA)

After converting the raw acoustic recordings into structured numerical features, Exploratory Data Analysis (EDA) was performed to understand the statistical behavior of the dataset and investigate whether the extracted acoustic characteristics differ between normal and abnormal pump operating conditions.

The primary objective of this stage was to understand the data before applying machine learning. This included assessing data quality, examining feature distributions, identifying potential outliers and redundancy, and studying the relationship between acoustic features and the target operating condition.

---

### 3.1 Dataset Structure & Quality Assessment

The processed feature dataset was first inspected to ensure that it was suitable for statistical analysis and subsequent machine learning.

The following checks were performed:

- Verified the number of observations and features.
- Inspected the data types of all variables.
- Identified the predictor variables and target label.
- Checked for missing values.
- Checked for duplicate observations.
- Examined the distribution of the target classes.
- Verified that the extracted acoustic features were stored in the expected numerical format.

These checks helped ensure that potential data-quality issues were identified before model development.

---

### 3.2 Descriptive Statistical Analysis

Descriptive statistics were generated for the extracted acoustic features to understand their numerical behavior.

For each feature, measures such as:

- Mean
- Standard deviation
- Minimum
- Maximum
- Quartiles

were examined.

This provided an initial understanding of the central tendency, variability, and range of the acoustic measurements across the recordings.

For example, features such as RMS represent signal energy, while spectral features and MFCCs describe different aspects of the frequency structure. Examining their statistical ranges helped identify differences in scale and variability that would later be considered during preprocessing.

---

### 3.3 Univariate Analysis

Each acoustic feature was analyzed independently to understand its individual distribution across the dataset.

#### Distribution Analysis

Histograms were generated to examine:

- The shape of each feature distribution.
- Concentration of observations.
- Possible skewness.
- Variation across recordings.
- Potential non-uniform distributions.

This helped determine whether certain acoustic features exhibited unusual or highly asymmetric distributions.

#### Outlier Analysis

Boxplots were used to examine the spread of the acoustic features and
identify observations that fall outside the typical distribution range.

The analysis examined whether individual recordings contained feature values substantially different from the majority of the dataset.

Potential outliers were treated as observations requiring investigation rather than automatically being removed, since unusual acoustic measurements may represent genuine changes in pump operating conditions.


#### Skewness Analysis

Feature skewness was evaluated to understand whether the distributions were approximately symmetric or strongly skewed.

This was particularly relevant for determining the statistical behavior of the extracted acoustic variables and informing subsequent preprocessing decisions.

---

### 3.4 Bivariate Analysis

The next stage examined relationships between individual acoustic features and the pump operating condition.

Each acoustic feature was compared across the two operating-condition
classes using feature-wise boxplots. This allowed the distribution,
central tendency, variability, and potential outliers of individual
features to be compared between the two classes.

### Acoustic Feature Comparison Across Pump Conditions

<img width="1872" height="2013" alt="features_by_condition" src="https://github.com/user-attachments/assets/0ce560d6-5931-4ac7-abc0-decb3583cc32" />

The feature-wise comparisons show differences in the distributions of
several acoustic characteristics between normal and abnormal operating
conditions. At the same time, overlap remains between the two classes,
indicating that no single acoustic feature is sufficient to reliably
separate the operating conditions. This supports the use of a multivariate
machine learning approach that combines information from multiple
acoustic characteristics.


The acoustic features were compared between:

- **Normal operating condition**
- **Abnormal operating condition**

Comparative visualizations were used to determine whether the distributions of individual features differed between the two classes.

### Analysis Performed

- Feature-wise comparison of normal and abnormal recordings.
- Comparative boxplots.
- Class distribution analysis.
- Comparison of average feature values between operating conditions.
- Examination of feature-level separation between the two target classes.

The purpose was not to assume that any individual feature could independently diagnose pump failure, but to determine whether the extracted acoustic measurements contained useful discriminatory information that could be combined by a machine learning model.

---

### 3.5 Target Class Analysis

The target variable was examined to understand the distribution of normal and abnormal observations.

The dataset contained:

| Operating Condition | Recordings |
|---|---:|
| Normal | **412** |
| Abnormal | **456** |
| **Total** | **868** |


<img width="541" height="470" alt="pump_condition_distribution" src="https://github.com/user-attachments/assets/63314d62-860f-492d-beb0-b9b89c42306d" />

The class distribution shows that the dataset contains observations from both
normal and abnormal operating conditions, with abnormal recordings
representing a slightly larger proportion of the dataset.

The class distribution was considered during subsequent model development
because differences in class frequency can influence classification model
behavior and evaluation.

---

### 3.6 Correlation Analysis

A correlation matrix was generated to investigate relationships between the acoustic features.

A heatmap was used to visualize the correlation structure across the feature set.

<img width="1479" height="1190" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/271e331d-3d73-4d1a-9619-04da7fab4635" />

The analysis helped identify:

- Strongly correlated acoustic features.
- Features containing potentially overlapping information.
- Relationships between spectral and cepstral characteristics.
- Potential feature redundancy.
- Groups of features with similar statistical behavior.

Understanding feature correlations is important because the feature set contains multiple measurements derived from related properties of the same acoustic signal.

However, correlated features were not automatically removed at this stage. Their usefulness was evaluated in the context of the machine learning models rather than relying solely on pairwise correlation.

---

### 3.7 Key EDA Findings

The exploratory analysis provided several important observations for the subsequent modeling stages:

1. The processed dataset was structurally suitable for machine learning after the data-quality checks.

2. The acoustic features exhibited different distributions, ranges, and levels of variability.

3. Several features showed differences between normal and abnormal pump recordings, indicating that acoustic characteristics contain potentially useful information about operating condition.

4. The feature correlation analysis revealed relationships between multiple acoustic variables, highlighting the need to consider feature redundancy during model interpretation.

5. The target classes were not perfectly balanced, which was taken into consideration during model development and preprocessing.

6. The combined acoustic feature set provided a reasonable basis for building a supervised classification model rather than relying on a single acoustic measurement.

---

### Outcome

EDA established a statistical understanding of the engineered acoustic dataset and provided evidence that the extracted features contain information relevant to distinguishing normal and abnormal pump operation.

The findings from this stage were then used to guide the **data preprocessing and machine learning pipeline**, including train-test splitting, feature scaling where required, and class-imbalance handling.


## ✅ 4. Data Preprocessing

Before training the machine learning models, the engineered acoustic dataset was prepared using a structured preprocessing workflow. The objective was to ensure that the models received clean and appropriately transformed input data while minimizing the risk of data leakage between training and evaluation sets.

This stage converted the EDA-ready dataset into a machine-learning-ready dataset for supervised classification.

---

### 4.1 Predictor and Target Separation

The processed dataset was divided into:

- **Predictor variables (`X`)** – the 18 extracted acoustic features.
- **Target variable (`y`)** – the pump operating condition indicating whether the recording belonged to the normal or abnormal class.

The target label was separated from the acoustic predictors before model training so that the models learned the relationship between the acoustic characteristics and the operating condition.

The predictor set consisted of:

```text
RMS
ZCR
Spectral Centroid
Spectral Bandwidth
Spectral Roll-off
MFCC_1
MFCC_2
...
MFCC_13
```
4.2 Train-Test Split

The dataset was divided into training and test subsets before model development.

A stratified split was used so that the relative representation of the normal and abnormal classes was maintained across the training and test datasets.

This is particularly important for classification problems because an uneven distribution of classes between the training and test sets can produce misleading performance estimates.

The test dataset was kept separate from model fitting and was used to evaluate how well the trained model performed on previously unseen observations.

4.3 Feature Scaling

The acoustic features have different numerical ranges and statistical distributions. Therefore, feature scaling was evaluated as part of the preprocessing workflow.

StandardScaler was used where required to standardize the numerical predictors.

Standardization transforms a feature approximately according to:

z = (x - μ) / σ

where:

x = original feature value
μ = mean of the feature calculated from the training data
σ = standard deviation calculated from the training data

This places the features on a comparable scale and prevents variables with larger numerical magnitudes from disproportionately influencing algorithms that are sensitive to feature scale.

Importantly, the scaler was fitted using the training data and then applied to the corresponding evaluation data rather than calculating scaling parameters using the complete dataset.

4.4 Class Imbalance Handling

The dataset contained different numbers of normal and abnormal recordings:

| Class    | Recordings |
| -------- | ---------: |
| Normal   |    **412** |
| Abnormal |    **456** |


Although the difference is not extreme, class distribution was explicitly considered during model development because predictive maintenance applications often place greater importance on correctly identifying abnormal or potentially failing equipment.

SMOTE (Synthetic Minority Over-sampling Technique) was incorporated into the training workflow to address class imbalance during model development.

SMOTE generates synthetic training observations for the minority class rather than simply duplicating existing observations.

This allows the classifier to receive a more balanced training signal while retaining the original test distribution for evaluation.

4.5 Preventing Data Leakage

Avoiding data leakage was an important part of the preprocessing design.

Information from the test set should not influence:

Feature scaling parameters
Synthetic sample generation
Model fitting
Hyperparameter selection

Therefore, preprocessing operations that learn from the data were performed using the training portion of the dataset.

The general workflow was:

Complete Dataset
       │
       ▼
Stratified Train-Test Split
       │
       ├──────────────────┐
       ▼                  ▼
   Training Set        Test Set
       │                  │
       ▼                  │
   Preprocessing           │
       │                  │
       ├── Scaling         │
       └── SMOTE           │
       │                  │
       ▼                  │
 Model Training            │
       │                  │
       └──────────┐        │
                  ▼        ▼
               Trained Model
                    │
                    ▼
              Test Evaluation

This separation helps ensure that the reported model performance reflects predictions on data that was not used to construct the training process.

4.6 Reproducibility

Randomized operations used during preprocessing and model development were controlled using fixed random states where appropriate.

This allows the workflow to be reproduced and makes it easier to compare different models and preprocessing configurations consistently.

The preprocessing stage was also integrated with the subsequent machine learning workflow so that the same transformation logic could be applied consistently during model training and evaluation.

Outcome

The acoustic feature dataset was converted into a structured machine-learning-ready format through:

Predictor-target separation
Stratified train-test splitting
Feature scaling where required
Class-imbalance handling using SMOTE
Leakage-aware preprocessing
Reproducible processing

The resulting training data was then used for baseline machine learning model development and comparative evaluation.


## ✅ 5. Baseline Machine Learning Models

After preprocessing the acoustic feature dataset, multiple supervised machine learning classification models were developed to determine whether the extracted acoustic characteristics could be used to distinguish between normal and abnormal pump operating conditions.

Rather than immediately selecting a single algorithm, several baseline models were trained and evaluated using the same underlying feature set. This provided a consistent basis for comparing their predictive behavior and identifying a suitable model for the subsequent predictive maintenance pipeline.

---

### 5.1 Classification Objective

The machine learning task was formulated as a **binary classification problem**.

Given the acoustic feature vector of a pump recording, the model predicts its operating condition:

```text
Acoustic Features
       │
       ▼
Machine Learning Model
       │
       ▼
Predicted Operating Condition
       │
       ├── Normal
       │
       └── Abnormal
```

The model predictions were later converted into failure probabilities, which became an important input to the risk analysis and maintenance optimization stages.

5.2 Baseline Models

Multiple classification algorithms were evaluated to establish baseline predictive performance.

The models considered included:

## Logistic Regression

Logistic Regression was used as a relatively simple linear baseline.

It provides a useful reference point for determining whether the acoustic features contain approximately linear relationships with the target class.

It also provides interpretable probability-based predictions that can be compared with more complex models.

## Decision Tree

A Decision Tree was evaluated to capture non-linear relationships and feature interactions.

Unlike a linear model, a decision tree can divide the feature space through a sequence of decision rules, allowing it to model more complex relationships between acoustic characteristics and pump operating conditions.

## Random Forest

Random Forest was evaluated as an ensemble tree-based approach.

It combines predictions from multiple decision trees and can capture non-linear relationships and interactions among the acoustic features.

This makes it particularly suitable for a feature set containing different types of acoustic measurements, including energy, temporal, spectral, and MFCC-based features.

5.3 Model Evaluation

The baseline models were evaluated using multiple classification metrics rather than relying only on accuracy.

The evaluation included:

- Precision
- Recall
- F1-Score
- ROC-AUC

Confusion matrices were also examined to understand the distribution
of correct and incorrect predictions across the normal and abnormal classes.

<img width="2184" height="623" alt="baseline_confusion_matrices" src="https://github.com/user-attachments/assets/eb5ca047-9f87-4d80-81e0-904f33a2a511" />

The confusion matrices provide a direct comparison of the classification
behavior of Logistic Regression, Decision Tree, and Random Forest across
normal and abnormal pump recordings.

These metrics provide different perspectives on model behavior.

# Precision

Precision measures the proportion of predicted abnormal recordings that were actually abnormal.

A higher precision means that fewer normal recordings are incorrectly flagged as abnormal.

# Recall

Recall measures the proportion of actual abnormal recordings that were successfully identified by the model.

Recall is particularly important in predictive maintenance because failing to identify an abnormal pump can result in an unexpected equipment failure.

# F1-Score

F1-score combines precision and recall into a single metric using their harmonic mean.

It provides a balanced measure when both false positives and false negatives are important.

# ROC-AUC
<img width="691" height="546" alt="roc_curve_comparison" src="https://github.com/user-attachments/assets/03bde317-c7a7-4427-b7d9-e78f850acd85" />

The ROC curves compare the ability of the three baseline models to
distinguish between normal and abnormal pump conditions across different
classification thresholds. The corresponding AUC values provide a
threshold-independent measure of discrimination performance.

ROC-AUC measures the model's ability to distinguish between the two operating conditions across different classification thresholds.

It was also useful because the eventual maintenance decision framework required probability-based risk assessment, rather than relying solely on a fixed class prediction.


5.4 Model Comparison

The models were evaluated using the same feature representation and preprocessing workflow to make the comparison meaningful.

The comparison focused on:

- Predictive performance
- Ability to identify abnormal conditions
- Generalization to unseen recordings
- Probability-based predictions
- Suitability for downstream predictive maintenance decisions

The baseline comparison identified Random Forest as the most suitable primary model for the subsequent stages of the project.

5.5 Why Random Forest Was Selected

Random Forest was selected because it provided a strong combination of predictive capability and suitability for the structure of the acoustic feature dataset.

The model can:

- Capture non-linear relationships between acoustic features and operating conditions.
- Model interactions between different acoustic characteristics.
- Handle heterogeneous feature types within the same feature space.
- Provide feature-level importance information.
- Produce probability estimates that can be used for downstream risk scoring.
- Serve as a suitable foundation for explainability using SHAP.

The model was therefore carried forward to the next stage for systematic hyperparameter optimization.

# Outcome

The baseline modeling stage established a comparative machine learning benchmark for pump operating-condition classification.

Multiple classification approaches were evaluated using precision, recall, F1-score, and ROC-AUC. Random Forest was selected as the primary predictive model, providing the foundation for the subsequent hyperparameter optimization, probability-based risk assessment, explainable AI, and maintenance decision framework.

## ✅ 6. Hyperparameter Optimization

After comparing the baseline classification models, **Random Forest** was selected as the primary predictive model. The next stage focused on improving its performance and controlling model complexity through systematic hyperparameter optimization.

The objective was to identify a Random Forest configuration that provides a strong balance between predictive performance and generalization on unseen pump recordings.

---

### 6.1 Why Hyperparameter Optimization?

A Random Forest model contains several hyperparameters that control how individual decision trees are constructed and how the ensemble behaves.

Examples include:

- Number of trees in the forest
- Maximum depth of individual trees
- Minimum number of samples required for a node split
- Minimum number of samples required at a leaf
- Number of features considered during each split

Using arbitrary parameter values may result in an underfitted or overfitted model.

Therefore, the model configuration was optimized systematically rather than relying only on default Random Forest settings.

---

### 6.2 GridSearchCV

**GridSearchCV** from Scikit-learn was used to evaluate different combinations of Random Forest hyperparameters.

A predefined parameter grid was constructed containing multiple candidate values for the selected hyperparameters.

The optimization process evaluated these combinations using cross-validation on the training data.

Conceptually, the process followed:

```text
Training Data
      │
      ▼
Candidate Hyperparameter Combinations
      │
      ▼
Cross-Validation
      │
      ├── Model Configuration 1
      ├── Model Configuration 2
      ├── Model Configuration 3
      ├── ...
      └── Model Configuration N
      │
      ▼
Compare Validation Performance
      │
      ▼
Select Best Configuration
      │
      ▼
Optimized Random Forest
```
This provides a more systematic approach to model tuning than manually selecting parameters.

6.3 Cross-Validation

Cross-validation was used during hyperparameter optimization to evaluate how consistently each candidate model configuration performed across different subsets of the training data.

Rather than relying on a single training-validation split, the training data was repeatedly divided into training and validation portions.

This helps reduce the influence of any particular split and provides a more robust estimate of model performance during the parameter-selection process.

The held-out test data remained separate from this optimization process and was reserved for final evaluation.

6.4 Optimization Objective

The hyperparameter search was designed to identify a configuration that provided strong classification performance while maintaining good generalization.

Model configurations were compared using the selected evaluation criterion from the cross-validation process.

The optimization considered the trade-off between:

- Predictive performance
- Model complexity
- Generalization
- Ability to distinguish abnormal pump conditions

The best-performing configuration was then used to construct the optimized Random Forest model.

6.5 Optimized Random Forest

The best hyperparameter configuration identified through GridSearchCV was used to train the optimized Random Forest classifier.

The optimized model was subsequently evaluated on the held-out test data.

This ensured that the final evaluation represented the model's performance on observations that were not used during hyperparameter selection.

The optimized model also generated failure probabilities for individual pump recordings. These probabilities became an important input to the later risk-scoring and economic decision framework.

6.6 Probability-Based Prediction

The default classification threshold was evaluated from a maintenance
perspective. Different probability thresholds were examined to understand
the trade-off between precision, recall, and F1-score.

<img width="846" height="546" alt="threshold_tradeoff" src="https://github.com/user-attachments/assets/6bf33656-2847-4dcc-a3a6-d0e05f784408" />

The figure shows how precision, recall, and F1-score change as the
classification threshold is varied. Increasing the threshold generally
reduces the number of pumps classified as abnormal, increasing precision
while reducing recall.

### Classification Performance at the Optimized Threshold

The selected operating threshold was then applied to the model predictions
to examine the resulting classification behavior.

<img width="541" height="454" alt="optimized_threshold_confusion_matrix" src="https://github.com/user-attachments/assets/4f8811e9-c2ea-48de-bf59-167d429cb42f" />

At the optimized threshold, the model correctly classified **80 normal
recordings and 76 failure recordings**, while producing **11 false
positives and 7 false negatives** in this evaluation.

The selected threshold was therefore determined based on the desired
balance between correctly identifying abnormal pumps and limiting
unnecessary maintenance alerts.

Instead of using only a binary prediction such as:
- Normal → 0
- Abnormal → 1
the optimized Random Forest was used to obtain a probability estimate for the abnormal/failure condition.

For example:
- Pump A → Failure Probability = 0.18
- Pump B → Failure Probability = 0.64
- Pump C → Failure Probability = 0.91

These probability estimates provide a more useful representation for predictive maintenance because pumps can be ranked according to their estimated risk rather than being treated simply as "failed" or "not failed."

The probability output was subsequently used in:

- Risk classification
- Maintenance prioritization
- Expected failure-loss calculation
- Economic modeling
- MILP-based maintenance optimization

6.7 Prediction Threshold Optimization

The default classification threshold was also evaluated from a maintenance perspective.

Instead of automatically treating a probability of 0.50 as the boundary between normal and abnormal conditions, different probability thresholds were considered to understand the trade-off between precision and recall.

The selected threshold was used to generate the final classification decisions for the predictive maintenance workflow.

This is important because the operational cost of missing a potentially failing pump can be substantially different from the cost of investigating a pump that turns out to be healthy.

# Outcome

The hyperparameter optimization stage produced an optimized Random Forest predictive model and established a probability-based prediction framework for the maintenance system.

The optimized model provides:

- Improved and systematically tuned predictive performance.
- Probability estimates for individual pump recordings.
- A configurable decision threshold.
- A model suitable for downstream risk and economic analysis.
- A foundation for explainable AI using SHAP.

The optimized model was then carried forward to the Explainable AI stage to understand which acoustic characteristics were driving its predictions.

## ✅ 7. Explainable AI (SHAP)

Machine learning models can provide accurate predictions while remaining difficult to interpret. For a predictive maintenance application, understanding **why a pump is assigned a higher failure probability** is important because maintenance decisions should not depend entirely on an unexplained model output.

To improve model transparency, **SHAP (SHapley Additive exPlanations)** was applied to the optimized Random Forest model.

The objective of this stage was to understand how individual acoustic features contribute to the model's predictions at both the overall dataset level and the individual pump level.

---

### 7.1 Why Explainability Was Required

The predictive model uses multiple acoustic characteristics simultaneously, including energy, temporal, spectral, and MFCC-based features.

A prediction such as:

```text
Pump ID → Failure Probability = 0.91
```

# Conceptually:

Acoustic Features
       │
       ▼
Optimized Random Forest
       │
       ▼
Failure Probability
       │
       ▼
SHAP Explanation
       │
       ├── Feature contribution
       ├── Direction of contribution
       └── Relative importance

This makes the model output easier to investigate and interpret.

7.2 SHAP Feature Importance

### Global SHAP Feature Importance
<img width="772" height="859" alt="shap_summary" src="https://github.com/user-attachments/assets/627b3662-4f01-48ad-82d3-4bd947496510" />

The SHAP summary plot provides a global view of the features that most
strongly influence the Random Forest predictions. Features are ranked
according to their overall contribution to the model output.

The horizontal position of each point represents the SHAP value, indicating
whether the corresponding feature value pushes the prediction toward a
higher or lower model output. The color represents the relative feature
value.
A global SHAP analysis was performed to understand which acoustic features had the greatest influence on the model across the dataset.

The analysis examined the magnitude of SHAP values associated with the different acoustic features.

Features with larger absolute SHAP values have a greater influence on the model's predictions, while features with smaller values generally have less influence.

This provides a model-specific measure of feature importance rather than relying only on simple statistical relationships such as correlation.

7.3 Direction of Feature Influence

SHAP analysis was also used to understand not only which features were important, but also how their values influenced predictions.

A feature can contribute towards:
- Higher predicted failure risk
             or
- Lower predicted failure risk

depending on its value and its interaction with the other features.

This distinction is important because a feature can be statistically related to the target without necessarily having a simple positive or negative relationship with the model's prediction.

7.4 SHAP Summary Analysis

A SHAP summary analysis was generated to provide a global view of model behavior.

The summary considers:

- Feature importance across observations.
- Distribution of feature contributions.
- Direction of contribution.
- Variation in feature influence across different recordings.

This allows the model to be interpreted at the dataset level rather than examining individual predictions independently.

7.5 Feature Interaction Analysis

### SHAP Dependence Analysis

Dependence plots were used to examine how individual acoustic feature
values influence their SHAP contribution to the model prediction.

<img width="1536" height="1024" alt="shap_top_feature_dependence" src="https://github.com/user-attachments/assets/309dc6d2-2a37-4ae6-b540-e34e70b9b102" />


The dependence plots illustrate the relationship between feature values and
their corresponding contribution to the model output. The patterns also
show that the influence of important acoustic features can be non-linear,
supporting the use of a non-linear ensemble model such as Random Forest.

Interactions between acoustic features were also investigated using SHAP.

This is useful because pump acoustic behavior is not necessarily determined by one measurement in isolation.

For example, the predictive contribution of one acoustic feature may change depending on the value of another feature.

The interaction analysis therefore provides additional insight into whether the model is relying on combinations of acoustic characteristics when assigning failure risk.

7.6 SHAP Dependence Analysis

SHAP dependence analysis was used to examine the relationship between individual feature values and their corresponding contribution to model predictions.

This helps investigate questions such as:

- How does increasing or decreasing a feature affect its contribution?
- Are there regions where the feature has a stronger influence?
- Does the relationship appear approximately linear or non-linear?
- Do interactions with other features affect the contribution?

This provides a more detailed interpretation than a simple feature-ranking plot.

7.7 Individual Prediction Interpretation

SHAP can also be used to explain individual pump predictions.

For a particular pump, the model's predicted failure probability can be examined together with the features that contributed most strongly to that prediction.

Conceptually:
Pump Acoustic Profile
          │
          ▼
  Failure Probability
          │
          ▼
   Individual SHAP
      Explanation
          │
          ├── Factors increasing risk
          └── Factors reducing risk

This creates a pathway for moving from:

"The model predicts high risk"

to:

"The model predicts high risk because of the combined contribution of specific acoustic characteristics."

7.8 From Prediction to Decision

SHAP was used primarily for model interpretation, while the actual maintenance decision was developed in subsequent stages.

The overall logic is:

Acoustic Recording
        │
        ▼
Feature Extraction
        │
        ▼
Random Forest
        │
        ▼
Failure Probability
        │
        ├──────────────► SHAP
        │                 │
        │                 ▼
        │          Model Explanation
        │
        ▼
Risk & Economic Analysis
        │
        ▼
Maintenance Optimization

This separation is important: SHAP explains the predictive model, while the later risk and optimization framework determines how those predictions can be converted into maintenance actions.

# Outcome

The Explainable AI stage provided a transparent view of the optimized Random Forest model by examining:

- Global feature importance.
- Individual feature contributions.
- Direction of feature influence.
- Feature interactions.
- Feature-value versus SHAP relationships.
- Individual prediction explanations.

SHAP therefore provided an interpretability layer between the machine learning prediction and the subsequent risk-based maintenance decision framework.

## ✅ 8. Predictive Maintenance & Risk Analysis

The machine learning model provides a failure probability for each pump recording. However, a predictive maintenance system requires more than simply classifying equipment as normal or abnormal.

The next stage therefore converts the model predictions into an actionable **risk and economic decision framework**.

The objective is to identify which pumps require greater maintenance attention by combining:

- Predicted failure probability
- Actual operating condition
- Failure-related economic impact
- Maintenance requirements
- Risk severity
- Expected economic benefit

This creates a bridge between the machine learning model and the subsequent optimization problem.

---

### 8.1 Failure Probability

The optimized Random Forest generates a probability estimate for the abnormal/failure condition for each pump.

Instead of representing the model output only as:

```text
Normal / Abnormal
```

each pump receives a continuous failure-risk estimate.
For example:
- Pump A → 0.18
- Pump B → 0.57
- Pump C → 0.91

A higher probability indicates that the model considers the pump more likely to exhibit the abnormal condition represented in the dataset.

These probability estimates form the primary predictive input to the risk-analysis stage.

8.2 Risk Classification

The predicted failure probabilities were converted into risk categories to make the model output easier to interpret from a maintenance perspective.

Pumps were categorized according to their estimated level of failure risk.

This allows the maintenance system to distinguish between pumps requiring relatively low attention and pumps that may require more immediate investigation or intervention.

The risk classification provides a practical layer between the continuous machine learning probability and the eventual maintenance decision.

8.3 Maintenance Priority

Failure probability alone does not necessarily determine the best maintenance action.

For example, two pumps may have similar failure probabilities but very different consequences if they fail.

Therefore, maintenance prioritization considers both:

Probability of Failure
          +
Potential Failure Impact
          │
          ▼
      Maintenance Priority

A priority framework was developed to rank pumps according to their maintenance relevance.

This allows the system to move beyond a simple probability ranking and incorporate the potential operational and economic consequences associated with equipment failure.

8.4 Expected Failure Loss

The predicted failure probability was combined with the estimated failure cost to calculate the Expected Failure Loss for each pump.

Conceptually:
Expected Failure Loss = Failure Probability × Failure Cost

For example, a pump with a high probability of failure and a high failure cost will have a substantially greater expected loss than a pump with the same probability but a lower failure consequence.

8.5 Maintenance Cost

The economic model also incorporates the cost associated with performing maintenance.

Maintenance cost may depend on the resources required to intervene on a particular pump.

The framework therefore distinguishes between:

Potential Loss from Not Maintaining
                  │
                  ▼
          Expected Failure Loss

                  versus

          Cost of Intervention
                  │
                  ▼
            Maintenance Cost

This comparison is necessary because a high-risk pump is not automatically the optimal maintenance candidate if the intervention requires disproportionate resources.

8.6 Expected Net Benefit

The expected economic benefit of maintenance was calculated by comparing the expected failure loss with the corresponding maintenance cost.

The project uses:

Expected Net Benefit = Expected Failure Loss − Maintenance Cost

A positive expected net benefit indicates that, under the model assumptions, the expected avoided failure loss is greater than the estimated maintenance cost.

This provides an economic basis for prioritizing maintenance interventions.

8.7 Benefit per Maintenance Hour

Maintenance resources are constrained not only by cost but also by available workforce and equipment capacity.

Therefore, the framework also calculates the economic benefit generated per maintenance hour.

Conceptually:
Benefit per Hour = Expected Net Benefit ÷ Maintenance Hours

This metric helps compare maintenance candidates when available maintenance time is limited.

For example, two pumps may both have positive expected benefits, but the pump generating greater expected benefit per maintenance hour may provide better utilization of a constrained maintenance workforce.

8.8 Maintenance Decision Framework

The complete risk and economic framework can therefore be represented as:
Failure Probability
        │
        ▼
   Risk Assessment
        │
        ▼
   Failure Cost
        │
        ▼
Expected Failure Loss
        │
        ├──────────────┐
        │              │
        ▼              ▼
Maintenance Cost   Maintenance Hours
        │              │
        └──────┬───────┘
               ▼
      Expected Net Benefit
               │
               ▼
       Maintenance Priority

This framework transforms a machine learning prediction into a measurable maintenance decision criterion.

8.9 Pump-Level Decision Dataset

The outputs of the predictive and economic analysis were consolidated into a pump-level decision dataset.

The resulting dataset contains information such as:

- Pump ID
- Acoustic features
- Actual operating condition
- Failure probability
- Predicted operating condition
- Risk level
- Maintenance hours
- Failure cost
- Maintenance cost
- Expected failure loss
- Expected net benefit
- Benefit per maintenance hour
- Maintenance decision

This consolidated dataset acts as the input to the optimization stage.

# Outcome

The predictive maintenance stage transformed the Random Forest's failure probabilities into an actionable risk and economic framework.

The system can now evaluate each pump based on:

Likelihood of failure → Risk → Economic exposure → Maintenance cost → Expected benefit → Maintenance priority

This creates the decision layer required for the next stage, where Mixed-Integer Linear Programming (MILP) is used to select an optimal maintenance portfolio under limited maintenance capacity.

## ✅ 9. MILP-Based Maintenance Optimization

The predictive maintenance framework generates failure probabilities, risk levels, expected failure losses, maintenance costs, and maintenance requirements for individual pumps. However, maintenance planning is subject to practical resource constraints.

A maintenance team cannot necessarily service every high-risk pump at the same time because available maintenance hours, workforce, and other resources are limited.

To address this problem, a **Mixed-Integer Linear Programming (MILP)** optimization model was developed to determine which pumps should be selected for maintenance while considering both operational risk and economic benefit.

The objective was to move from:

> **"Which pumps are risky?"**

to:

> **"Which combination of pumps should be maintained given limited maintenance resources?"**

---

### 9.1 Why Optimization Was Required

A simple risk-ranking approach would sort pumps by failure probability and select the highest-risk pumps until the maintenance capacity is reached.

However, failure probability alone does not account for:

- Different consequences of pump failure.
- Different maintenance costs.
- Different maintenance durations.
- Economic benefit of intervention.
- Risk constraints.
- Limited maintenance capacity.

Therefore, the project formulated maintenance planning as a constrained optimization problem.

The decision process becomes:

```text
Machine Learning
      │
      ▼
Failure Probability
      │
      ▼
Risk & Economic Analysis
      │
      ▼
MILP Optimization
      │
      ├── Risk
      ├── Failure Loss
      ├── Maintenance Cost
      ├── Maintenance Hours
      └── Capacity Constraints
      │
      ▼
Optimized Maintenance Portfolio
```
9.2 Decision Variable

A binary decision variable was defined for each pump.
- xᵢ = 1  → Pump i is selected for maintenance
- xᵢ = 0  → Pump i is not selected

This binary formulation reflects the real maintenance decision: a pump is either included in the current maintenance plan or it is not.

9.3 Maintenance Capacity Constraint

The maintenance team has a limited number of available maintenance hours.

The optimization therefore constrains the total maintenance time of the selected pumps.

Conceptually:
Σ Maintenance_Hoursᵢ × xᵢ ≤ Available_Maintenance_Hours

For the current project scenario:
| Capacity Metric             |         Value |
| --------------------------- | ------------: |
| Available Maintenance Hours | **148 hours** |
| Optimized Maintenance Hours | **148 hours** |
| Capacity Utilization        |      **100%** |

The resulting solution uses the available maintenance capacity fully.

9.4 Risk Constraint

The optimization framework also incorporates a risk-based selection criterion.

A risk threshold, represented by α = 0.60, was used to identify the pool of pumps meeting the specified failure-risk criterion.

For the current scenario:
| Risk Metric                  |     Result |
| ---------------------------- | ---------: |
| Risk Threshold (α)           |   **0.60** |
| Pumps Meeting Risk Threshold |     **68** |
| Pumps Selected by MILP       |     **37** |
| Risk-Threshold Coverage      | **54.41%** |

This ensures that the optimization does not treat all pumps identically and focuses the maintenance portfolio on pumps meeting the defined risk criterion.

9.5 Economic Objective

The optimization considers the economic consequences associated with pump failure and maintenance.

For each pump, the framework estimates:

Expected Failure Loss
=
Failure Probability × Failure Cost

and:
Expected Net Benefit
=
Expected Failure Loss − Maintenance Cost

These quantities provide an economic basis for deciding which maintenance interventions are more valuable.

The optimization therefore seeks a maintenance portfolio that provides a strong expected economic return while satisfying the operational constraints.

9.6 Maintenance Portfolio Selection

The MILP model evaluates the available pump candidates simultaneously rather than making an independent decision for each pump.

The resulting solution identifies a portfolio of pumps that can be maintained within the available maintenance capacity.

For the current optimization scenario:

| Metric                    | MILP Result |
| ------------------------- | ----------: |
| Total Pumps Evaluated     |     **174** |
| Pumps Selected            |      **37** |
| Maintenance Hours         |     **148** |
| Capacity Utilization      |    **100%** |
| Actual Failures Available |      **83** |
| Actual Failures Covered   |      **36** |
| Actual Failure Coverage   |  **43.37%** |

The selected portfolio therefore represents a constrained maintenance plan rather than simply the top 37 pumps according to one individual ranking criterion.

9.7 Economic Performance

The optimized maintenance portfolio was evaluated using the economic framework developed in the previous stage.

For the selected portfolio:

| Economic Metric       |           Result |
| --------------------- | ---------------: |
| Expected Failure Loss |  **₹33.54 lakh** |
| Maintenance Cost      |   **₹2.96 lakh** |
| Expected Net Benefit  |  **₹30.58 lakh** |
| Net Benefit per Hour  | **₹20,662/hour** |

The expected net benefit is calculated as:
₹33.54 lakh − ₹2.96 lakh
=
₹30.58 lakh

This represents the model-estimated economic benefit of the selected maintenance portfolio under the project's assumptions. It should not be interpreted as realized or guaranteed financial savings.

9.8 Strategy Comparison

The MILP solution was compared with alternative maintenance selection approaches to understand the value of incorporating optimization into the decision process.

The strategies considered were:

- ML Risk Ranking
  Select pumps primarily according to their predicted failure risk.
- Economic Ranking
  Prioritize pumps according to their expected economic benefit.
- Risk-Constrained MILP
  Select the maintenance portfolio while simultaneously considering risk, economic value,   maintenance requirements, and capacity constraints.

The current comparison is:

| Strategy                  | Pumps Selected | Maintenance Hours | Actual Failures Covered | Failure Coverage | Expected Net Benefit | Net Benefit / Hour |
| ------------------------- | -------------: | ----------------: | ----------------------: | ---------------: | -------------------: | -----------------: |
| ML Risk Ranking           |             37 |               124 |                      37 |           44.58% |          ₹19.32 lakh |            ₹15,579 |
| Economic Ranking          |             32 |               148 |                      32 |           38.55% |          ₹17.67 lakh |            ₹11,936 |
| **Risk-Constrained MILP** |         **37** |           **148** |                  **36** |       **43.37%** |      **₹30.58 lakh** |        **₹20,662** |

The comparison demonstrates that the MILP framework provides a substantially higher model-estimated expected net benefit under the current economic assumptions.

The MILP solution does not necessarily maximize every individual metric. For example, the ML risk-ranking strategy covers slightly more observed failures in this evaluation. Instead, the purpose of MILP is to optimize the overall maintenance decision under multiple constraints and objectives.

9.9 Optimization Workflow

The complete optimization process can be summarized as:

Pump Acoustic Recordings
          │
          ▼
Acoustic Feature Extraction
          │
          ▼
Random Forest Prediction
          │
          ▼
Failure Probability
          │
          ▼
Risk Assessment
          │
          ▼
Failure Cost + Maintenance Cost
          │
          ▼
Expected Failure Loss
          │
          ▼
Expected Net Benefit
          │
          ▼
Maintenance Hours & Risk Constraints
          │
          ▼
        MILP Model
          │
          ▼
Optimal Maintenance Portfolio
          │
          ▼
Economic & Operational Evaluation

9.10 Decision-Support Interpretation

The key advantage of the MILP framework is that it changes the role of machine learning predictions.

The Random Forest does not directly decide which pump should be maintained.

Instead:

Machine Learning
      ↓
Predicts Failure Risk

Risk & Economic Model
      ↓
Quantifies Consequences

MILP Optimization
      ↓
Selects Maintenance Portfolio

This creates a separation between prediction and decision-making.

The machine learning model estimates what may happen, while the optimization model determines what action should be taken given the available resources and project constraints.

Outcome

The MILP stage transformed individual pump-level predictions into an optimized maintenance portfolio.

For the current scenario, the model selected:

37 pumps using 148 available maintenance hours, producing a model-estimated ₹30.58 lakh expected net benefit and 43.37% coverage of observed failures.

The resulting portfolio provides the final decision output of the analytical pipeline and serves as the primary dataset for the interactive Streamlit decision-support dashboard.
