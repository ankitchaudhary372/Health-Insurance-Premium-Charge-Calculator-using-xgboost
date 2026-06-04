import pandas as pd
import streamlit as st
import joblib



st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered"
)



st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

h1 {
    text-align: center;
    color: #1f77b4;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
}

div[data-testid="stMetric"] {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)



model = joblib.load("insurance_prediction.pkl")



st.markdown("""
# 🏥 Insurance Cost Prediction App

Enter your details below and get an estimated insurance cost instantly.
""")



st.sidebar.title("ℹ️ About")

st.sidebar.info(
    """
    This application predicts insurance cost using a Machine Learning model.

    Model Used:
    - XGBoost Regressor
    - OneHotEncoder
    - StandardScaler
    - Scikit-Learn Pipeline

    Developed using:
    - Python
    - Streamlit
    - XGBoost
    """
)



with st.form("insurance_form"):

    st.subheader("📝 Enter Applicant Details")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=5,
        value=0
    )

    smoker = st.selectbox(
        "Smoker",
        ["yes", "no"]
    )

    region = st.selectbox(
        "Region",
        [
            "southeast",
            "southwest",
            "northwest",
            "northeast"
        ]
    )

    medical_history = st.selectbox(
        "Medical History",
        [
            "NO",
            "Diabetes",
            "High blood pressure",
            "Heart disease"
        ]
    )

    family_medical_history = st.selectbox(
        "Family Medical History",
        [
            "NO",
            "High blood pressure",
            "Diabetes",
            "Heart disease"
        ]
    )

    exercise_frequency = st.selectbox(
        "Exercise Frequency",
        [
            "Never",
            "Rarely",
            "Occasionally",
            "Frequently"
        ]
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Blue collar",
            "White collar",
            "Student",
            "Unemployed"
        ]
    )

    coverage_level = st.selectbox(
        "Coverage Plan",
        [
            "Basic",
            "Standard",
            "Premium"
        ]
    )

    submit = st.form_submit_button(
        "🔍 Predict Insurance Cost"
    )


if submit:

    input_df = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region],
        "medical_history": [medical_history],
        "family_medical_history": [family_medical_history],
        "exercise_frequency": [exercise_frequency],
        "occupation": [occupation],
        "coverage_level": [coverage_level]
    })

    prediction = model.predict(input_df)

    st.success("✅ Prediction Generated Successfully")

    st.metric(
        label="Estimated Insurance Cost",
        value=f"₹ {prediction[0]:,.2f}"
    )

    with st.expander("📄 View Input Data"):
        st.dataframe(input_df)



st.markdown("---")
st.caption(
    "Built with Streamlit | Machine Learning Insurance Cost Prediction Project"
)