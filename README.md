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
