import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()

def check_column():
    if "name" not in df.columns:
        st.error("El archivo CSV debe contener una columna llamada 'nombre'")
        return False
    return True

if check_column():
    st.title("Búsqueda de Nombres en CSV")
    
    search_query = st.text_input("Ingrese un nombre:")
    
    if search_query:
        filtered_df = df[df["name"].str.contains(search_query, case=False, na=False)]
        
        st.write(f"Número de coincidencias encontradas: {len(filtered_df)}")
        
        st.dataframe(filtered_df)
    else:
        st.write("Ingrese un término de búsqueda para comenzar.")

st.markdown("___")
st.image('identificacion.png')
st.text("Christian Rodrigo Porfirio Castro - S21004519") 