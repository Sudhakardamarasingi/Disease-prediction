import streamlit as st
import joblib

# Load pipeline
@st.cache_resource
def load_model():
    return joblib.load("disease_pipeline.pkl")

model = load_model()

st.title("🩺 Disease Prediction from Symptoms")

symptoms = st.text_area("Enter symptoms (comma/space separated):", placeholder="e.g. fever, cough, headache")

if st.button("Predict"):
    if symptoms.strip():
        pred = model.predict([symptoms])[0]
        st.success(f"**Predicted Disease:** {pred}")
    else:
        st.warning("Please enter symptoms first!")
