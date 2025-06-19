import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Heart Disease Prediction App 🫀")

age = st.number_input("Age", min_value = 1, max_value = 100, step = 1)
sex = st.selectbox("sex",  ["Male", "Female"])
cp = st.selectbox("Enter chest pain" , ["Typical Angina (0)", "Atypical Angina (1)", "Non-anginal Pain (2)", "Asymptomatic (3)"])
trestbps = st.number_input("Enter bp ", min_value=50, max_value=250, step=1)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, step=1)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["True", "False"])
restecg = st.selectbox("Resting ECG Results", ["Normal (0)", "Having ST-T wave abnormality (1)", "Probable or definite left ventricular hypertrophy (2)"])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=250, step=1)
exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.number_input("Oldpeak (ST depression)", step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Upsloping (0)", "Flat (1)", "Downsloping (2)"])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thal", ["Normal (0)", "Fixed Defect (1)", "Reversible Defect (2)"])


sex = 1 if sex == "Male" else 0
cp = int(cp[-2])           # e.g., "Non-anginal Pain (2)" -> 2
fbs = 1 if fbs == "True" else 0
restecg = int(restecg[-2])  # e.g., "Having ST-T wave abnormality (1)" -> 1
exang = 1 if exang == "Yes" else 0
slope = int(slope[-2])
thal = int(thal[-2])

if st.button("Predict"):
    input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    input_data = input_data.reshape(1, 13)
    prediction = model.predict(input_data)
    if (prediction==1):
        st.error("⚠️ The model predicts the patient *has* heart disease.")
    else:
        st.success("✅ The model predicts the patient *does not have* heart disease.")

