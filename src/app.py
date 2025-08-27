import streamlit as st
import pandas as pd
import os 

BASE_PATH = os.getcwd()
car = pd.read_csv(os.path.join(BASE_PATH, "data/cleaned_car_data.csv"))
st.title("Car Price Prediction")
company = st.selectbox("Select Company", options=car['company'].unique())
# base on car company i want car names
car_names = car[car['company'] == company]['name'].unique()
name = st.selectbox("Select Car Name", options=car_names)
fuel_type = st.selectbox("Select Fuel Type", options=car['fuel_type'].unique())
year = st.number_input("Enter Year", min_value=2000, max_value=2025)
kms_driven = st.number_input("Enter KMs Driven", min_value=0)

if st.button("Predict Price"):
    import joblib
    # model = joblib.load(os.path.join(BASE_PATH, "models/car_price_model.pkl"))
    model = joblib.load(os.path.join(BASE_PATH, "models/car_price_model.pkl"))
    input_df = pd.DataFrame([[name, company, year, kms_driven, fuel_type]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    price = model.predict(input_df)[0]
    st.success(f"The predicted price of the car is: ₹ {price:,.2f}")