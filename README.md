## 🦷 OralCare AI: Multi-Agent Dental Triage System

**A Generative AI Solution for Accessible Oral Healthcare in Nigeria**

OralCare AI addresses the critical gap in dental health accessibility. In many regions, professional dental advice is delayed; this system acts as a **"First-Response" diagnostic dashboard**. It processes patient symptoms through a specialized Generative AI pipeline to categorize urgency and provide localized hospital referrals.

---

### 🎓 Academic & Professional Context
* **Program:** Generative AI & Data Science Course
* **Internship:** Dataraflow Data Science Program
* **Focus:** Multi-Agent Orchestration, Azure OpenAI Integration, and Healthcare Analytics.

---

###  Live Demo
🔗 **oralcare-ai.streamlit.app**
<video src="[1fdb7316-2a70-496b-a10e-a2ba3d9b02a2.webm](https://github.com/user-attachments/assets/f14e50d6-c0cb-4c8f-b30b-618fbfb8c69f)" width="100%" controls>
  Your browser does not support the video tag.

</video> (https://github.com/user-attachments/assets/7f3d59ad-42df-4596-82cf-3fb49e2931d1)


---

###  Technical Architecture: The "Multi-Agent" Pipeline
Unlike standard chatbots, OralCare AI utilizes a **Multi-Agent Orchestration** pattern. When a patient submits data, the system triggers two specialized agents via **Azure OpenAI (GPT-4o)**:

1.  **SymptomAnalyst Agent:** Evaluates clinical variables (Pain level, Age, Swelling, Bleeding) to determine triage urgency.
2.  **PatientCounselor Agent:** Analyzes lifestyle factors (e.g., Sugar Intake) to provide empathetic, personalized health advice and reduce patient anxiety.
3.  **AccessOrchestrator:** Maps the patient's location to the nearest Nigerian tertiary health institution (e.g., LUTH, UCH, AKTH).

---

### 📊 Data & Insights
This project utilizes a custom **Synthetic Dataset** of 1,000+ Nigerian dental patient profiles. 
* **Key Features:** Age, Location (Lagos, Abuja, etc.), Sugar Intake, and Pain Intensity.
* **Visualization:** Integrated Streamlit charts to show regional dental trends, simulating how a healthcare administrator would monitor public health.

---

### 💻 Tech Stack
* **Frontend:** Streamlit (Python-based Web Framework)
* **LLM Provider:** Azure OpenAI Service (GPT-4o)
* **Data Handling:** Pandas & NumPy
* **Security:** Streamlit Secrets Management (Environment Variables)

---

### 📂 Project Structure
```text
├── app.py                   # Main Application Logic & AI Agents
├── requirements.txt         # Python Dependencies (Streamlit, OpenAI)
├── nigerian_dental_data.csv    # Synthetic Patient Dataset
└── README.md                # Project Documentation
---

## 🔧 Installation & Local Setup
**1. Clone the repo**
```bash
git clone https://github.com/zeepaps/oralcare-ai.git
cd oralcare-ai
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

## 📊 Feature Highlights & Agents
[SymptomAnalyst] 
- Role: Emergency Triage
- Input: Pain Level, Swelling, Bleeding
- Output: Urgency Category (Red/Yellow/Green)

[DietaryRiskAgent]
- Role: Preventive Analysis
- Input: Sugar Consumption, Brushing Habits
- Output: Future Decay Risk Score

[AccessOrchestrator]
- Role: Regional Referral
- Input: Patient Location (State-level)
- Output: Nearest Tertiary Dental Center (LUTH, UCH, etc.)

 ## 👩🏾‍💻 Author & Professional Identity
**Ayomide Zaccheaus**

- Role: Data Science Intern at Dataraflow
- Project: GenAI Multi-Agent Assignment
- GitHub: [@zeepaps](https://github.com/zeepaps)
- ORCID: [0009-0004-0488-172X](https://orcid.org/0009-0004-0488-172X)

---

