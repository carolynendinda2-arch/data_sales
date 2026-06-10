import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="RevenueForge", layout="wide")
st.title("📈 RevenueForge")
st.markdown("**Professional Sales Revenue Prediction**")

@st.cache_resource
def load_model():
    return joblib.load("sales_model.pkl")

model = load_model()

# Get expected features from the model
expected_features = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else None

st.sidebar.header("Prediction Input")

product = st.sidebar.selectbox("Product", [
    "iPhone 13 Case", "Tecno Spark 20 Case", "Samsung A35 Case", 
    "Redmi Note 14 Case", "Infinix Hot 40 Case", "Power Bank", 
    "Earbuds", "Screen Protector", "Unknown"
])

city = st.sidebar.selectbox("City", ["Nairobi", "Mombasa", "Nakuru", "Eldoret", "Unknown"])

quantity = st.sidebar.number_input("Quantity", min_value=1, value=3)
unit_price = st.sidebar.number_input("Unit Price (KES)", min_value=100, value=1200)

if st.sidebar.button("Predict Revenue", type="primary"):
    try:
        # Base data
        data = {
            "Quantity": [quantity],
            "Unit_Price": [unit_price],
            "Order_ID": [100000]
        }
        
        df = pd.DataFrame(data)
        
        # Add one-hot columns safely
        if expected_features is not None:
            for col in expected_features:
                if col not in df.columns:
                    df[col] = 0
                    
            # Set correct values
            if f"Product_{product}" in df.columns:
                df[f"Product_{product}"] = 1
            if f"City_{city}" in df.columns:
                df[f"City_{city}"] = 1
        
        # Ensure correct column order
        if expected_features is not None:
            df = df[expected_features]
        
        prediction = model.predict(df)[0]
        
        st.success(f"**Predicted Revenue: KES {prediction:,.0f}**")
        
    except Exception as e:
        st.error(f"Prediction Error: {str(e)}")
        st.info("Please check input values or contact developer.")

# Show graphs
st.divider()
st.subheader("Model Insights")
col1, col2 = st.columns(2)
with col1:
    try:
        st.image("feature_importance.png", use_column_width=True)
    except:
        pass
with col2:
    try:
        st.image("actual_vs_predicted.png", use_column_width=True)
    except:
        pass

st.caption("Project by Carolyne Ndinda")
