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


