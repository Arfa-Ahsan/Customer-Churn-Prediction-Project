# -*- coding: utf-8 -*-
"""
@author: pt
"""

import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model_path = 'C:/Users/pt/logistics_regression_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Define the original columns used during model training
original_columns = [
    'tenure', 'monthlycharges', 'totalcharges', 'contract_One year', 'contract_Two year',
    'gender_Male', 'internetservice_Fiber optic', 'internetservice_No',
    'onlinebackup_No internet service', 'onlinebackup_Yes',
    'onlinesecurity_No internet service', 'onlinesecurity_Yes',
    'paperlessbilling_Yes', 'paymentmethod_Credit card (automatic)',
    'paymentmethod_Electronic check', 'paymentmethod_Mailed check'
]

# Define the values for the select boxes
gender_options = {0: 'Female', 1: 'Male'}
internetservice_options = {0: 'DSL', 1: 'Fiber optic', 2: 'No'}
onlinesecurity_options = {0: 'No', 1: 'Yes', 2: 'No internet service'}
onlinebackup_options = {0: 'No', 1: 'Yes', 2: 'No internet service'}
contract_options = {0: 'Month-to-month', 1: 'One year', 2: 'Two year'}
paymentmethod_options = {
    0: 'Bank transfer (automatic)', 1: 'Credit card (automatic)',
    2: 'Electronic check', 3: 'Mailed check'
}

def churn_prediction(input_data):
    # Convert the input data to a DataFrame and ensure it has the same columns as the model was trained on
    input_df = pd.DataFrame([input_data]).reindex(columns=original_columns, fill_value=0)
    
    # Predict the churn and the probability
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[:, 1][0]
    
    return prediction, probability

# Create the Streamlit app
def main():
    st.markdown('<h1 style="color: #FFF;">Customer Churn Prediction App</h1>', unsafe_allow_html=True)
    st.markdown("## Customer Details :")
    st.write("<b font-size:14px>Enter the following details of the customer to predict if a customer will churn or not</b>", unsafe_allow_html=True)

    # Create input fields for user input
    gender = st.selectbox("Gender", options=list(gender_options.keys()), format_func=lambda x: gender_options[x])
    tenure = st.slider("Tenure (months)", 0, 100, 1)
    internetservice = st.selectbox("Internet Service", options=list(internetservice_options.keys()), format_func=lambda x: internetservice_options[x])
    onlinesecurity = st.selectbox("Online Security", options=list(onlinesecurity_options.keys()), format_func=lambda x: onlinesecurity_options[x])
    onlinebackup = st.selectbox("Online Backup", options=list(onlinebackup_options.keys()), format_func=lambda x: onlinebackup_options[x])
    contract = st.selectbox("Contract", options=list(contract_options.keys()), format_func=lambda x: contract_options[x])
    paymentmethod = st.selectbox("Payment Method", options=list(paymentmethod_options.keys()), format_func=lambda x: paymentmethod_options[x])
    monthlycharges = st.number_input("Monthly Charges", min_value=0.0)
    totalcharges = st.number_input("Total Charges", min_value=0.0)
    paperlessbilling = st.selectbox("Paperless Billing", options={0: 'No', 1: 'Yes'}.keys(), format_func=lambda x: {0: 'No', 1: 'Yes'}[x])

    # One-hot encode the input data
    input_data = {
        'tenure': tenure,
        'monthlycharges': monthlycharges,
        'totalcharges': totalcharges,
        'contract_One year': 1 if contract == 1 else 0,
        'contract_Two year': 1 if contract == 2 else 0,
        'gender_Male': gender,
        'internetservice_Fiber optic': 1 if internetservice == 1 else 0,
        'internetservice_No': 1 if internetservice == 2 else 0,
        'onlinebackup_No internet service': 1 if onlinebackup == 2 else 0,
        'onlinebackup_Yes': 1 if onlinebackup == 1 else 0,
        'onlinesecurity_No internet service': 1 if onlinesecurity == 2 else 0,
        'onlinesecurity_Yes': 1 if onlinesecurity == 1 else 0,
        'paperlessbilling_Yes': paperlessbilling,
        'paymentmethod_Credit card (automatic)': 1 if paymentmethod == 1 else 0,
        'paymentmethod_Electronic check': 1 if paymentmethod == 2 else 0,
        'paymentmethod_Mailed check': 1 if paymentmethod == 3 else 0,
    }

    # Predict churn based on user input
    if st.button("Predict"):
        churn_prediction_result, churn_probability = churn_prediction(input_data)

        # Display the prediction and probability
        st.markdown("## Churn Prediction")
        if churn_prediction_result >= 0.5:
            st.markdown(f'<div class="result-div"><p style="color: #DC2552; font-weight:bold; font-size: 20px;">The customer is likely to churn. The probability of churn is: <span>{churn_probability:.2f}</span></p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-div"><p style="color: #50de40;font-weight:bold; font-size: 20px;">The customer is unlikely to churn. The probability of churn is: <span>{churn_probability:.2f}</span></p></div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
