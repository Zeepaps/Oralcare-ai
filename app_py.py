import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="OralCare AI - Nigeria", page_icon="🦷")

# 2. Title and Header
st.title("🦷 OralCare AI: Dental Triage System")
st.markdown("---")

# 3. Sidebar for User Input (The "Patient" Profile)
st.sidebar.header("Patient Information")
age = st.sidebar.slider("Age", 1, 100, 25)
location = st.sidebar.selectbox("Location", ["Lagos", "Abuja", "Ibadan", "Kano", "Enugu"])
sugar = st.sidebar.select_slider("Daily Sugar Intake", options=["Low", "Medium", "High"])
pain = st.sidebar.slider("Pain Level (0-10)", 0, 10, 2)
swelling = st.sidebar.checkbox("Is there any swelling?")

# 4. Logic Tools
def calculate_risk(sugar, pain, swelling):
    score = 0
    if sugar == "High": score += 3
    if pain > 7: score += 4
    if swelling: score += 5

    if score >= 8: return "🔴 EMERGENCY: See a dentist within 24 hours."
    if score >= 5: return "🟡 URGENT: Schedule an appointment this week."
    return "🟢 ROUTINE: Regular check-up recommended."

def get_clinic(city):
    clinics = {
        'Lagos': 'LUTH Dental Clinic, Idi-Araba',
        'Abuja': 'National Hospital Dental Wing',
        'Ibadan': 'UCH Dental Center',
        'Kano': 'Aminu Kano Teaching Hospital',
        'Enugu': 'UNTH Dental School'
    }
    return clinics.get(city, "Nearest General Hospital")

# 5. The "Run Analysis" Button
if st.button("Run AI Dental Triage"):
    st.subheader("AI Agent Analysis")

    # Simulate Agent 1: Triage
    with st.status("SymptomAnalyst Agent is thinking...", expanded=True):
        risk_result = calculate_risk(sugar, pain, swelling)
        st.write(f"**Triage Verdict:** {risk_result}")

    # Simulate Agent 2: Referral
    with st.status("AccessOrchestrator Agent searching clinics...", expanded=True):
        clinic_result = get_clinic(location)
        st.success(f"**Recommended Facility:** {clinic_result}")

    st.info("Note: This is an AI-generated assessment. Always consult a human dentist for medical diagnosis.")
