import streamlit as st
import pandas as pd
import pickle

# Set page config
st.set_page_config(page_title="Real Estate Price Prediction", layout="centered")

# Load the pre-trained model
model_path = './real_estate_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Inject custom CSS for background image and centering
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1568605114967-8130f3a36994");
        background-size: cover;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.9);
        padding: 2rem;
        border-radius: 10px;
        max-width: 600px;
        margin: 200px auto;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🏠 Real Estate Price Prediction")
st.markdown("Enter the property details below to predict the **house price per unit area.**")

# Input form
with st.form(key='prediction_form'):
    distance_to_mrt = st.number_input("Distance to the nearest MRT station (in meters)", min_value=0.0, step=10.0)
    num_convenience_stores = st.number_input("Number of convenience stores", min_value=0)
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")
    
    submit = st.form_submit_button(label='Predict Price')

# Prediction
if submit:
    if None not in [distance_to_mrt, num_convenience_stores, latitude, longitude]:
        features = pd.DataFrame([[distance_to_mrt, num_convenience_stores, latitude, longitude]],
            columns=['Distance to the nearest MRT station', 'Number of convenience stores', 'Latitude', 'Longitude'])
        
        prediction = model.predict(features)[0]
        st.success(f"💰 Predicted House Price: {prediction:.2f} per unit area")
    else:
        st.warning("Please fill in all input fields.")
