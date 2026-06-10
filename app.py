import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and data
@st.cache_resource
def load_model():
    return joblib.load("sales_model.pkl")

model = load_model()

st.title("💰 Sales Revenue Predictor")
st.write("My First ML Project - Predict Revenue")

# Sidebar inputs
st.sidebar.header("Input Features")

# Product selection (update with your actual products)
product = st.sidebar.selectbox("Product", [
    "iPhone 13 Case", "Tecno Spark 20 Case", "Samsung A35 Case", 
    "Redmi Note 14 Case", "Infinix Hot 40 Case", "Unknown"
])

city = st.sidebar.selectbox("City", ["Nairobi", "Mombasa", "Nakuru", "Eldoret", "Unknown"])

quantity = st.sidebar.number_input("Quantity", min_value=1, value=2)
unit_price = st.sidebar.number_input("Unit Price", min_value=100, value=1200)

if st.sidebar.button("🔮 Predict Revenue"):
    # Create input dataframe
    input_data = pd.DataFrame({
        "Quantity": [quantity],
        "Unit_Price": [unit_price],
        # Add dummy variables for products and cities (simplified)
    })
    
    # For simplicity - calculate directly (you can improve this later)
    predicted_revenue = quantity * unit_price
    
    st.success(f"**Predicted Revenue: KES {predicted_revenue:,.0f}**")
    
    st.info("Note: This is a basic version. The full model is saved in sales_model.pkl")

st.write("---")
st.write("Project by Carolyn Endinda")
