import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Sayfa ayarları
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Başlık
st.title("📊 Customer Churn Prediction")
st.markdown("""
This application predicts whether a telecom customer is likely to churn.

### Instructions
- Enter the customer information from the left sidebar.
- Click **Predict Churn**.
- The model will display the prediction, churn probability and risk level.
""")

st.divider()
# Model ve feature listesi
model = joblib.load("models/churn_model.joblib")
feature_columns = joblib.load("models/feature_columns.pkl")
st.sidebar.header("Müşteri Bilgileri")

gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)

SeniorCitizen = st.sidebar.selectbox(
    "Senior Citizen",
    [0, 1]
)

Partner = st.sidebar.selectbox(
    "Partner",
    ["No", "Yes"]
)

Dependents = st.sidebar.selectbox(
    "Dependents",
    ["No", "Yes"]
)

tenure = st.sidebar.slider(
    "Tenure (Month)",
    0,
    72,
    12
)

PhoneService = st.sidebar.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

MultipleLines = st.sidebar.selectbox(
    "Multiple Lines",
    [
        "No",
        "Yes",
        "No phone service"
    ]
)

InternetService = st.sidebar.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

OnlineSecurity = st.sidebar.selectbox(
    "Online Security",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

OnlineBackup = st.sidebar.selectbox(
    "Online Backup",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

DeviceProtection = st.sidebar.selectbox(
    "Device Protection",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

TechSupport = st.sidebar.selectbox(
    "Tech Support",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

StreamingTV = st.sidebar.selectbox(
    "Streaming TV",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

StreamingMovies = st.sidebar.selectbox(
    "Streaming Movies",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

Contract = st.sidebar.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

PaperlessBilling = st.sidebar.selectbox(
    "Paperless Billing",
    [
        "No",
        "Yes"
    ]
)

PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.sidebar.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.sidebar.number_input(
    
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)
st.sidebar.markdown("---")

st.sidebar.info("""
### Model Information

Model : Random Forest

Dataset : IBM Telco Customer Churn

Developer : Muhammed Beraa Erdem
""")
input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [SeniorCitizen],
    "Partner": [Partner],
    "Dependents": [Dependents],
    "tenure": [tenure],
    "PhoneService": [PhoneService],
    "MultipleLines": [MultipleLines],
    "InternetService": [InternetService],
    "OnlineSecurity": [OnlineSecurity],
    "OnlineBackup": [OnlineBackup],
    "DeviceProtection": [DeviceProtection],
    "TechSupport": [TechSupport],
    "StreamingTV": [StreamingTV],
    "StreamingMovies": [StreamingMovies],
    "Contract": [Contract],
    "PaperlessBilling": [PaperlessBilling],
    "PaymentMethod": [PaymentMethod],
    "MonthlyCharges": [MonthlyCharges],
    "TotalCharges": [TotalCharges]
})
# One-Hot Encoding
input_encoded = pd.get_dummies(input_data)

# Eksik sütunları ekle
for col in feature_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

# Fazla sütunları kaldır
input_encoded = input_encoded[feature_columns]
if st.button("Predict Churn"):

    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0][1]

    st.divider()

    st.subheader("Prediction Result")

    st.dataframe(input_data, use_container_width=True)


    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

    st.metric(
        
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(int(probability * 100))

    if probability < 0.30:
        st.success("🟢 Risk Level: Low")

    elif probability < 0.70:
        st.warning("🟡 Risk Level: Medium")

    else:
        st.error("🔴 Risk Level: High")
        st.divider()

st.subheader("Customer Information")

st.dataframe(
    input_data,
    use_container_width=True
)
st.markdown("---")

st.caption(
    "Customer Churn Prediction System | Built with Streamlit & Random Forest"
)
        