# Alzheimer Detection Web Application

This project is a web application designed to detect Alzheimer’s disease through data visualization and prediction using machine learning. The app is built with [Streamlit](https://streamlit.io/) and provides insights into Alzheimer-related parameters and demographic statistics.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data](#data)
6. [Technologies Used](#technologies-used)
7. [License](#license)

## Overview
Alzheimer's disease impacts memory, thinking, and social abilities. This app provides visual data analysis and a prediction model based on various parameters related to Alzheimer’s. It also includes a detailed look into the scientific and statistical aspects of Alzheimer’s disease.

## Features
The application has the following sections:
- **Introduction**: Overview of Alzheimer's disease and important predictive parameters (MMSE, SES, eTIV, nWBV, ASF).
- **Statistics**: Provides visual insights into Alzheimer’s demographics by gender, age, and key parameters.
- **Prediction**: Allows users to input relevant parameters and predict Alzheimer status based on a pre-trained model.
- **About Us**: General information about the project and contributors.

### Key Parameters:
- **MMSE**: Mini Mental State Examination
- **SES**: Social Economic Status
- **eTIV**: Estimated Total Intracranial Volume
- **nWBV**: Normalized Whole Brain Volume
- **ASF**: Atlas Scaling Factor

## Installation

### Prerequisites
- [Python 3.7+](https://www.python.org/downloads/)
- Required libraries in `requirements.txt`

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/spark1810/alzheimer-detection.git
    cd alzheimer-detection
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the Dataset**:
   - Place the `oasis_longitudinal.csv` file in the root directory of the project.

4. **Run the App**:
    ```bash
    streamlit run app.py
    ```

## Usage
After launching the app, select the sections in the sidebar to navigate between **Introduction**, **Statistics**, **Prediction**, and **About Us**.

### Prediction Section
Input values for parameters like gender, age, MMSE, SES, eTIV, nWBV, and ASF to get an estimation of the Alzheimer status.

### Visualization in Statistics Section
- Visualize distributions of key features (e.g., **Gender**, **MMSE**, **ASF**, **ETIV**, **nWBV**, **Age**, **Education**).
- Scatter plots and histograms provide insights into patterns and trends in Alzheimer’s data.

## Data
The dataset used is [OASIS Longitudinal](https://www.oasis-brains.org/) dataset. It includes longitudinal data of Alzheimer's patients and healthy individuals.

## Technologies Used
- **Streamlit** for the web interface
- **Pandas** for data manipulation
- **Seaborn** and **Matplotlib** for data visualization
- **Scikit-learn** for machine learning model training
- **Numpy** for numerical operations

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the OASIS Brain project for making the Alzheimer dataset available.
