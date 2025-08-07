# 💊 Medical Insurance Premium Predictor

Welcome to the **Medical Insurance Premium Predictor** — an intelligent web application that predicts medical insurance premiums based on user health and demographic details using machine learning.

## 🚀 Project Overview

This application uses a trained **Random Forest** or **Gradient Boosting** model to estimate the premium amount for a user based on factors such as age, height, weight, diseases, surgeries, and family medical history. 

It provides:
- 🎯 Real-time premium prediction (in USD & INR)
- 📊 Interactive data visualizations
- 🎙️ Voice interaction support (Flask + Speech Recognition)
- 🌐 Streamlit-based UI

---

## 🧠 Machine Learning Model

- **Model Used:** Random Forest / Gradient Boosting Regressor
- **Target Variable:** Insurance Premium
- **Input Features:**
  - Age
  - Diabetes
  - Blood Pressure Problems
  - Transplants
  - Chronic Diseases
  - Height & Weight
  - Allergies
  - Family History of Cancer
  - Number of Major Surgeries

---

## 📁 File Structure

📦 Medical-Premium-Predictor
├── App.py # Streamlit frontend app
├── voice.py # Flask + Voice-enabled backend API
├── medical.ipynb # Model training and exploration notebook
├── Medicalpremium.csv # Dataset used
├── MIPML (2).pkl # Trained model file
├── README.md # Project documentation (this file)

---

## 🛠️ Installation & Run Locally

### 🔹 Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/medical-insurance-premium-predictor.git
cd medical-insurance-premium-predictor

---

## 🛠️ Installation & Run Locally

### 🔹  Step 2: Install Dependencies
pip install -r requirements.txt
If requirements.txt is not available, install manually:
pip install streamlit pandas numpy seaborn matplotlib scikit-learn gTTS speechrecognition flask joblib

🖥️ Usage
✅ Run the Streamlit App
bash
Copy
Edit
streamlit run App.py
✅ Run the Voice-Enabled Flask API
bash
Copy
Edit
python voice.py
Then send a POST request to http://127.0.0.1:5000/predict with:

json
Copy
Edit
{
  "features": [28, 0, 1, 0, 0, 170, 65, 0, 0, 1]
}
🧪 Sample Input
Feature	Value
Age	28
Diabetes	No (0)
Blood Pressure	Yes (1)
Transplants	No (0)
Chronic Diseases	No (0)
Height	170
Weight	65
Allergies	No (0)
Family History Cancer	No (0)
Major Surgeries	1
📊 Visualizations
Age distribution

Premium price distribution

Height vs Weight scatter plot colored by premium

📣 Voice Features
Speech input using microphone

Text-to-speech output for results

👨‍💻 Author
Developed by AM & Team 🚀

📄 License
This project is open-source and available under the MIT License.
