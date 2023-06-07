import streamlit as st
import pandas as pd

# Carga de datos simulada (puedes reemplazar esto con tus propios datos)
data = [
    { "name": "Ejemplo 1", "age": 25, "city": "Ciudad 1", "date": "2023-06-01" },
    { "name": "Ejemplo 2", "age": 30, "city": "Ciudad 2", "date": "2023-06-02" },
    { "name": "Ejemplo 3", "age": 35, "city": "Ciudad 3", "date": "2023-06-03" },
    { "name": "Ejemplo 4", "age": 40, "city": "Ciudad 1", "date": "2023-06-04" }
]

# Convertir los datos en un DataFrame de pandas
df = pd.DataFrame(data)

# Mostrar los datos en la aplicación de Streamlit
st.title("Aplicación con datos")

# Filtro de ciudad
selected_city = st.selectbox("Selecciona una ciudad", df["city"].unique())
filtered_data = df[df["city"] == selected_city]

# Filtro de fecha
start_date = st.date_input("Selecciona una fecha de inicio", value=pd.to_datetime(df["date"]).min())
end_date = st.date_input("Selecciona una fecha de fin", value=pd.to_datetime(df["date"]).max())
filtered_data = filtered_data[(pd.to_datetime(filtered_data["date"]) >= start_date) & (pd.to_datetime(filtered_data["date"]) <= end_date)]

# Mostrar tabla con filtros
st.write("Datos filtrados por ciudad y fecha:")
st.dataframe(filtered_data)
