import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Live Monitoring",
    page_icon="🚨",
    layout="wide"
    )

st.title("🚨 Live Machine Monitoring")
st.caption("Real-Time Industrial Machine Health Dashboard")

st.markdown("---")

# Simulated Live Sensor Data

air_temp = np.random.randint(295, 310)
process_temp = np.random.randint(305, 325)
rpm = np.random.randint(1200, 1800)
torque = np.random.randint(20, 70)
tool_wear = np.random.randint(0, 250)

# KPI Cards

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🌡 Air Temp", f"{air_temp} K")

with col2:
    st.metric("🔥 Process Temp", f"{process_temp} K")

with col3:
    st.metric("⚙ RPM", rpm)

with col4:
    st.metric("🔧 Torque", f"{torque} Nm")

with col5:
    st.metric("🛠 Tool Wear", f"{tool_wear} min")

st.markdown("---")

# Machine Status

st.subheader("🏭 Machine Status")

if tool_wear > 200 or torque > 60:
    st.error("🔴 HIGH RISK MACHINE")

elif tool_wear > 120 or torque > 45:
    st.warning("🟡 MEDIUM RISK MACHINE")

else:
    st.success("🟢 MACHINE OPERATING NORMALLY")

st.markdown("---")

# Time Series Data

time = pd.date_range(
end=datetime.now(),
periods=30,
freq="min"
)

monitor_df = pd.DataFrame({
    "Time": time,
    "RPM": np.random.randint(1200, 1800, 30),
    "Torque": np.random.randint(20, 70, 30),
    "Tool Wear": np.random.randint(0, 250, 30)
    })

# RPM Trend

st.subheader("⚙ RPM Trend")

fig = px.line(
    monitor_df,
    x="Time",
    y="RPM",
    markers=True
    )

st.plotly_chart(
    fig,
    use_container_width=True
    )

# Torque Trend

st.subheader("🔧 Torque Trend")

fig = px.line(
monitor_df,
x="Time",
y="Torque",
markers=True
)

st.plotly_chart(
fig,
use_container_width=True
)

# Tool Wear Trend

st.subheader("🛠 Tool Wear Trend")

fig = px.area(
monitor_df,
x="Time",
y="Tool Wear"
)

st.plotly_chart(
fig,
use_container_width=True
)

# Live Sensor Table

st.subheader("📋 Live Sensor Data")

st.dataframe(
monitor_df.tail(10),
use_container_width=True
)

st.markdown("---")

st.success("✅ Monitoring System Active")
