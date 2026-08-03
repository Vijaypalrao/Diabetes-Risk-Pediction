# Diabetes-Risk-Pediction
End-to-end Machine Learning project for Diabetes Risk Prediction with Streamlit deployment
#  Diabetes Risk Prediction using Machine Learning
website link: https://diabetes-risk-pediction-1405.streamlit.app/

## Overview

This project develops a Machine Learning-based Diabetes Risk Prediction System using clinical symptoms and demographic information. Multiple classification models were trained and evaluated to identify the best-performing model for predicting diabetes risk.

The final model is deployed using Streamlit, allowing users to enter patient information and receive an instant diabetes risk prediction.

---

## Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Feature Encoding
- Feature Selection using SHAP
- Model Training and Evaluation
- Model Comparison
- Explainable AI (SHAP)
- Streamlit Web Application
- New Patient Prediction

---

## Machine Learning Models

- Logistic Regression
- XGBoost
- Random Forest
- LightGBM

**Final Selected Model:** Random Forest

---

## Input Features

The deployed model uses the top 10 most important features selected through SHAP:

- Age
- Gender
- Polyuria
- Polydipsia
- Sudden Weight Loss
- Partial Paresis
- Itching
- Irritability
- Polyphagia
- Alopecia

---

## Prediction Output

The application provides:

- Diabetes Status (Positive / Negative)
- Probability of Diabetes
- Risk Category

---

## Project Structure

```
Diabetes-Risk-Prediction/
│
├── app.py
├── Final_Diabetes_RF_Model.pkl
├── Selected_Features.pkl
├── requirements.txt
├── README.md
└── Diabetes_Risk_Prediction.ipynb
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- SHAP
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/Diabetes-Risk-Prediction.git
```

Move into the project directory

```bash
cd Diabetes-Risk-Prediction
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## Deployment

The application can be deployed using **Streamlit Community Cloud**.

Steps:

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py`.
5. Deploy the application.

---

## Future Improvements

- Hyperparameter Tuning
- External Dataset Validation
- Integration with Clinical Data
- Cloud Deployment
- Mobile-Friendly Interface

---



---


M.Sc. Statistics  
University of Delhi
