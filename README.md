# 🏭 Predictive Maintenance AI

AI-Powered Machine Failure Prediction System built using Machine Learning and Streamlit.

## 📌 Project Overview

Predictive Maintenance AI is an industrial machine monitoring and failure prediction system that helps identify potential machine failures before breakdowns occur.

The system analyzes machine sensor data and predicts machine health using an XGBoost Machine Learning model.

This solution helps industries:

* Reduce downtime
* Improve operational efficiency
* Schedule maintenance proactively
* Prevent unexpected machine failures

---

## 🚀 Features

### 📊 Machine Analytics

* Failure Distribution Analysis
* Machine Type Analysis
* Temperature Analysis
* RPM Analysis
* Torque Analysis
* Tool Wear Analysis

### 🤖 Failure Prediction

* Real-time Machine Failure Prediction
* Failure Probability Calculation
* Machine Health Score
* Risk Assessment
* Maintenance Recommendations

### 🚨 Live Monitoring

* Live Sensor Dashboard
* RPM Monitoring
* Torque Monitoring
* Tool Wear Tracking
* Machine Status Monitoring

### 📈 Model Performance

* Model Comparison
* Accuracy Analysis
* Feature Importance
* Performance Metrics

---

## ⚙️ Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Deployment

---

## 🧠 Model Used

### XGBoost Classifier

Performance:

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 98.8% |
| Precision | 91%   |
| Recall    | 72%   |
| F1 Score  | 80%   |

---

## 📂 Project Structure

```text
Predictive-Maintenance-System/
│
├── assets/
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Machine_Analytics.py
│   ├── 3_Failure_Prediction.py
│   ├── 4_Live_Monitoring.py
│   └── 5_Model_Performance.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Plotly
* Joblib

### Framework

* Streamlit

---

## 📊 Dataset

Dataset Used:

AI4I 2020 Predictive Maintenance Dataset

Features:

* Type
* Air Temperature
* Process Temperature
* Rotational Speed
* Torque
* Tool Wear

Target:

* Machine Failure

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

* IoT Sensor Integration
* Real-Time Data Streaming
* Cloud Deployment
* Automated Maintenance Alerts
* Email Notifications

---

## 👨‍💻 Developed By

Aman Saini

B.Tech Computer Science Engineering

Machine Learning & AI Enthusiast
