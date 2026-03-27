import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config (Must be the first Streamlit command)
st.set_page_config(page_title="OralCare AI - Nigeria", page_icon="🦷", layout="wide")

# 2. Professional Header & Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 6])
with col1:
    st.title("🦷")
with col2:
    st.title("OralCare AI: Dental Triage")
    st.write("_Smart Dental Health Assessment for Nigeria_")

st.sidebar.success("✅ System Online: Dataraflow Intern Project")
st.markdown("---")

# 3. Sidebar for User Input
st.sidebar.header("📋 Patient Profile")
age = st.sidebar.slider("Age", 1, 100, 25)
location = st.sidebar.selectbox("Location", ["Lagos", "Abuja", "Ibadan", "Kano", "Enugu"])
sugar = st.sidebar.select_slider("Daily Sugar Intake", options=["Low", "Medium", "High"])
pain = st.sidebar.slider("Pain Level (0-10)", 0, 10, 2)
swelling = st.sidebar.checkbox("Is there any visible swelling?")
bleeding = st.sidebar.checkbox("Are your gums bleeding?")

# 4. Logic Tools
def calculate_risk(sugar, pain, swelling, bleeding):
    score = 0
    if sugar == "High": score += 2
    if pain > 7: score += 4
    if swelling: score += 4
    if bleeding: score += 2
    
    if score >= 8: return "🔴 EMERGENCY", "Please seek immediate care at a dental emergency ward."
    if score >= 5: return "🟡 URGENT", "Schedule a dental appointment within the next 48 hours."
    return "🟢 ROUTINE", "No immediate danger. Schedule a regular check-up."

def get_clinic(city):
    clinics = {
        'Lagos': 'LUTH Dental Clinic, Idi-Araba',
        'Abuja': 'National Hospital Dental Wing',
        'Ibadan': 'UCH Dental Center',
        'Kano': 'Aminu Kano Teaching Hospital',
        'Enugu': 'UNTH Dental School'
    }
    return clinics.get(city, "Nearest General Teaching Hospital")

# 5. Dashboard Layout
# 5.1 Historical Insight Chart (Visualizes the mockup data)
st.subheader(f"📊 Oral Health Trends in {location}")
try:
    df = pd.read_csv('nigerian_dental_data.csv')
    city_df = df[df['location'] == location]
    st.bar_chart(city_df['symptom_pain_level'].value_counts().sort_index())
    st.caption("Distribution of pain levels reported by other patients in your region.")
except:
    st.info("Historical data summary will appear here once the dataset is loaded.")

st.markdown("---")

# 5.2 The Analysis Button
if st.button("🚀 Run AI Triage Analysis"):
    with st.spinner("Agents are analyzing your symptoms..."):
        # Run the "Agents"
           
    # Run the "Agents"
        status_label, instruction = calculate_risk(sugar, pain, swelling, bleeding)
        clinic_link = get_clinic(location)
    
    # Display Results in Metric Cards
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="Urgency Level", value=status_label)
    with m_col2:
        st.metric(label="Primary Symptom", value=f"Pain {pain}/10")
    with m_col3:
        st.metric(label="Recommended City", value=location)

    # Final Detailed Report
    with st.expander("📄 View Detailed AI Report", expanded=True):
        st.write(f"### Assessment: {status_label}")
        st.write(instruction)
        st.success(f"**Referral:** Proceed to **{clinic_link}**")
        st.info("Medical Disclaimer: This AI tool provides triage guidance only. It is not a formal medical diagnosis.")

# 6. Footer
st.markdown("<br><hr><center>Built by [Ayomide Zaccheaus] | Dataraflow Internship Project 2026</center>", unsafe_allow_html=True)
