import streamlit as st
import pandas as pd
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("sales_model.pkl")

model = load_model()

st.title("💰 Sales Revenue Predictor")
st.markdown("**Sales Analysis Dashboard**")

st.sidebar.header("Input Sales Details")

product = st.sidebar.selectbox("Product", [
    "iPhone 13 Case", "Tecno Spark 20 Case", "Samsung A35 Case", 
    "Redmi Note 14 Case", "Infinix Hot 40 Case", "Power Bank", 
    "Earbuds", "Screen Protector", "Unknown"
])

city = st.sidebar.selectbox("City", ["Nairobi", "Mombasa", "Nakuru", "Eldoret", "Unknown"])

quantity = st.sidebar.number_input("Quantity", min_value=1, value=2, step=1)
unit_price = st.sidebar.number_input("Unit Price (KES)", min_value=100, value=1200, step=50)

if st.sidebar.button("🔮 Predict Revenue", type="primary"):
    input_data = pd.DataFrame({
        "Quantity": [quantity],
        "Unit_Price": [unit_price],
        "Order_ID": [100000]
    })
    
    # One-hot encoding
    products = ["Product_" + p for p in ["iPhone 13 Case", "Tecno Spark 20 Case", "Samsung A35 Case", 
                                        "Redmi Note 14 Case", "Infinix Hot 40 Case", "Power Bank", 
                                        "Earbuds", "Screen Protector"]]
    cities = ["City_" + c for c in ["Nairobi", "Mombasa", "Nakuru", "Eldoret"]]
    
    for col in products + cities:
        input_data[col] = 0
    
    if "Product_" + product in input_data.columns:
        input_data["Product_" + product] = 1
    if "City_" + city in input_data.columns:
        input_data["City_" + city] = 1
    
    prediction = model.predict(input_data)[0]
    
    st.success(f"**Predicted Revenue: KES {prediction:,.0f}**")
    st.balloons()

st.write("---")
st.caption("Project by Carolyn Endinda")
