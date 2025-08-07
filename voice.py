import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load and preprocess data
data = pd.read_csv("Medicalpremium.csv")
X = data.drop("premium", axis=1)
y = data["premium"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "Medicalpremium.pkl")
import speech_recognition as sr
from gtts import gTTS
import os

# Speech recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."

# Text-to-speech
def speak_text(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    os.system("start response.mp3")
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("medical_premium_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict([data["features"]])
    return jsonify({"predicted_premium": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)


