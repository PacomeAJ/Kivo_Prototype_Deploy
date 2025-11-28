import os
import streamlit as st
from PIL import Image

# -----------------------------
# APP CONFIG
# -----------------------------
st.set_page_config(page_title="KIVO AI", page_icon="🤖", layout="centered")

# -----------------------------
# SIDEBAR INSTRUCTIONS
# -----------------------------
st.sidebar.header("KIVO Demo Instructions")
st.sidebar.markdown("""
- Select a question below to see KIVO's response.
- This is a pre-written demo using sample data.
- Judges can see decision, reasoning, confidence, source, and supporting evidence.
""")

# -----------------------------
# ADDITIONAL NOTE
# -----------------------------
st.sidebar.header("Additional Information")
st.sidebar.markdown("""
- This demo showcases how KIVO simplifies complex processes, enhances accuracy, and empowers businesses to make faster, data-driven decisions. Experience the future of intelligent billing today.
- For any additional questions or support, feel free to contact us.
""")

# -----------------------------
# LOAD LOGO
# -----------------------------
logo_path = os.path.join("assets", "kivo_logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
else:
    logo = None
    st.warning("⚠️ KIVO logo not found. Make sure it's in assets/kivo_logo.png")

# -----------------------------
# HEADER WITH LOGO INLINE
# -----------------------------
if logo:
    col1, col2 = st.columns([1, 4])  # Adjust ratio: 1 for logo, 4 for text
    with col1:
        st.image(logo, width=250)  # Adjust width as needed
    with col2:
        st.markdown("## KIVO: Instant Billing Intelligence")
else:
    st.markdown("## KIVO: Instant Billing Intelligence")

st.write("Ask KIVO any billing question from the demo below:")

# -----------------------------
# DEMO QUESTIONS & PRE-WRITTEN ANSWERS
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
            "Reason": "CarrierZ submitted a certified weight ticket that matches the freight description and NMFC weight guidelines.",
            "Confidence": "94%",
            "Source": "CarrierZ_WeightCertificate.pdf — Seal 772199; BOL.pdf — Line Item 3",
            "Supporting Evidence": ["Original Declared Weight: 4,980 lbs", "Carrier Reweigh Weight: 5,040 lbs", "Difference: +60 lbs (1.2% variance)"]
        }
    },
    {
        "question": "CarrierABC changed the freight from Class 85 to Class 250 for load #334455. Should we dispute this?",
        "answer": {
            "Decision": "Dispute",
            "Reason": "Density and NMFC classification do not support a class increase from 85 to 250.",
            "Confidence": "97%",
            "Source": "NMFC_DensityTable.pdf; CarrierABC_Tariff.pdf",
            "Supporting Evidence": ["Shipment characteristics align with Class 85", "No commodity attributes justify Class 250", "Increase results in inflated charge"]
        }
    }
]

# -----------------------------
# USER INTERFACE (Buttons for Questions)
# -----------------------------
st.subheader("Choose a question to ask KIVO:")

for q in demo_questions:
    if st.button(q["question"]):  # Create a button for each question
        answer = q["answer"]
        
        # -----------------------------
        # Highlighting specific words in response
        # -----------------------------
        highlighted_answer = answer["Decision"]
        highlighted_answer = highlighted_answer.replace("Deny", f"<span style='color:red;'>❌ Deny</span>")
        highlighted_answer = highlighted_answer.replace("Approve", f"<span style='color:green;'>✅ Approve</span>")
        highlighted_answer = highlighted_answer.replace("Dispute", f"<span style='color:blue;'>ℹ️ Dispute</span>")

        # -----------------------------
        # Display Answer
        # -----------------------------
        st.subheader("KIVO Answer")
        
        # Highlighted decision
        st.markdown(f"**Decision:** {highlighted_answer}", unsafe_allow_html=True)
        
        # Display other details
        for k, v in answer.items():
            if k != "Decision":
                if isinstance(v, list):
                    st.write(f"**{k}:**")
                    for item in v:
                        st.write(f"- {item}")
                else:
                    st.write(f"**{k}:** {v}")

# -----------------------------
# THANK YOU SECTION / CALL TO ACTION
# -----------------------------
st.markdown("""
    ### Thank you for experiencing KIVO AI!

    We appreciate your time in exploring KIVO, and we'd love to hear your thoughts on the demo.

    Please share your feedback with us to help us improve. 

    [Jean Anno - KIVO Prototype AI Demo - Feedback - Fill out form](https://forms.office.com/Pages/ResponsePage.aspx?id=jkIKfbCgsOe3NbLc3ZV1eXjLp60xVbZMiGUKgfxJBA5URE5JWFIZSFUxUENTRUIoUThCMTAxWTVHQS4u)  

    Stay tuned for more updates, and thank you for your support!
""")
