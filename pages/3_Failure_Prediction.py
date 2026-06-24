import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Failure Prediction",
    page_icon="🤖",
    layout="wide"
)

# =========================
# Load Files
# =========================

model = joblib.load("models/model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

# =========================
# Page Header
# =========================

st.title("🤖 Machine Failure Prediction")
st.caption("AI-Powered Predictive Maintenance using XGBoost")

st.markdown("---")

# =========================
# Input Section
# =========================

st.subheader("⚙️ Machine Parameters")

col1, col2 = st.columns(2)

with col1:

    machine_type = st.selectbox(
        "Machine Type",
        ["L", "M", "H"]
    )

    air_temp = st.number_input(
        "Air Temperature [K]",
        min_value=250.0,
        max_value=400.0,
        value=300.0
    )

    process_temp = st.number_input(
        "Process Temperature [K]",
        min_value=250.0,
        max_value=450.0,
        value=310.0
    )

with col2:

    rotational_speed = st.number_input(
        "Rotational Speed [rpm]",
        min_value=500,
        max_value=5000,
        value=1500
    )

    torque = st.number_input(
        "Torque [Nm]",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

    tool_wear = st.number_input(
        "Tool Wear [min]",
        min_value=0,
        max_value=300,
        value=100
    )

st.markdown("---")

# =========================
# Prediction Button
# =========================

if st.button("🔍 Predict Failure", use_container_width=True):

    encoded_type = label_encoder.transform(
        [machine_type]
    )[0]

    input_data = pd.DataFrame(
        [[
            encoded_type,
            air_temp,
            process_temp,
            rotational_speed,
            torque,
            tool_wear
        ]],
        columns=[
            "Type",
            "Air_temperature",
            "Process_temperature",
            "Rotational_speed",
            "Torque",
            "Tool_wear"
        ]
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    health_score = round(
        (1 - probability) * 100,
        2
    )

    st.markdown("---")

    st.subheader("📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Failure Probability",
            f"{probability * 100:.2f}%"
        )

    with col2:
        st.metric(
            "Health Score",
            f"{health_score}%"
        )

    with col3:
        st.metric(
            "Prediction",
            "Failure" if prediction == 1 else "Normal"
        )

    st.markdown("---")

    # =========================
    # Risk Level
    # =========================

    st.subheader("🚨 Risk Assessment")

    if probability < 0.30:

        st.success("🟢 LOW RISK")

        st.success(
            "Machine is operating normally."
        )

    elif probability < 0.70:

        st.warning("🟡 MEDIUM RISK")

        st.warning(
            "Maintenance should be scheduled soon."
        )

    else:

        st.error("🔴 HIGH RISK")

        st.error(
            "Immediate maintenance required."
        )

    st.markdown("---")

    # =========================
    # Maintenance Recommendation
    # =========================

    st.subheader("🔧 Maintenance Recommendation")

    if probability < 0.30:

        st.success("✔ Machine Healthy")
        st.success("✔ No Immediate Maintenance Required")
        st.success("✔ Continue Regular Monitoring")

    elif probability < 0.70:

        st.warning("✔ Inspect Machine Components")
        st.warning("✔ Check Temperature & Torque")
        st.warning("✔ Schedule Maintenance Soon")

    else:

        st.error("✔ Critical Machine Condition")
        st.error("✔ Immediate Maintenance Required")
        st.error("✔ Risk of Unexpected Breakdown")