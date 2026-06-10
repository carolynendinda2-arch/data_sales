import streamlit as st

st.title("💰 Sales Revenue Predictor")
st.write("**My Sales Analysis Project**")

st.success("App is working! 🚀")

quantity = st.number_input("Quantity", min_value=1, value=2)
unit_price = st.number_input("Unit Price (KES)", min_value=100, value=1200)

if st.button("Calculate Revenue"):
    revenue = quantity * unit_price
    st.success(f"**Predicted Revenue: KES {revenue:,.0f}**")

st.caption("Project by Carolyn Endinda")
