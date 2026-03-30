import streamlit as st
import pandas as pd
from openai import AzureOpenAI

# 1. Page Config
st.set_page_config(page_title="OralCare AI - Nigeria", page_icon="🦷", layout="wide")

# 2. Azure OpenAI Client Setup
try:
    client = AzureOpenAI(
        api_key=st.secrets["AZURE_OPENAI_API_KEY"],  
        api_version="2024-02-01", # Updated to standard stable version
        azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
    )
except Exception as e:
    st.error("Secrets Configuration Error. Check your Streamlit Dashboard.")

# 3. Styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #007BFF; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦷 OralCare AI: Multi-Agent Triage")
st.write("_Project for Dataraflow & GenAI Course 2026_")

# 4. Inputs
st.sidebar.header("📋 Patient Profile")
age = st.sidebar.slider("Age", 1, 100, 25)
location = st.sidebar.selectbox("Location", ["Lagos", "Abuja", "Ibadan", "Kano", "Enugu"])
pain = st.sidebar.slider("Pain Level (0-10)", 0, 10, 5)
swelling = st.sidebar.checkbox("Visible Swelling?")

def get_clinic_name(city):
    clinics = {'Lagos': 'LUTH', 'Abuja': 'National Hospital', 'Ibadan': 'UCH', 'Kano': 'AKTH', 'Enugu': 'UNTH'}
    return clinics.get(city, "Teaching Hospital")

# 5. Analysis
if st.button("🚀 Run Multi-Agent Triage Analysis"):
    with st.spinner("Agents are communicating with Azure OpenAI..."):
        try:
            # The AI Call
            response = client.chat.completions.create(
                model=st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"],
                messages=[
                    {"role": "system", "content": "You are a Dental Triage AI for Nigeria."},
                    {"role": "user", "content": f"Patient: Age {age}, Pain {pain}/10, Swelling: {swelling}. Suggest {get_clinic_name(location)}."}
                ]
            )
            
            ai_report = response.choices[0].message.content
            
            st.markdown("### 📄 AI Assessment")
            st.info(ai_report)
            st.success(f"**Referral:** Proceed to **{get_clinic_name(location)}**")

        except Exception as e:
            st.error("🚨 Connection Error!")
            st.write("**Debug Info for Developer:**")
            st.write(f"- Deployment Name Used: `{st.secrets['AZURE_OPENAI_DEPLOYMENT_NAME']}`")
            st.write(f"- Endpoint Used: `{st.secrets['AZURE_OPENAI_ENDPOINT']}`")
            st.write(f"- Error Message: `{str(e)}`")

# 6. Footer
st.markdown("<br><hr><center>Built by **Ayomide Zaccheaus** | 2026</center>", unsafe_allow_html=True)
