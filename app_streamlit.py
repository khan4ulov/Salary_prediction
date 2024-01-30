"""
Salary Prediction Preogram
@author: Awesh Khan
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("C:\\Users\\Administrator\\Desktop\\Salary_program\\salary_predition.pkl", "rb")

model=pickle.load(pickle_in)

def welcome():
    return "Salary Prediction Program "

def predict_salary(YearsExperience):
   
    prediction=model.predict([[YearsExperience]])
    print(prediction)
    return prediction

def main():
    st.title("------------Predicting Salary------------")
    st.markdown(
        """
        <style>
            body {
                background-color: #F9E795;
            }
            .stButton button {
                background-color: #CBD18F;
                color: black;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .stButton button:hover {
                background-color: #FCEDDA;
                transform: scale(1.05);
            }
            #app-title {
                background-color: #CCF381;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                margin-bottom: 10px;
            }
            .stButton button[data-baseweb="button"] {
                background-color: #FF5733;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .stButton button[data-baseweb="button"]:hover {
                background-color: #FCEDDA;
                transform: scale(1.05);
            }
            .css-1sna17z {
                text-align: center !important;
            }
            .stTitle {
                text-align: center !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div id="app-title">
            <h2 style="color: white;">Streamlit Salary Prediction App </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    years_experience = st.text_input("YearsExperience", "Type Here")
    result = ""

    if st.button("Predict"):
        try:
            years_experience_numeric = eval(years_experience)
            if isinstance(years_experience_numeric, (int, float)):
                result = predict_salary(years_experience_numeric)[0]  # Extract the first element
                result = str(result)  # Convert to string
            else:
                st.warning("Please enter a valid numeric value.")
        except:
            st.warning("Please enter a valid numeric value.")

    st.success(f'The expected Salary is {result}')

    if st.button("Know More"):
        st.markdown("### About the Salary Prediction Model")
        st.write("This salary prediction model is based on machine learning.")
        st.write("It takes the number of years of experience as input and predicts the expected salary.")
        st.write("The model was trained using a dataset of historical salary and experience data.")
        st.write("Feel free to explore and use the app!")
if __name__ == "__main__":
    main()
