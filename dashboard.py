import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Breast Cancer Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Breast Cancer Analytics Dashboard")

st.markdown("""
Analytics dashboard for monitoring the breast cancer detection project.
""")

# =====================
# DATASET STATISTICS
# =====================

total_images = 277524
cancer_cases = 78786
non_cancer_cases = 198738

accuracy = 84.64
precision = 84.0
recall = 85.0
auc = 91.0

# =====================
# KPIs
# =====================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Images", f"{total_images:,}")
col2.metric("Cancer Cases", f"{cancer_cases:,}")
col3.metric("Non-Cancer Cases", f"{non_cancer_cases:,}")
col4.metric("Accuracy", f"{accuracy}%")

# =====================
# MODEL PERFORMANCE
# =====================

st.subheader("📈 Model Performance")

performance = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "AUC-ROC"],
    "Value": [accuracy, precision, recall, auc]
})

st.bar_chart(
    performance.set_index("Metric")
)

# =====================
# DATASET DISTRIBUTION
# =====================

st.subheader("📊 Dataset Distribution")

distribution = pd.DataFrame({
    "Class": ["Cancer", "Non-Cancer"],
    "Count": [cancer_cases, non_cancer_cases]
})

st.bar_chart(
    distribution.set_index("Class")
)

# =====================
# PROJECT OVERVIEW
# =====================

st.subheader("🧠 Project Overview")

st.success("""
✔ Histopathology Dataset

✔ Deep Learning using EfficientNetB0

✔ Accuracy: 84.64%

✔ AI Medical Assistant

✔ Grad-CAM Explainability

✔ Streamlit Deployment

✔ Data Analytics Dashboard
""")
