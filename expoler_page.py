import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def shorten_categories(categories, limit):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= limit:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    return categorical_map

def clean_expreince(x):
    if x == "Less than 1 year":
        return 0.5
    return float(x)

def clean_education(x):
    if 'Professional degree' in x:
        return 'Professional degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    return 'Less than Bachelors'

@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country","EdLevel", "YearsCodePro","Employment","ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly":"Salary"}, axis = 1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    
    category_map = shorten_categories(df["Country"].value_counts(), 350)
    df["Country"] = df["Country"].map(category_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_expreince)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df


df = load_data()

def expoler_page():
    st.title("Expoler Software Engineer Salary ")
    st.write("""#### Stack Overflow Annual Developer Survey 2024""")


    data = df["Country"].value_counts()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)

