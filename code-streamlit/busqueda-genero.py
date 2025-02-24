import streamlit as st
import pandas as pd

@st.cache_data
def obtener_datos():
    return pd.read_csv("dataset.csv")

data = obtener_datos()

st.title("Búsqueda de Registros por Género")

genero_seleccionado = st.selectbox("Seleccione una opción:", ["Masculino", "Femenino"])

if st.button("Buscar"):
    filtro = "M" if genero_seleccionado == "Masculino" else "F"
    datos_filtrados = data[data["sex"] == filtro]
    cantidad = len(datos_filtrados)
    
    st.write(f"Total de registros encontrados: {cantidad}")
    st.dataframe(datos_filtrados)

st.markdown("___")
st.image('identificacion.png')
st.text("Christian Rodrigo Porfirio Castro - S21004519") 
