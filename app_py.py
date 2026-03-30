import streamlit as st
import pandas as pd
from openai import AzureOpenAI

# 1. Page Config
st.set_page_config(page_title="OralCare AI - Nigeria", page_icon="🦷", layout="wide")

# 2. Azure OpenAI Client Setup (Pulls from Secrets)
client = AzureOpenAI(
    api_key=st.secrets["AZURE_OPENAI_API_KEY"],  
    api_version="2024-02-15-preview",
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
)

# 3. Professional Styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦷 OralCare AI: Multi-Agent Triage")
st.write("_Powered by Azure GPT-4o_")
st.markdown("---")

# 4. Sidebar Inputs
st.sidebar.header("📋 Patient Profile")
location = st.sidebar.selectbox("Location", ["Lagos", "Abuja", "Ibadan", "Kano", "Enugu"])
sugar = st.sidebar.select_slider("Daily Sugar Intake", options=["Low", "Medium", "High"])
pain = st.sidebar.slider("Pain Level (0-10)", 0, 10, 5)
swelling = st.sidebar.checkbox("Is there any visible swelling?")

# 5. The "Brain" - Multi-Agent Function
def get_ai_diagnosis(sugar, pain, swelling, location):
    # This acts as the "Orchestrator" Agent
    prompt = f"""
    You are a Dental Triage AI for Nigeria. 
    Patient Data:
    - Location: {location}
    - Pain: {pain}/10
    - Swelling: {swelling}
    - Sugar Intake: {sugar}

    Provide a 2-sentence professional assessment and suggest a specific Nigerian hospital from this list: 
    LUTH (Lagos), National Hospital (Abuja), UCH (Ibadan), AKTH (Kano), or UNTH (Enugu).
    """
    
    response = client.chat.completions.create(
        model=st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"],
        messages=[{"role": "system", "content": "You are a helpful dental assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 6. Run Analysis
if st.button("🚀 Run AI Triage Analysis"):
    with st.spinner("SymptomAnalyst & AccessOrchestrator agents are communicating..."):
        # Real AI Call
        ai_report = get_ai_diagnosis(sugar, pain, swelling, location)
        
        # Display Results
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Pain Intensity", value=f"{pain}/10")
        with col2:
            st.metric(label="Status", value="AI Analyzed")

        with st.expander("📄 Official AI Medical Report", expanded=True):
            st.write(ai_report)
            st.info("Note: This is an AI assessment for triage purposes only.")

# Footer
st.markdown("<br><hr><center>Built by [Your Name] | Dataraflow Internship 2026</center>", unsafe_allow_html=True)
