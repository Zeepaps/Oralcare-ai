import streamlit as st
import pandas as pd
from openai import AzureOpenAI

# 1. Page Config
st.set_page_config(page_title="OralCare AI - Nigeria", page_icon="🦷", layout="wide")

# 2. Azure OpenAI Client Setup
# Ensure these names match your "Secrets" EXACTLY
client = AzureOpenAI(
    api_key=st.secrets["AZURE_OPENAI_API_KEY"],  
    api_version="2024-02-15-preview",
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
)

# 3. Professional Styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #007BFF; color: white; font-weight: bold; }
    .report-box { padding: 20px; border-radius: 10px; background-color: #ffffff; border: 1px solid #e0e0e0; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦷 OralCare AI: Multi-Agent Triage")
st.write(f"_Internship Project for **Dataraflow** | Powered by Azure GPT-4o_")
st.markdown("---")

# 4. Sidebar Inputs
st.sidebar.header("📋 Patient Profile")
age = st.sidebar.slider("Patient Age", 1, 100, 25)
location = st.sidebar.selectbox("Location", ["Lagos", "Abuja", "Ibadan", "Kano", "Enugu"])
sugar = st.sidebar.select_slider("Daily Sugar Intake", options=["Low", "Medium", "High"])
pain = st.sidebar.slider("Pain Level (0-10)", 0, 10, 5)
swelling = st.sidebar.checkbox("Visible Swelling?")
bleeding = st.sidebar.checkbox("Gum Bleeding?")

# Helper function for hard-coded referrals
def get_clinic_name(city):
    clinics = {'Lagos': 'LUTH', 'Abuja': 'National Hospital', 'Ibadan': 'UCH', 'Kano': 'AKTH', 'Enugu': 'UNTH'}
    return clinics.get(city, "the nearest Teaching Hospital")

# 5. The "Multi-Agent" Reasoning Engine
def get_ai_diagnosis(age, sugar, pain, swelling, bleeding, location):
    # This prompt instructs the AI to act as two different agents
    clinic = get_clinic_name(location)
    
    prompt = f"""
    You are acting as two specialized agents:
    1. [SymptomAnalyst]: Analyze this patient: Age {age}, Pain {pain}/10, Swelling: {swelling}, Bleeding: {bleeding}.
    2. [PatientCounselor]: Given their {sugar} sugar intake, provide empathetic advice.

    REQUIRED ACTION:
    - Acknowledge the pain level and age-specific concerns.
    - Mention the clinical significance of swelling/bleeding if present.
    - Explicitly direct them to {clinic} in {location}.
    - Keep the response under 100 words and very supportive.
    """
    
    response = client.chat.completions.create(
        model=st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"],
        messages=[
            {"role": "system", "content": "You are a professional Dental Triage AI assistant for Nigerian patients."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 6. Main Dashboard Interface
st.subheader("📊 Diagnostic Dashboard")

if st.button("🚀 Run Multi-Agent Triage Analysis"):
    with st.spinner("SymptomAnalyst and PatientCounselor agents are processing..."):
        try:
            # Call the Azure AI
            ai_report = get_ai_diagnosis(age, sugar, pain, swelling, bleeding, location)
            
            # Display Results
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Pain Scale", value=f"{pain}/10")
            with col2:
                st.metric(label="Urgency", value="High" if pain > 7 or swelling else "Moderate")
            with col3:
                st.metric(label="Location", value=location)

            st.markdown("### 📄 Official AI Assessment")
            st.info(ai_report)
            
            st.success(f"**Referral:** Please proceed to the Dental Wing at **{get_clinic_name(location)}**.")
            
        except Exception as e:
            st.error("🚨 Connection Error: Please verify your Azure Deployment Name in Streamlit Secrets.")
            st.write(f"Details: {e}")

# 7. Footer
st.markdown("<br><hr><center>Built by **Ayomide Zaccheaus** | Dataraflow Internship Project 2026</center>", unsafe_allow_html=True)
