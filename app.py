# app.py

import os
import time
import streamlit as st
from PIL import Image

# -----------------------------
# PAGE SETUP (must be first)
# -----------------------------
st.set_page_config(
    page_title="KIVO Instant Billing Intelligence",
    page_icon="💠",
    layout="wide"
)

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
# SIDEBAR (with full KIVO demo instructions)
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
# HEADER
# -----------------------------
st.markdown("""
<div style="background-color:#2B6CB0; padding:18px; border-radius:8px;">
    <h2 style="color:white; margin:0;">KIVO – Instant Billing Intelligence</h2>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# DEMO DATA
# -----------------------------
demo_questions = [
    {
        "question": "Carrier billed 4 hours of detention for load #447788. Should we deny it?",
        "answer": {
            "Decision": "Deny",
            "Reason": "POD timestamps show only 1.3 hours of waiting, below the 2-hour threshold.",
            "Confidence": "90%",
            "Source": "Customer_Contract.pdf — Page 2, Section 1.4",
            "Supporting Evidence": [
                "Arrived: 14:05",
                "Checked Out: 15:22",
                "Total Wait: 1.28 hours"
            ]
        }
    },
    {
        "question": "Is the reweigh from CarrierZ valid for load #889900?",
        "answer": {
            "Decision": "Approve",
            "Reason": "CarrierZ submitted a certified weight ticket that matches the freight description.",
            "Confidence": "94%",
            "Source": "CarrierZ_WeightCertificate.pdf — Seal 772199",
            "Supporting Evidence": [
                "Declared: 4,980 lbs",
                "Reweigh: 5,040 lbs",
                "+60 lbs variance"
            ]
        }
    },
    {
        "question": "CarrierABC changed freight class from 85 to 250. Should we dispute?",
        "answer": {
            "Decision": "Dispute",
            "Reason": "Density and NMFC classification do not support increase.",
            "Confidence": "97%",
            "Source": "NMFC_DensityTable.pdf",
            "Supporting Evidence": [
                "Fits Class 85",
                "Class 250 unjustified"
            ]
        }
    }
]

# -----------------------------
# SELECT QUESTION
# -----------------------------
st.write("### Ask KIVO a billing question:")
questions_list = [q["question"] for q in demo_questions]
selected_question = st.selectbox("Select scenario:", questions_list)

# -----------------------------
# FIND ANSWER
# -----------------------------
for q in demo_questions:
    if q["question"] == selected_question:
        answer = q["answer"]

# -----------------------------
# AI THINKING EFFECT
# -----------------------------
with st.spinner("KIVO is analyzing the request..."):
    time.sleep(1.5)

# -----------------------------
# FORMAT DECISION
# -----------------------------
decision = answer["Decision"]
if decision == "Deny":
    decision_html = "<span style='color:red;'>❌ Deny</span>"
elif decision == "Approve":
    decision_html = "<span style='color:green;'>✅ Approve</span>"
else:
    decision_html = "<span style='color:blue;'>ℹ️ Dispute</span>"

# -----------------------------
# DISPLAY RESPONSE
# -----------------------------
st.write("---")
st.subheader("KIVO Decision")
st.markdown(f"### {decision_html}", unsafe_allow_html=True)
st.write(f"**Reason:** {answer['Reason']}")
st.write(f"**Confidence:** {answer['Confidence']}")
st.write(f"**Source:** {answer['Source']}")
st.write("**Supporting Evidence:**")
for item in answer["Supporting Evidence"]:
    st.write(f"- {item}")

# -----------------------------
# FOOTER / FEEDBACK FORM
# -----------------------------
st.write("---")
st.markdown("""
<h3>Thank you for experiencing <b>KIVO AI</b></h3>
<p>Please share your feedback:<br> <i>(RXO login required)</i></p>
<div style="margin-top:15px;">
    <a href="https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=JkIKfbCgs0e3NbLc3ZV1eXjLp60xVbZMiGUKgfxJBA5URE5JWFIZSFUxUENTRUI0UThCMTAxWTVHQS4u" target="_blank" 
       style="background-color:#2B6CB0; color:white; padding:12px 24px; border-radius:6px; text-decoration:none; font-size:16px; font-weight:600;">
       Submit Feedback
    </a>
</div>
""", unsafe_allow_html=True)