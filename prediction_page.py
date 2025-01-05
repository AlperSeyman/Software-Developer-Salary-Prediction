import streamlit as st 
import pickle
import numpy as np



def load_model():
    with open("saved_steps.pkl","rb") as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
country_encoder = data["country_encoder"]
education_encoder = data["education_encoder"]



def prediction_page():
    st.title("Software Developer Salary Prediction")
    st.write("""#### We need information to predict the salary""")

    countries = (
        "United States of America",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Ukraine",
        "India",
        "France",
        "Canada",
        "Brazil",
        "Spain",
        "Italy",
        "Netherlands",
        "Australia",
        "Sweden"
    )

    education = (
        "Professional degree",
        "Master’s degree",
        "Less than Bachelors",
        "Bachelor’s degree",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education)

    expreince = st.slider("Years of Expreince",0, 50, 4)

    button = st.button("Calculate Salary")
    if button:
        X = np.array([[country, education, expreince]])
        X[:, 0] = country_encoder.transform(X[:,0])
        X[:, 1] = education_encoder.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")






