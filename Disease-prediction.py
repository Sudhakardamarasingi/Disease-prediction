import streamlit as st

# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="Disease Prediction", page_icon="🩺", layout="centered")

# ---------------- HEADER ----------------
st.markdown(
    """
    <h2 style='text-align:center; color:#4CAF50;'>🩺 Disease Prediction from Symptoms</h2>
    <p style='text-align:center; color:gray;'>
        Select symptoms from the list or enter them manually.<br>
        The model will predict the most likely disease.
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- SYMPTOM LIST ----------------
# Example symptom list (expand this with your dataset)
symptom_list = [
    "fever", "cough", "headache", "fatigue", "sore throat", "nausea", 
    "vomiting", "diarrhea", "chest pain", "breathlessness", "dizziness",
    "runny nose", "muscle pain", "loss of appetite", "rash"
]

# ---------------- MULTISELECT OPTION ----------------
selected_symptoms = st.multiselect(
    "🔍 Select your symptoms from the list:",
    options=symptom_list,
    help="You can select multiple symptoms by clicking on them or typing in the box."
)

st.markdown("---")

# ---------------- MANUAL INPUT (OPTIONAL) ----------------
manual_input = st.text_area(
    "✍️ Or enter symptoms manually (comma or space separated):",
    placeholder="e.g. fever, cough, headache"
)

# Combine symptoms (both ways)
final_symptoms = selected_symptoms.copy()

if manual_input.strip():
    manual_list = [s.strip().lower() for s in manual_input.replace(",", " ").split()]
    final_symptoms.extend(manual_list)

# ---------------- PREDICTION BUTTON ----------------
if st.button("🔮 Predict Disease", use_container_width=True):
    if final_symptoms:
        # ---- Replace this with your ML model prediction ----
        result = "Bronchial Asthma"   # Example placeholder
        st.success(f"✅ Predicted Disease: **{result}**")
    else:
        st.warning("⚠️ Please select or enter at least one symptom.")

# ---------------- FOOTER ----------------
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray; font-size:13px;'>
        Built with ❤️ using Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
