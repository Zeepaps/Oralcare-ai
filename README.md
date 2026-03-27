# 🦷 OralCare AI: Multi-Agent Dental Triage System (Nigeria)

A specialized **Multi-Agent GenAI System** built during my internship at **Dataraflow**. This application leverages a sequential agent pipeline to provide real-time dental triage and facility referrals for users across Nigeria.

---

##  Project Overview
OralCare AI addresses the critical gap in dental health accessibility. In many regions, professional dental advice is delayed; this system acts as a "First-Response" diagnostic dashboard. It processes patient symptoms through a specialized AI pipeline to categorize urgency and provide localized hospital referrals.

> **Note:** This project utilizes a custom **Mockup Dataset** of 1,000+ Nigerian dental patient profiles (simulating age, location, sugar intake, and pain levels) to demonstrate data-driven decision-making.

---

## 🏗️ Multi-Agent Architecture
The system uses a **Sequential Pipeline Pattern**. Each agent has a specific "System Prompt" and responsibility, passing its findings to the next stage of the report.

### 🤖 The Agent Team
| Agent Role | Responsibility | Logic Pattern |
| :--- | :--- | :--- |
| **SymptomAnalyst** | Performs clinical triage based on pain, swelling, and bleeding. | **Triage Logic** |
| **DietaryRiskAgent** | Analyzes lifestyle impact (e.g., sugar intake) on future oral health. | **Risk Assessment** |
| **AccessOrchestrator** | Maps the user to the nearest Nigerian Teaching Hospital (LUTH, UCH, UNTH, etc.). | **Geospatial Referral** |

---

## 🛠️ Tech Stack
* **Core Logic:** Python 3.10+
* **LLM Integration:** Azure OpenAI (GPT-4o) / Rule-based Agent Logic
* **Web Framework:** [Streamlit](https://streamlit.io)
* **Data Science:** Pandas, NumPy (for processing the 1,000-row patient dataset)
* **Deployment:** Streamlit Community Cloud
* **Visualization:** Native Streamlit Charts (Bar charts for regional pain-level trends)

---

##  Project Requirements Coverage
- **[x] Real/Mock Dataset (500+ rows):** Uses a generated 1,000-row `nigerian_dental_data.csv`.
- **[x] 3+ Specialized Agents:** SymptomAnalyst, DietaryRiskAgent, and AccessOrchestrator.
- **[x] Multi-Agent Pattern:** Implements a Sequential Workflow.
- **[x] Custom Tools:** Functional Python tools for `calculate_risk` and `get_clinic` mapping.
- **[x] Data Visualization:** Interactive bar charts showing regional dental trends.
- **[x] User Interface:** Full Streamlit dashboard with sidebar inputs and metric cards.

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

