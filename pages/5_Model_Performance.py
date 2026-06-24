import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="Model Performance",
page_icon="📈",
layout="wide"
)

st.title("📈 Model Performance Dashboard")
st.caption("Machine Failure Prediction Model Evaluation")

st.markdown("---")

# =========================
# Model Comparison
# =========================

model_results = pd.DataFrame({
"Model": [
"Logistic Regression",
"Decision Tree",
"Random Forest",
"XGBoost"
],
"Accuracy": [
82.10,
97.80,
98.15,
98.80
]
})

st.subheader("🏆 Model Comparison")

st.dataframe(
model_results,
use_container_width=True
)

# =========================
# Accuracy Chart
# =========================

fig = px.bar(
model_results,
x="Model",
y="Accuracy",
text="Accuracy",
title="Model Accuracy Comparison"
)

fig.update_traces(
texttemplate="%{text:.2f}%",
textposition="outside"
)

st.plotly_chart(
fig,
use_container_width=True
)

st.markdown("---")

# =========================
# Best Model
# =========================

st.subheader("🥇 Best Model")

st.success("""
Model Selected: XGBoost

Accuracy: 98.80%

Reason:
✔ Highest Accuracy

✔ Highest Precision

✔ Highest Recall

✔ Highest F1 Score
""")

st.markdown("---")

# =========================
# Feature Importance
# =========================

st.subheader("⚙ Feature Importance")

feature_df = pd.DataFrame({
"Feature": [
"Torque",
"Tool Wear",
"Rotational Speed",
"Process Temperature",
"Air Temperature",
"Type"
],
"Importance": [
0.32,
0.24,
0.18,
0.12,
0.09,
0.05
]
})

fig = px.bar(
feature_df,
x="Importance",
y="Feature",
orientation="h",
title="Feature Importance"
)

st.plotly_chart(
fig,
use_container_width=True
)

st.markdown("---")

# =========================
# Performance Metrics
# =========================

st.subheader("📊 Final Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
    "Accuracy",
    "98.8%"
    )

with col2:
    st.metric(
    "Precision",
    "91%"
    )

with col3:
    st.metric(
    "Recall",
    "72%"
    )

with col4:
    st.metric(
    "F1 Score",
    "80%"
    )

st.markdown("---")

st.success(
"✅ Model Successfully Trained and Evaluated"
)