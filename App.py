import streamlit as st
import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
import seaborn as sns

# Exchange rate (Example: 1 USD = 84.85 INR)
USD_TO_INR = 84.85
# Load the trained model
model = pkl.load(open('MIPML (2).pkl', 'rb'))

# App Title and Description
st.set_page_config(page_title="Medical Insurance Premium Predictor", page_icon="💊", layout="wide")
st.title("Medical Insurance Premium Predictor 💰")
st.write("Bridge the gap between health and affordability—calculate your premium now!"
)
st.write("Predict your medical insurance premium based on various health and demographic factors. Interact with the tool below to get insights.")

# Sidebar for Input
st.sidebar.header("Input Parameters")
st.sidebar.write("Provide the details below:")

# User Input Form
def user_inputs():
    Name =st.text_input("What is your name?")
    if Name:
     st.write(f"Hello, {Name} Welcome!")

    age = st.sidebar.slider("Age", 18, 100, 30)
    diabetes = st.sidebar.selectbox("Diabetes", ["No", "Yes"])
    blood_pressure = st.sidebar.selectbox("Blood Pressure Problems", ["No", "Yes"])
    transplants = st.sidebar.selectbox("Any Transplants", ["No", "Yes"])
    chronic_diseases = st.sidebar.selectbox("Any Chronic Diseases", ["No", "Yes"])
    height = st.sidebar.slider("Height (cm)", 100, 250, 170)
    weight = st.sidebar.slider("Weight (kg)", 30, 200, 70)
    allergies = st.sidebar.selectbox("Known Allergies", ["No", "Yes"])
    cancer_family = st.sidebar.selectbox("History of Cancer in Family", ["No", "Yes"])
    major_surgeries = st.sidebar.slider("Number of Major Surgeries", 0, 10, 0)

    # Convert categorical inputs to numerical
    diabetes = 1 if diabetes == "Yes" else 0
    blood_pressure = 1 if blood_pressure == "Yes" else 0
    transplants = 1 if transplants == "Yes" else 0
    chronic_diseases = 1 if chronic_diseases == "Yes" else 0
    allergies = 1 if allergies == "Yes" else 0
    cancer_family = 1 if cancer_family == "Yes" else 0

    return np.array([age, diabetes, blood_pressure, transplants, chronic_diseases,
                     height, weight, allergies, cancer_family, major_surgeries])

# Predict Premium
input_features = user_inputs()
if st.sidebar.button("Predict Premium"):
    prediction_usd = model.predict(input_features.reshape(1, -1))[0]
    prediction_inr = prediction_usd * USD_TO_INR
    st.success(f"🏥 Your Predicted Insurance Premium is: **${prediction_usd:.2f} USD**")

    st.success(f"💵 Converted Premium in INR: **₹{prediction_inr:,.2f}**")

# Fancy Visualization Section
st.write("---")
st.subheader("Explore Data Insights 📊")

# Sample Dataset Visualization (using Seaborn)
try:
    # Assume the dataset is already loaded as `df` in the provided file
    import pandas as pd
    df = pd.read_csv('Medicalpremium.csv')

    # Plot distributions
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Age Distribution")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df['Age'], kde=True, color="blue", ax=ax)
        st.pyplot(fig)

    with col2:
        st.write("### Premium Price Distribution")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df['PremiumPrice'], kde=True, color="green", ax=ax)
        st.pyplot(fig)

    # Scatter plot
    st.write("### Height vs Weight Scatter Plot")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=df['Height'], y=df['Weight'], hue=df['PremiumPrice'], palette="viridis", ax=ax)
    st.pyplot(fig)

except Exception as e:
    st.error("Could not load the dataset for visualizations. Please check the dataset path.")
    st.write(e)

# Footer
st.write("---")
st.markdown("Developed by AM & Team🚀")
