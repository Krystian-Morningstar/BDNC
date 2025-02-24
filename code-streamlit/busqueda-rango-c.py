import streamlit as st
import pandas as pd

@st.cache_data
def cargar_dataset():
    return pd.read_csv("dataset.csv", index_col=0)

df = cargar_dataset()

st.header("Consulta de Nombres por Rango de Índices")

inicio_rango = st.text_input("Introduzca el índice inicial:")
fin_rango = st.text_input("Introduzca el índice final:")

if st.button("Ejecutar búsqueda"):
    if inicio_rango.isdigit() and fin_rango.isdigit():
        inicio, fin = int(inicio_rango), int(fin_rango)
        
        if inicio <= fin:
            resultados = df.iloc[inicio:fin+1]
            st.subheader(f"Total de resultados: {len(resultados)}")
            st.dataframe(resultados)
        else:
            st.warning("El valor de inicio debe ser menor o igual al valor final.")
    else:
        st.warning("Ingrese números válidos en ambos campos.")
