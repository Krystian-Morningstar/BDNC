import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)

sidebar = st.sidebar

sidebar.title("Informacion.")
sidebar.image('identificacion.png') 
sidebar.text("""Christian Rodrigo Porfirio Castro
S21004519""")


fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)

st.markdown("___")

fig2, ax2 = plt.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic?')

st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)

st.markdown("___")

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)