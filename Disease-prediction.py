import streamlit as st
import joblib

# --- MODEL LOADING ---
# Load your trained machine learning pipeline
@st.cache_resource
def load_model():
    try:
        return joblib.load("disease_pipeline.pkl")
    except FileNotFoundError:
        return None

model = load_model()

# --- UI CONFIG ---
st.set_page_config(page_title="Disease Prediction", page_icon="🩺", layout="centered")

# --- HEADER ---
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

# --- SYMPTOM LIST ---
# This list is used for the dropdown selector
symptom_list =['itching','skin-rash','nodal-skin-eruptions','dischromic-patches','continuous-sneezing','shivering','chills','watering-from-eyes','stomach-pain',
               'acidity','ulcers-on-tongue','vomiting','cough','chest-pain','yellowish-skin','nausea','loss-of-appetite','abdominal-pain','yellowing-of-eyes',
               'burning-micturition','spotting-','urination','passage-of-gases','internal-itching','indigestion','muscle-wasting','patches-in-throat','high-fever',
               'extra-marital-contacts','fatigue','weight-loss','restlessness','lethargy','irregular-sugar-level','blurred-and-distorted-vision','obesity',
               'excessive-hunger','increased-appetite','polyuria','sunken-eyes','dehydration','diarrhoea','breathlessness','family-history','mucoid-sputum',
               'headache','dizziness','loss-of-balance','lack-of-concentration','stiff-neck','depression','irritability','visual-disturbances','back-pain',
               'weakness-in-limbs','neck-pain','weakness-of-one-body-side','altered-sensorium','dark-urine','sweating','muscle-pain','mild-fever',
               'swelled-lymph-nodes','malaise','red-spots-over-body','joint-pain','pain-behind-the-eyes','constipation','toxic-look-(typhos)','belly-pain',
               'yellow-urine','receiving-blood-transfusion','receiving-unsterile-injections','coma','stomach-bleeding','acute-liver-failure','swelling-of-stomach',
               'distention-of-abdomen','history-of-alcohol-consumption','fluid-overload','phlegm','blood-in-sputum','throat-irritation','redness-of-eyes','sinus-pressure',
               'runny-nose','congestion','loss-of-smell','fast-heart-rate','rusty-sputum','pain-during-bowel-movements','pain-in-anal-region','bloody-stool',
               'irritation-in-anus','cramps','bruising','swollen-legs','swollen-blood-vessels','prominent-veins-on-calf','weight-gain','cold-hands-and-feets',
               'mood-swings','puffy-face-and-eyes','enlarged-thyroid','brittle-nails','swollen-extremeties','abnormal-menstruation','muscle-weakness','anxiety',
               'slurred-speech','palpitations','drying-and-tingling-lips','knee-pain','hip-joint-pain','swelling-joints','painful-walking','movement-stiffness',
               'spinning-movements','unsteadiness','pus-filled-pimples','blackheads','scurring','bladder-discomfort','foul-smell-of','urine','continuous-feel-of-urine',
               'skin-peeling','silver-like-dusting','small-dents-in-nails','inflammatory-nails','blister','red-sore-around-nose','yellow-crust-ooze']


# --- CHECK IF MODEL IS LOADED ---
if model is None:
    st.error("Model file 'disease_pipeline.pkl' not found. Please ensure it's in the same directory as the script.")
else:
    # --- MULTISELECT OPTION ---
    selected_symptoms = st.multiselect(
        "🔍 Select your symptoms from the list:",
        options=symptom_list,
        help="You can select multiple symptoms by clicking on them or typing in the box."
    )
    st.markdown("---")

    # --- MANUAL INPUT (OPTIONAL) ---
    manual_input = st.text_area(
        "✍️ Or enter symptoms manually (comma or - separated):",
        placeholder="e.g. fever, cough, headache,high-fever"
    )

    # Combine symptoms from both inputs
    final_symptoms = selected_symptoms.copy()
    if manual_input.strip():
        # Clean and split manual input
        manual_list = [s.strip().lower().replace(" ", "-") for s in manual_input.replace(",", " ").split() if s.strip()]
        final_symptoms.extend(s for s in manual_list if s not in final_symptoms)

    # --- PREDICTION BUTTON ---
    if st.button("🔮 Predict Disease", use_container_width=True):
        if final_symptoms:
            try:
                # 1. Process the input for the model
                # The pipeline expects a single string of space-separated symptoms
                input_string = " ".join(final_symptoms)

                # 2. Make the prediction
                prediction = model.predict([input_string])
                result = prediction[0]  # Get the first (and only) prediction

                st.success(f"✅ Predicted Disease: **{result}** \n *Consult a healthcare professional for an accurate diagnosis.*", icon="🩺")
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")
        else:
            st.warning("⚠️ Please select or enter at least one symptom.")

# --- FOOTER ---
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray; font-size:13px;'>
        A Machine Learning Application by Sudhakar Damarasingi
        


    </p>
    """,
    unsafe_allow_html=True
)





