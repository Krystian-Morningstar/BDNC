import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def cargar_datos(n_registros=1000):
    try:
        df = pd.read_csv("citibike.csv", encoding="utf-8", nrows=n_registros)
    except UnicodeDecodeError:
        df = pd.read_csv("citibike.csv", encoding="latin1", nrows=n_registros)  # Alternativa en caso de error
    
    df.rename(columns={"start_lat": "lat", "start_lng": "lon"}, inplace=True)

    df["started_at"] = pd.to_datetime(df["started_at"], errors="coerce")
    
    return df

df = cargar_datos()

st.title("Análisis de recorridos en bicicleta 🚲")

st.sidebar.image('identificacion.png') 
st.sidebar.text("""Christian Rodrigo Porfirio Castro
S21004519""")
st.sidebar.markdown("______")
st.sidebar.header("Opciones de Visualización")

mostrar_todos = st.sidebar.checkbox("Mostrar todos los registros")
if mostrar_todos:
    st.write(f"Total de registros recuperados: {len(df)}")
    st.dataframe(df)
    st.markdown("______")

mostrar_grafica = st.sidebar.checkbox("Mostrar gráfica de recorridos", value=False)

st.sidebar.header("Gráfica de recorridos por hora")
df["hour"] = df["started_at"].dt.hour 
conteo_horas = df["hour"].value_counts().sort_index()  

fig, ax = plt.subplots()
ax.bar(conteo_horas.index, conteo_horas.values, color="blue")
ax.set_xlabel("Hora del día - 24hrs")
ax.set_ylabel("Número de recorridos")

hora_seleccionada = st.sidebar.slider("Seleccione una hora del día", min_value=0, max_value=23, value=12)

df_filtrado = df[df["hour"] == hora_seleccionada]

st.write(f"Mapa de recorridos iniciados a las {hora_seleccionada}:00 hrs")
st.map(df_filtrado)

st.markdown("____")

if mostrar_grafica:
    st.subheader("Gráfica de recorridos por hora")
    st.pyplot(fig)