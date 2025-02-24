import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber pickups in NYC')

sidebar = st.sidebar
sidebar.title("Informacion.")
sidebar.image('identificacion.png') 
sidebar.text("""Christian Rodrigo Porfirio Castro
S21004519""")

DATE_COLUMN = 'date/time'
DATA_URL = 'uber_dataset.csv'

@st.cache  
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(columns=lowercase, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
