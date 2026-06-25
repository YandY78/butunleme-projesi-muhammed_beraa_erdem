# Customer Churn Prediction

## Project Description

This project predicts whether a telecom customer is likely to churn using a Machine Learning model.

A Random Forest classifier was trained on the IBM Telco Customer Churn dataset and deployed with Streamlit to provide an interactive web application.

---

## Features

- Customer information input
- Churn prediction
- Churn probability
- Risk level visualization
- Customer information summary
- Interactive Streamlit interface

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## Dataset

IBM Telco Customer Churn Dataset

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app/app.py
```

---

## Machine Learning Model

- Algorithm: Random Forest Classifier
- Task: Binary Classification
- Target Variable: Churn

---

## Project Structure

```
Customer-Churn-Prediction/
│
├── app/
│   └── app.py
│
├── models/
│   ├── churn_model.joblib
│   └── feature_columns.pkl
│
├── notebooks/
│   └── 01_Data_Exploration.ipynb
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Developer

Muhammed Beraa Erdem