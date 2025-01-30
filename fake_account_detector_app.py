import streamlit as st
import instaloader
import pandas as pd
import joblib

# Load the trained ML model
model = joblib.load("fake_account_detector_model.pkl")

# Function to fetch Instagram data using Instaloader
def fetch_instagram_data(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        data = {
            "Followers": profile.followers,
            "Following": profile.followees,
            "Posts": profile.mediacount,
            "Has_Profile_Pic": 1 if profile.profile_pic_url else 0,
        }
        return data
    except Exception as e:
        return {"error": f"Error fetching data: {str(e)}"}

# Function to predict using ML model
def predict_fake_account(data):
    if "error" in data:
        return data["error"]

    # Prepare the input data for the model
    input_data = pd.DataFrame([data])  # Convert to DataFrame
    prediction = model.predict(input_data)[0]  # Predict (0 = Fake, 1 = Real)
    probability = model.predict_proba(input_data)[0][prediction] * 100  # Probability
    
    return "Real Account ✅" if prediction == 1 else "Fake Account ❌", probability

# Streamlit app
st.title("Instagram Fake Account Detector")
st.markdown("**Enter an Instagram username below to detect if the account is real or fake using AI!**")

username = st.text_input("Instagram Username", placeholder="Enter username...")

if st.button("Check Account"):
    if username:
        with st.spinner("Analyzing the account..."):
            data = fetch_instagram_data(username)
            if "error" in data:
                st.error(data["error"])
            else:
                result, confidence = predict_fake_account(data)
                st.success(f"Prediction: {result}")
                st.info(f"Confidence Level: {confidence:.2f}%")
                st.write("**Account Details:**", data)
    else:
        st.warning("Please enter a username!")
