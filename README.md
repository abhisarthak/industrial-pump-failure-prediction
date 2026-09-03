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

Boxplots were used to identify potential extreme observations.

The analysis examined whether individual recordings contained feature values substantially different from the majority of the dataset.

Potential outliers were treated as observations requiring investigation rather than automatically being removed, since unusual acoustic measurements may represent genuine changes in pump operating conditions.

#### Skewness Analysis

Feature skewness was evaluated to understand whether the distributions were approximately symmetric or strongly skewed.

This was particularly relevant for determining the statistical behavior of the extracted acoustic variables and informing subsequent preprocessing decisions.

---

### 3.4 Bivariate Analysis

The next stage examined relationships between individual acoustic features and the pump operating condition.

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

The class distribution was considered during subsequent model development because differences in class frequency can influence the behavior of classification algorithms and evaluation metrics.

This analysis subsequently motivated the use of appropriate preprocessing and class-imbalance handling during the machine learning stage.

---

### 3.6 Correlation Analysis

A correlation matrix was generated to investigate relationships between the acoustic features.

A heatmap was used to visualize the correlation structure across the feature set.

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

Class	Recordings
Normal	412
Abnormal	456

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
