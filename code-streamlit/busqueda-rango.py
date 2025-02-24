import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos():
    return pd.read_csv("dataset.csv", index_col=0)

datos = cargar_datos()

st.title("Búsqueda de Nombres por Índice")

indice_inicio = st.text_input("Ingrese el índice de inicio:")
indice_fin = st.text_input("Ingrese el índice de fin:")

if st.button("Buscar nombres en el rango"):
    if indice_inicio.isdigit() and indice_fin.isdigit():
        inicio, fin = int(indice_inicio), int(indice_fin)
        
        if inicio <= fin:
            resultado = datos.iloc[inicio:fin+1] 
            st.write(f"Se encontraron {len(resultado)} registros.")
            st.dataframe(resultado)
        else:
            st.error("El índice de inicio debe ser menor o igual al índice de fin.")
    else:
        st.error("Por favor, ingrese valores numéricos válidos.")
        
st.markdown("___")
st.image('identificacion.png')
st.text("Christian Rodrigo Porfirio Castro - S21004519") 