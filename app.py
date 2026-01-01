import streamlit as st
import numpy as np
import joblib

# ===============================
# Load model
# ===============================
model = joblib.load("best_diabetes_model.joblib")

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Diabetes Risk Prediction",
    layout="centered"
)

# ===============================
# Custom CSS
# ===============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f0fdf4, #ecfeff);
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
h1 {
    color: #0f172a;
    text-align: center;
    white-space: nowrap;
    font-size: 3rem;
}

/* Card */
.card {
    background: white;
    padding: 1.8rem;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    margin-top: 1.8rem;
}

/* ===============================
   ADVANCED BUTTON
=============================== */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: white;
    height: 3.4em;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 600;
    border: 2px solid transparent;
    transition: all 0.25s ease-in-out;
}

/* Hover Effect */
.stButton > button:hover {
    transform: scale(1.06);
    border: 2px solid #22c55e;
    box-shadow: 0 0 18px rgba(34, 197, 94, 0.9);
    background: linear-gradient(135deg, #15803d, #22c55e);
}

/* Risk Bar */
.risk-container {
    background: #e5e7eb;
    border-radius: 12px;
    height: 18px;
    width: 100%;
    overflow: hidden;
    margin-top: 12px;
}

.risk-fill {
    height: 100%;
    border-radius: 12px;
    transition: width 0.6s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Title
# ===============================
st.markdown("<h1>Diabetes Risk Prediction System</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#475569;'>AI-powered healthcare application for early diabetes risk assessment.</p>",
    unsafe_allow_html=True
)

# ===============================
# Input Card
# ===============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Patient Health Information")

c1, c2, c3 = st.columns(3)
with c1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
with c2:
    glucose = st.number_input("Glucose (mg/dL)", 0, 300, 120)
with c3:
    bp = st.number_input("Blood Pressure (mm Hg)", 0, 200, 70)

c4, c5, c6 = st.columns(3)
with c4:
    skin = st.number_input("Skin Thickness (mm)", 0, 100, 20)
with c5:
    insulin = st.number_input("Insulin (μU/ml)", 0, 900, 80)
with c6:
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0)

c7, c8, _ = st.columns(3)
with c7:
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
with c8:
    age = st.number_input("Age", 1, 120, 30)

st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# Prediction
# ===============================
if st.button("Predict"):
    X = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]
    risk_percent = int(prob * 100)

    if risk_percent < 35:
        color = "#16a34a"
        status = "Low Risk of Diabetes"
    elif risk_percent < 65:
        color = "#f59e0b"
        status = "Moderate Risk of Diabetes"
    else:
        color = "#dc2626"
        status = "High Risk of Diabetes"

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Result")

    st.markdown(f"**{status}**")

    st.markdown(f"""
        <div class="risk-container">
            <div class="risk-fill" style="width:{risk_percent}%; background:{color};"></div>
        </div>
        <p style="margin-top:8px; font-weight:600;">Risk Level: {risk_percent}%</p>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
