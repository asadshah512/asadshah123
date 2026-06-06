import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"
    df = pd.read_csv(url)
    df = df.dropna(subset=['Total', 'ShareWomen', 'Unemployment_rate'])
    return df
