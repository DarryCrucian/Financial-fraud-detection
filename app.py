import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from joblib import load

# Custom CSS to enhance the app's appearance
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        font-family: "Arial", sans-serif;
    }
    h1, h2, h3, h4 {
        color: #2C3E50;
    }
    .stButton button {
        background-color: #1abc9c;
        color: white;
        border-radius: 8px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# App Title and Sidebar
st.title("💼 Professional Fraud Detection App")
st.sidebar.header("Navigation")
st.sidebar.markdown("Upload a CSV file containing transaction data to detect fraudulent activities.")
uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV)", type=["csv"])

# Load the trained model
model = load('best_naive_bayes_model.joblib')

# Load the feature names used during training
feature_names = pd.read_csv('feature_names.csv', header=None).iloc[:, 0].tolist()

# Displaying content based on file upload
if uploaded_file is not None:
    # Read the dataset
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Dataset Overview")
    st.dataframe(data.head(10))
    
    # Data Visualization
    st.subheader("Transaction Type Distribution")
    transaction_counts = data['type'].value_counts()
    fig = px.bar(transaction_counts, x=transaction_counts.index, y=transaction_counts.values, labels={'x': 'Transaction Type', 'y': 'Count'}, title="Transaction Type Distribution")
    st.plotly_chart(fig)
    
    st.subheader("Transaction Amount Over Time")
    fig = px.line(data, x='step', y='amount', color='type', title="Transaction Amount Over Time")
    st.plotly_chart(fig)
    
    # Prepare the data for prediction
    X = data.drop(['nameOrig', 'nameDest', 'isFraud', 'isFlaggedFraud'], axis=1, errors='ignore')
    X = pd.get_dummies(X, columns=['type'], drop_first=False)
    
    # Align X with the saved feature names
    for col in feature_names:
        if col not in X.columns:
            X[col] = 0  # Add missing columns
    X = X[feature_names]  # Reorder columns to match the training set
    
    # Make predictions
    predictions = model.predict(X)
    data['PredictedFraud'] = predictions
    
    # Show flagged fraud transactions
    fraud_transactions = data[data['PredictedFraud'] == 1]
    st.subheader("Flagged Fraud Transactions")
    if not fraud_transactions.empty:
        st.write(f"Total Flagged Fraud Transactions: {len(fraud_transactions)}")
        st.dataframe(fraud_transactions)
        
        # Enhanced Visualization for Fraud Transactions
        st.subheader("Fraud Transaction Analysis")
        fig = px.scatter(fraud_transactions, x='amount', y='oldbalanceOrg', color='type', size='amount',
                         hover_data=['nameOrig', 'nameDest'], title="Scatter Plot of Flagged Fraud Transactions")
        st.plotly_chart(fig)
    else:
        st.write("No fraud transactions detected.")

    st.sidebar.success("Upload successful! Analysis complete.")
else:
    st.sidebar.warning("Please upload a CSV file to start detection.")
