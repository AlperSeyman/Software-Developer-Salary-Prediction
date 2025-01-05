import streamlit as st 
import numpy as np
from prediction_page import prediction_page
from expoler_page import expoler_page

page = st.sidebar.selectbox("Explore or Predict",("Predict","Expoler"))

if page == "Predict":
    prediction_page()
else:
    expoler_page()