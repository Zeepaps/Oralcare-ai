import streamlit as st
import pandas as pd
from openai import AzureOpenAI

# 1. Page Config
st.set_page_config(page_title="OralCare AI - Nigeria", page_icon="🦷", layout="wide")

# 2. Azure OpenAI Client Setup
client = AzureOpenAI(
    api_key=st.secrets["AZURE_OPENAI_API_KEY"],  
    api_version="2024-08-01-preview", 
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
)

# 3. Professional Styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #007BFF; color: white; font-weight: bold; }
    .report-card { padding: 20px; border-radius: 10px; background-color: #ffffff; border-left: 5px solid #007BFF; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦷 OralCare AI: Multi-Agent Triage")
st.write(f"_Internship Project for **Dataraflow** | Powered by Azure GPT-4o_")
st.markdown("---")

# 4. Sidebar Inputs (Restored all features)
st.sidebar.header("📋 Patient Profile")
age = st.sidebar.slider("Patient Age", 1, 100, 25)
location = st.sidebar.selectbox("Location", ["Lagos", "Abuja", "Ibadan", "Kano", "Enugu"])
sugar = st.sidebar.select_slider("Daily Sugar Intake", options=["Low", "Medium", "High"])
pain = st.sidebar.slider("Pain Level (0-10)", 0, 10, 5)
swelling = st.sidebar.checkbox("Is there any visible swelling?")
bleeding = st.sidebar.checkbox("Are your gums bleeding?")

def get_clinic_name(city):
    clinics = {'Lagos': 'LUTH', 'Abuja': 'National Hospital', 'Ibadan': 'UCH', 'Kano': 'AKTH', 'Enugu': 'UNTH'}
    return clinics.get(city, "the nearest General Teaching Hospital")

# 5. The "Multi-Agent" Reasoning Engine (Enhanced for Personality)
def get_ai_diagnosis(age, sugar, pain, swelling, bleeding, location):
    clinic = get_clinic_name(location)
    
    # We use a 'System Message' to set the tone and a 'User Message' for the data
    response = client.chat.completions.create(
        model=st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"],
        messages=[
            {
                "role": "system", 
                "content": "You are a warm, empathetic Nigerian Dental Triage Assistant. Do not use bullet points. Speak directly to the patient as 'you'. Blend clinical advice with a supportive, human tone."
            },
            {
                "role": "user", 
                "content": f"""
                Analyze this patient: Age {age}, Pain {pain}/10, Swelling: {swelling}, Bleeding: {bleeding}, Sugar: {sugar}.
                They are in {location}. 
                
                Your Task: 
                1. Acknowledge their specific pain and age with empathy.
                2. Explain how their sugar intake or symptoms (like bleeding) relate to their situation.
                3. Tell them specifically to go to {clinic}.
                4. End with a supportive 'Stay strong' or similar encouraging phrase.
                """
            }
        ]
    )
    return response.choices[0].message.content

# 6. Main Dashboard Interface
if st.button("🚀 Run AI Triage Analysis"):
    with st.spinner("SymptomAnalyst & PatientCounselor agents are evaluating your profile..."):
        try:
            ai_report = get_ai_diagnosis(age, sugar, pain, swelling, bleeding, location)
            
            # Layout for Results
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric(label="Pain Intensity", value=f"{pain}/10")
                st.metric(label="Urgency Status", value="🔴 Emergency" if pain > 7 or swelling else "🟡 Urgent" if bleeding else "🟢 Routine")
            
            with col2:
                st.markdown("### 📄 Personalized Health Report")
                st.info(ai_report)
                st.success(f"**Referral:** Proceed to the Dental Wing at **{get_clinic_name(location)}**.")
            
        except Exception as e:
            st.error("🚨 Connection Error: Please verify your Azure Deployment Name.")
            st.write(f"Details: {e}")

# 7. Footer
st.markdown("<br><hr><center>Built by **Ayomide Zaccheaus** | Dataraflow Internship Project 2026</center>", unsafe_allow_html=True)
