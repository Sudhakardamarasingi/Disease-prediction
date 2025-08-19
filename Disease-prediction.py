import streamlit as st
import joblib

model = joblib.load("log_reg_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Disease Prediction App")

symptoms = st.text_area("Enter symptoms:")

if st.button("Predict"):
    if symptoms.strip():
        X_input = vectorizer.transform([symptoms])
        prediction = model.predict(X_input)[0]
        st.success(f"Predicted Disease: {prediction}")
    else:
        st.warning("Please enter symptoms.")


