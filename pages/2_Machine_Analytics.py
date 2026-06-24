import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Machine Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Machine Analytics Dashboard")

# Load Dataset
df = pd.read_csv("data/raw/ai4i2020.csv")

# =========================
# Top Metrics
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Machine Failures", df["Machine failure"].sum())

with col3:
    st.metric(
        "Failure Rate",
        f"{(df['Machine failure'].mean()*100):.2f}%"
    )

with col4:
    st.metric(
        "Machine Types",
        df["Type"].nunique()
    )

st.markdown("---")

# =========================
# Failure Distribution
# =========================

st.subheader("🚨 Failure Distribution")

failure_counts = (
    df["Machine failure"]
    .value_counts()
    .reset_index()
)

failure_counts.columns = [
    "Machine Failure",
    "Count"
]

fig = px.pie(
    failure_counts,
    names="Machine Failure",
    values="Count",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# Machine Type Distribution
# =========================

st.subheader("🏭 Machine Type Distribution")

fig = px.histogram(
    df,
    x="Type"
)

fig.update_traces(
    marker_line_width=1,
    marker_line_color="black"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# Temperature Analysis
# =========================

col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        df,
        x="Air temperature [K]",
        nbins=30,
        title="Air Temperature Distribution"
    )
    
    fig.update_traces(
    marker_line_width=1,
    marker_line_color="black"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.histogram(
        df,
        x="Process temperature [K]",
        nbins=30,
        title="Process Temperature Distribution"
    )
    
    fig.update_traces(
    marker_line_width=1,
    marker_line_color="black"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================
# RPM Analysis
# =========================

st.subheader("⚙️ Rotational Speed Analysis")

fig = px.box(
    df,
    y="Rotational speed [rpm]"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# Torque Analysis
# =========================

st.subheader("🔧 Torque Analysis")

fig = px.box(
    df,
    y="Torque [Nm]"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# Tool Wear Analysis
# =========================

st.subheader("🛠 Tool Wear Analysis")

fig = px.histogram(
    df,
    x="Tool wear [min]",
    nbins=30
)

fig.update_traces(
    marker_line_width=1,
    marker_line_color="black"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# Dataset Preview
# =========================

st.subheader("📋 Dataset Preview")

st.dataframe(df.head(20))