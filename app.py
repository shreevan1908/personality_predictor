import streamlit as st
import pandas as pd
import joblib  # or pickle

# Load your saved model
model = joblib.load("personality_predictor.pkl")

# Title
st.title("🧠 Personality Predictor")

# Inputs from user
time_alone = st.slider("Time Spent Alone", 0.0, 10.0)
stage_fear = st.selectbox("Stage Fear", ["Yes", "No"])
event_attendance = st.slider("Social Event Attendance", 0.0, 10.0)
going_out = st.slider("Going Outside", 0, 10)
drained = st.selectbox("Drained After Socializing", ["Yes", "No"])
friends = st.slider("Friends Circle Size", 0.0, 20.0)
post_freq = st.slider("Post Frequency", 0.0, 10.0)

# Convert inputs
stage_fear_val = 1 if stage_fear == "Yes" else 0
drained_val = 1 if drained == "Yes" else 0

# Predict button
if st.button("Predict Personality"):
    input_data = pd.DataFrame([[time_alone, stage_fear_val, event_attendance,
                                going_out, drained_val, friends, post_freq]],
                              columns=['Time_spent_Alone', 'Stage_fear', 'Social_event_attendance',
                                       'Going_outside', 'Drained_after_socializing',
                                       'Friends_circle_size', 'Post_frequency'])

    prediction = model.predict(input_data)[0]
    personality = "Introvert" if prediction == 1 else "Extrovert"

    st.success(f"🧠 Predicted Personality: {personality}")