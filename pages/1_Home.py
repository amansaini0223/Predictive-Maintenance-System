import streamlit as st

st.set_page_config(layout="wide")

# Banner
st.image("assets/machine_banner.jpg", use_container_width=True)

# Title
st.title("🏭 Predictive Maintenance AI")
st.subheader("AI-Powered Machine Failure Prediction System")

st.markdown("---")

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", "10,000")

with col2:
    st.metric("Features", "6")

with col3:
    st.metric("Failure Cases", "339")

with col4:
    st.metric("Model Accuracy", "98.8%")

st.markdown("---")

# Project Overview

st.header("📌 Project Overview")

st.write("""
This system predicts machine failures using machine sensor data.
The model helps industries reduce downtime and schedule maintenance before breakdowns occur.
""")

# Features

st.header("⚙️ Input Features")

features = [
    "Type",
    "Air Temperature",
    "Process Temperature",
    "Rotational Speed",
    "Torque",
    "Tool Wear"
]

for feature in features:
    st.write("✅", feature)

st.markdown("---")

# Model Summary

st.header("🤖 Model Summary")

st.success("""
Model Used : XGBoost Classifier

Accuracy : 98.8%

F1 Score : 80.3%

Purpose : Predict Machine Failure Before Breakdown
""")

st.markdown("---")

# Footer

st.caption("Developed using Python, Scikit-Learn, XGBoost and Streamlit")