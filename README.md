<p align="center">
  <img src="banner.svg" alt="Disease Prediction App Banner" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Live_App-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/ML_Model-scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Dataset-Health_Data-0ea5e9?style=flat-square" />
  <img src="https://img.shields.io/badge/Author-Sudhakar_Damarasingi-6b21a8?style=flat-square" />
</p>

---

# 🩺 Disease Prediction App  
**Streamlit + Machine Learning Model (scikit-learn)**

### Live App: *(Add your live Streamlit link here)*

---

## 📘 Overview

This project is a **data-driven disease prediction system** built with a trained **Machine Learning model**, deployed using **Streamlit**.  
It predicts whether a person is at **High Risk** or **Low Risk** of developing a disease based on clinical and lifestyle indicators.

This project demonstrates:

- ML classification model deployment  
- Interactive UI using Streamlit  
- Preprocessing of user input  
- Real-time model inference  
- Clean interface for health prediction tools  

It is designed for educational use in **AI, data science, healthcare analytics, and ML deployment**.

---

## 🚀 Features

### 🔹 Disease Risk Prediction (Instant ML Inference)
Predicts high-risk or low-risk outcomes using a pre-trained ML model.

### 🔹 Probabilistic Output  
Displays confidence score or probability (if enabled in the model).

### 🔹 Clean & Modern UI  
- Dark/light Streamlit theme  
- User-friendly clinical input form  
- Risk result with visual cues  
- Responsive layout  

### 🔹 Secure Local Inference  
No external APIs.  
All predictions run entirely in the app using the `.pkl` ML model.

### 🔹 Deployed Online  
Runs 24/7 using Streamlit Cloud.  
Accessible from any device.

---

## 🧩 Tech Stack

| Layer | Technology |
|------|------------|
| Frontend UI | Streamlit |
| Backend Model | scikit-learn |
| Data Handling | pandas, numpy |
| Deployment | Streamlit Cloud |
| Serialization | pickle/joblib |

---

## 🏗️ Architecture

```
User → Streamlit UI → Preprocessing → ML Model (.pkl) → Prediction → UI Output
```

### Explanation:

- User enters health-related parameters  
- Streamlit converts inputs into a model-compatible array  
- Input is optionally scaled/preprocessed  
- The ML model (loaded from `model.pkl`) performs inference  
- Prediction + probability is displayed clearly to the user  

---

## 📤 Input Sample (User Form)

A typical user request contains:

```json
{
  "age": 45,
  "bmi": 29.5,
  "glucose": 120,
  "blood_pressure": 80,
  "cholesterol": 210,
  "exercise_level": "Low",
  "smoking": "Yes"
}
```

---

## 📥 ML Model Output Format

Example:

```json
{
  "risk": "High Risk",
  "confidence": 0.87
}
```

Your Streamlit app converts this response into:

- ❗ High Risk (red)  
OR  
- ✅ Low Risk (green)

---

## 🔧 Model & Preprocessing Configuration

Your ML model typically includes:

- Removal of missing values  
- Encoding of categorical features  
- Feature scaling (optional)  
- Training using algorithms like:
  - Logistic Regression  
  - Random Forest  
  - Gradient Boosting  
  - SVM  
  - XGBoost  

The trained classifier is saved as:

```
model.pkl
```

And loaded inside `app.py` like:

```python
model = pickle.load(open("model.pkl", "rb"))
```

---

## 🖥️ Streamlit Frontend

The Streamlit application:

- Accepts user’s clinical parameters  
- Structures them for ML input  
- Runs prediction using `model.pkl`  
- Shows clear results with risk indicators  
- Includes disclaimers and guidance  

---

## 📦 Installation (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📸 Screenshots (Add later)

You can include:

- Home screen  
- Input form  
- Prediction result UI  
- Model architecture workflow  

---

## 🧪 Testing Suggestions

Try inputs for:

- Low-risk profile (healthy metrics)  
- High-risk profile (poor metrics)  
- Extreme values and edge cases  
- Missing or invalid user inputs  
- Mixed categorical & numeric data  

Validate:

- Input range handling  
- Model inference accuracy  
- UI behavior  
- Probability output stability  

---

## 🔮 Future Enhancements

- Add SHAP model explainability  
- Display top contributing features  
- Add multiple disease models  
- Integrate EHR/FHIR structured input  
- Deploy a mobile version  
- Add voice-based input  
- Add plotting of risk trends  

---

## 👨‍💻 Author

**Sudhakar Damarasingi**  
AI/ML Engineer | Data Science Practitioner  

Built with ❤️ using **Streamlit** and **scikit-learn**  

---

<p align="center"><b>⭐ If you found this useful, please star the repository!</b></p>
