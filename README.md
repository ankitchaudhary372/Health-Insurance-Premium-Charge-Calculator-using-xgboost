# Health-Insurance-Premium-Charge-Calculator-using-xgboost
# 🏥 Insurance Cost Prediction App

A Machine Learning web application built with **Python, Scikit-Learn, XGBoost, and Streamlit** to predict insurance costs based on customer demographics, lifestyle, and medical history.

## 📌 Project Overview

This project predicts the estimated insurance cost using various customer attributes such as:

* Age
* Gender
* BMI
* Number of Children
* Smoking Status
* Region
* Medical History
* Family Medical History
* Exercise Frequency
* Occupation
* Coverage Level

The application is deployed using **Streamlit** and allows users to get real-time insurance cost predictions through an interactive web interface.

---

## 🚀 Features

* Interactive Streamlit Dashboard
* Real-time Insurance Cost Prediction
* Data Preprocessing using Scikit-Learn Pipeline
* One-Hot Encoding for Categorical Features
* Feature Scaling using StandardScaler
* XGBoost Regression Model
* Model Serialization using Joblib
* Clean and User-Friendly Interface

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

## 📂 Project Structure

```text
Insurance-Cost-Prediction/
│
├── app.py
├── insurance_prediction.pkl
├── insurance_dataset.csv
├── requirements.txt
├── README.md
└── notebooks/
```

---

## 📊 Machine Learning Workflow

1. Data Cleaning
2. Feature Engineering
3. Train-Test Split
4. Data Preprocessing

   * OneHotEncoder
   * StandardScaler
5. Model Training using XGBoost Regressor
6. Hyperparameter Tuning
7. Model Evaluation
8. Deployment using Streamlit

---

## 📈 Model Performance

| Metric   | Score |
| -------- | ----- |
| R² Score | 0.835 |
| MAE      | 3812  |

The model explains approximately **83.5% of the variance** in insurance costs.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Insurance-Cost-Prediction.git
```

Move into the project directory:

```bash
cd Insurance-Cost-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🖥️ Application Inputs

* Age
* Gender
* BMI
* Number of Children
* Smoking Status
* Region
* Medical History
* Family Medical History
* Exercise Frequency
* Occupation
* Coverage Level

---

## 🎯 Future Improvements

* CatBoost and LightGBM Comparison
* Model Explainability using SHAP
* Docker Deployment
* Cloud Deployment (AWS/Azure/GCP)
* Advanced Feature Engineering

---

## 👨‍💻 Author

**Ankit Kumar**

Data Analyst | Machine Learning Enthusiast

### Skills

* Python
* SQL
* Power BI
* Excel
* Machine Learning
* Data Analysis

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
