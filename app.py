
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Diabetes Risk Prediction", page_icon="🩺", layout="wide")

try:
    model = joblib.load("Final_Diabetes_RF_Model.pkl")
    selected_features = joblib.load("Selected_Features.pkl")
except FileNotFoundError:
    st.error("Model files not found. Place the .pkl files in the same folder as app.py.")
    st.stop()

st.title("🩺 Diabetes Risk Prediction System")
st.markdown("---")
st.write("This application predicts diabetes using the trained Random Forest model.")

st.sidebar.title("Navigation")
st.sidebar.info("Machine Learning Project\n\nModel: Random Forest\nFeature Selection: Top 10 SHAP Features")

st.header("📝 Enter Patient Information")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 1, 120, 40)
    gender = st.selectbox("Gender", ["Male","Female"])
    polyuria = st.selectbox("Polyuria", ["No","Yes"])
    polydipsia = st.selectbox("Polydipsia", ["No","Yes"])
    sudden_weight_loss = st.selectbox("Sudden Weight Loss", ["No","Yes"])
with col2:
    partial_paresis = st.selectbox("Partial Paresis", ["No","Yes"])
    itching = st.selectbox("Itching", ["No","Yes"])
    irritability = st.selectbox("Irritability", ["No","Yes"])
    polyphagia = st.selectbox("Polyphagia", ["No","Yes"])
    alopecia = st.selectbox("Alopecia", ["No","Yes"])

gender = 1 if gender=="Male" else 0
polyuria = 1 if polyuria=="Yes" else 0
polydipsia = 1 if polydipsia=="Yes" else 0
sudden_weight_loss = 1 if sudden_weight_loss=="Yes" else 0
partial_paresis = 1 if partial_paresis=="Yes" else 0
itching = 1 if itching=="Yes" else 0
irritability = 1 if irritability=="Yes" else 0
polyphagia = 1 if polyphagia=="Yes" else 0
alopecia = 1 if alopecia=="Yes" else 0

input_data = pd.DataFrame({
"Polyuria":[polyuria],
"Polydipsia":[polydipsia],
"Gender":[gender],
"sudden weight loss":[sudden_weight_loss],
"partial paresis":[partial_paresis],
"Itching":[itching],
"Irritability":[irritability],
"Polyphagia":[polyphagia],
"Alopecia":[alopecia],
"Age":[age]
})

input_data = input_data[selected_features]

if st.button("🔍 Predict Diabetes Risk", use_container_width=True):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    probability_percent = probability*100
    status = "Positive" if prediction==1 else "Negative"

    if probability_percent <20:
        risk="Very Low Risk"
    elif probability_percent<40:
        risk="Low Risk"
    elif probability_percent<60:
        risk="Moderate Risk"
    elif probability_percent<80:
        risk="High Risk"
    else:
        risk="Very High Risk"

    st.markdown("---")
    c1,c2,c3=st.columns(3)
    c1.metric("Diabetes Status",status)
    c2.metric("Probability",f"{probability_percent:.2f}%")
    c3.metric("Risk Category",risk)

    st.subheader("Prediction Confidence")
    st.progress(float(probability))

    with st.expander("Patient Information"):
        st.dataframe(input_data,use_container_width=True)

st.markdown("---")
st.caption("Educational purpose only. This application is not a substitute for professional medical advice.")
