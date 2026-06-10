import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="RevenueForge | Sales Predictor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #1E3A8A;}
    .metric-card {background-color: #F8FAFC; padding: 1rem; border-radius: 10px; border: 1px solid #E2E8F0;}
</style>
""", unsafe_allow_html=True)

# Load Model
@st.cache_resource
def load_model():
    return joblib.load("sales_model.pkl")

model = load_model()

# Header
st.title("📈 RevenueForge")
st.markdown("**Professional Sales Revenue Prediction System**")
st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y')}")

# Sidebar
with st.sidebar:
    st.header("🔧 Prediction Parameters")

    product = st.selectbox(
        "Product Category",
        ["iPhone 13 Case", "Tecno Spark 20 Case", "Samsung A35 Case",
         "Redmi Note 14 Case", "Infinix Hot 40 Case", "Power Bank",
         "Earbuds", "Screen Protector", "Unknown"]
    )

    city = st.selectbox(
        "Sales Region",
        ["Nairobi", "Mombasa", "Nakuru", "Eldoret", "Unknown"]
    )

    col1, col2 = st.columns(2)
    with col1:
        quantity = st.number_input("Quantity", min_value=1, value=5, step=1)
    with col2:
        unit_price = st.number_input("Unit Price (KES)", min_value=100, value=1250, step=50)

    predict_btn = st.button("🚀 Predict Revenue", type="primary", use_container_width=True)

# Main Content
if predict_btn:
    with st.spinner("Generating prediction..."):
        # Prepare input
        input_data = pd.DataFrame({
            "Quantity": [quantity],
            "Unit_Price": [unit_price],
            "Order_ID": [100000]
        })

        # One-hot encoding
        product_list = ["iPhone 13 Case", "Tecno Spark 20 Case", "Samsung A35 Case",
                       "Redmi Note 14 Case", "Infinix Hot 40 Case", "Power Bank",
                       "Earbuds", "Screen Protector"]
        city_list = ["Nairobi", "Mombasa", "Nakuru", "Eldoret"]

        for p in product_list:
            input_data[f"Product_{p}"] = 1 if p == product else 0
        for c in city_list:
            input_data[f"City_{c}"] = 1 if c == city else 0

        # Make Prediction
        prediction = model.predict(input_data)[0]

        # Display Results
        st.success(f"**Predicted Revenue: KES {prediction:,.0f}**")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Quantity", quantity)
        with col2:
            st.metric("Unit Price", f"KES {unit_price:,.0f}")
        with col3:
            st.metric("Total Revenue", f"KES {prediction:,.0f}")

# Model Insights Section
st.divider()
st.subheader("📊 Model Insights")

col1, col2 = st.columns(2)
with col1:
    try:
        st.image("feature_importance.png", caption="Top Feature Importance", use_column_width=True)
    except:
        st.info("Feature importance chart will be displayed here")

with col2:
    try:
        st.image("actual_vs_predicted.png", caption="Model Performance", use_column_width=True)
    except:
        st.info("Performance visualization will be displayed here")

# Footer
st.divider()
st.markdown("**Built with:** Random Forest Regressor • Streamlit • Scikit-learn")
st.caption("Project by Carolyne Ndinda")

