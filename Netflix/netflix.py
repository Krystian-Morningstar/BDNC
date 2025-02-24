import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos(n_filmes=1000):
    try:
        df = pd.read_csv("movies.csv", encoding="utf-8", nrows=n_filmes)
    except UnicodeDecodeError:
        df = pd.read_csv("movies.csv", encoding="latin1", nrows=n_filmes)  # Alternativa en caso de error
    return df

movies_df = cargar_datos()

st.title("Netflix Recommender System")
st.write("Este es un sistema de recomendación de películas de Netflix.")

st.sidebar.image('identificacion.png') 
st.sidebar.text("""Christian Rodrigo Porfirio Castro
S21004519""")

st.sidebar.markdown("______")

st.sidebar.header("Opciones de Visualización")
mostrar_todos = st.sidebar.checkbox("Mostrar todas las peliculas")

if mostrar_todos:
    cantidad_total = len(movies_df)
    st.write(f"Lista de peliculas - ({cantidad_total} registros):")
    st.dataframe(movies_df)
    st.markdown("______")

st.sidebar.header("Buscar Pelicula por Título")
titulo_busqueda = st.sidebar.text_input("Ingrese el título")
if st.sidebar.button("Buscar"):
    resultado_busqueda = movies_df[movies_df["name"].str.contains(titulo_busqueda, case=False, na=False)]
    cantidad_busqueda = len(resultado_busqueda)
    st.write(f"Se encontraron {cantidad_busqueda} coincidencias")
    st.dataframe(resultado_busqueda)

st.sidebar.header("Filtrar peliculas por Director")
director_seleccionado = st.sidebar.selectbox("Seleccione un director:", movies_df["director"].dropna().unique())
if st.sidebar.button("Filtrar por Director"):
    filmes_director = movies_df[movies_df["director"] == director_seleccionado]
    cantidad_director = len(filmes_director)
    st.write(f"Peliculas dirigidas por {director_seleccionado} ({cantidad_director} registros):")
    st.dataframe(filmes_director)
