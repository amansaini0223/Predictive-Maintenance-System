import streamlit as st

st.set_page_config(
    page_title="Predictive Maintenance AI",
    page_icon="🏭",
    layout="wide"
)

st.image(
    "assets/machine_banner.jpg",
    use_container_width=True
)

st.title("🏭 Predictive Maintenance AI")
st.subheader("AI-Powered Machine Failure Prediction System")

st.markdown("---")

# =========================
# KPI Cards
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
    "📊 Total Records",
    "10,000"
    )

with col2:
    st.metric(
    "🚨 Failure Cases",
    "339"
    )

with col3:
    st.metric(
    "🤖 Model Accuracy",
    "98.8%"
    )

with col4:
    st.metric(
    "⚙️ Features Used",
    "6"
    )

st.markdown("---")

# =========================
# Project Overview
# =========================

st.header("📌 Project Overview")

st.write("""
Predictive Maintenance AI is an industrial machine monitoring and failure prediction system.

The project uses Machine Learning (XGBoost) to analyze machine sensor data and predict failures before breakdowns occur.

This helps industries reduce downtime, improve operational efficiency and schedule maintenance proactively.
""")

st.markdown("---")

# =========================
# Features Used
# =========================

st.header("⚙️ Features Used")

col1, col2 = st.columns(2)

with col1:
    st.success("Machine Type")
    st.success("Air Temperature")
    st.success("Process Temperature")

with col2:
    st.success("Rotational Speed")
    st.success("Torque")
    st.success("Tool Wear")

st.markdown("---")

# =========================
# Technology Stack
# =========================

st.header("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("Python")
    st.info("Pandas")
    st.info("NumPy")

with tech2:
    st.info("Scikit-Learn")
    st.info("XGBoost")
    st.info("Joblib")

with tech3:
    st.info("Plotly")
    st.info("Streamlit")
    st.info("Machine Learning")

st.markdown("---")

# =========================
# Dashboard Modules
# =========================

st.header("📂 Dashboard Modules")

st.write("📊 Machine Analytics")
st.write("🤖 Failure Prediction")
st.write("🚨 Live Monitoring")
st.write("📈 Model Performance")

st.markdown("---")

# =========================
# Model Summary
# =========================

st.header("🏆 Best Model")

st.success("""
Model Selected: XGBoost

Accuracy: 98.8%

Precision: 91%

Recall: 72%

F1 Score: 80%
""")

st.markdown("---")

st.success(
"✅ Predictive Maintenance System Ready for Deployment"
)