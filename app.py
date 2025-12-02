# app.py
import os
import streamlit as st
from PIL import Image

# -----------------------------
# LOAD LOGO
# -----------------------------
logo_path = os.path.join("assets", "kivo_logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
else:
    logo = None
    st.warning("⚠️ KIVO logo not found. Place it inside assets/kivo_logo.png")

# -----------------------------
# PAGE SETUP
# -----------------------------
st.set_page_config(
    page_title="KIVO Instant Billing Intelligence",
    page_icon="💠",
    layout="wide"
)

# -----------------------------
# SIDEBAR (KIVO DEMO INSTRUCTIONS)
# -----------------------------
with st.sidebar:
    if logo:
        st.image(logo, width=180)

    st.header("KIVO Demo Instructions")
    st.markdown("""
    - Select a question below to see KIVO's response.  
    - This is a pre-written demo using sample data.  
    - Judges can see decision, reasoning, confidence, source, and supporting evidence.  
    """)

    st.header("Additional Information")
    st.markdown("""
    - This demo showcases how KIVO simplifies complex processes, enhances accuracy,  
      and empowers businesses to make faster, data-driven decisions.  
    - Experience the future of intelligent billing today.  
    """)

# -----------------------------
# HEADER (Blue bar like screenshot)
# -----------------------------
st.markdown(
    """
    <div style="
        background-color:#2B6CB0;
        padding: 18px;
        border-radius: 8px;
        display:flex;
        align-items:center;
    ">
        <h2 style="color:white; margin:0;">KIVO – Instant Billing Intelligence</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# DEMO QUESTIONS & ANSWERS
# -----------------------------
demo_questions = [
    {
        "question": "Carrier billed 4 hours of detention for load #447788. Should we deny it?",
        "answer": {
            "Decision": "Deny",
            "Reason": "POD timestamps show only 1.3 hours of waiting, below the 2-hour threshold.",
            "Confidence": "90%",
            "Source": "Customer_Contract.pdf — Page 2, Section 1.4",
            "Supporting Evidence": ["Arrived: 14:05", "Checked Out: 15:22", "Total Wait: 1.28 hours"]
        }
    },
    {
        "question": "Is the reweigh from CarrierZ valid for load #889900?",
        "answer": {
            "Decision": "Approve",
            "Reason": "CarrierZ submitted a certified weight ticket that matches the freight description.",
            "Confidence": "94%",
            "Source": "CarrierZ_WeightCertificate.pdf — Seal 772199; BOL.pdf — Line Item 3",
            "Supporting Evidence": ["Declared: 4,980 lbs", "Reweigh: 5,040 lbs", "+60 lbs (1.2% variance)"]
        }
    },
    {
        "question": "CarrierABC changed the freight from Class 85 to Class 250 for load #334455. Should we dispute this?",
        "answer": {
            "Decision": "Dispute",
            "Reason": "Density and NMFC classification do not support a class increase.",
            "Confidence": "97%",
            "Source": "NMFC_DensityTable.pdf; CarrierABC_Tariff.pdf",
            "Supporting Evidence": ["Fits Class 85", "Class 250 unjustified", "Charge inflated"]
        }
    }
]

# -----------------------------
# USER INSTRUCTION TEXT
# -----------------------------
st.write("### Ask KIVO any billing question from the demo below:")

# -----------------------------
# DROPDOWN SELECT BOX WITH FIRST QUESTION PRE-SELECTED
# -----------------------------
questions_list = [q["question"] for q in demo_questions]
selected_question = st.selectbox(
    "Select a scenario:",
    questions_list,
    index=0  # Pre-select the first question
)

# Clear previous chat_history to show only current selection
st.session_state.chat_history = [{"sender": "user", "text": selected_question}]

# -----------------------------
# FIND ANSWER FOR SELECTED QUESTION
# -----------------------------
for q in demo_questions:
    if q["question"] == selected_question:
        answer = q["answer"]
        break

# -----------------------------
# HIGHLIGHT DECISION
# -----------------------------
decision = answer["Decision"]
if decision == "Deny":
    decision = "<span style='color:red;'>❌ Deny</span>"
elif decision == "Approve":
    decision = "<span style='color:green;'>✅ Approve</span>"
else:
    decision = "<span style='color:blue;'>ℹ️ Dispute</span>"

# -----------------------------
# DISPLAY KIVO ANSWER
# -----------------------------
st.subheader("KIVO Answer")
st.markdown(f"**Decision:** {decision}", unsafe_allow_html=True)

for k, v in answer.items():
    if k != "Decision":
        if isinstance(v, list):
            st.write(f"**{k}:**")
            for item in v:
                st.write(f"- {item}")
        else:
            st.write(f"**{k}:** {v}")

# -----------------------------
# FOOTER / THANK YOU
# -----------------------------
st.write("---")
st.markdown("""
### Thank you for experiencing **KIVO AI**

Please share your feedback to help us improve:

👉 [**Submit Feedback**](https://forms.office.com/Pages/ResponsePage.aspx?id=JkIKfbCgs0e3NbLc3ZV1eXjLp60xVbZMiGUKgfxJBA5UOFVFMkRGQkZHVU41M1VDNTNPV0E2T0E2T01NMS4u)
""")
