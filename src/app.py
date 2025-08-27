from utils import db_connect
engine = db_connect()

# your code here
import pandas as pd
import json
import streamlit as st
import pickle
from pickle import load

# Cargar modelo
with open("/workspaces/E-Pablos-Regresion-Lineal/src/modelo_regresion_lineal_default.pkl", "rb") as file:
    model = pickle.load(file)

# Cargar columnas de JSON
with open("/workspaces/E-Pablos-Regresion-Lineal/src/sex_rules.json", "r") as f:
    sex_dic = json.load(f)

with open("/workspaces/E-Pablos-Regresion-Lineal/src/smoker_rules.json", "r") as f:
    smoker_dic = json.load(f)

st.title("Predicción de Coste de Seguro Médico")

st.write("Introduce tus datos y estima el precio de tu seguro médico")

age = st.number_input("Edad", 18, 100, 30)
children = st.number_input("Número de hijos", 0, 10, 0)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
sex_n = st.selectbox("Sexo", ["male", "female"])
smoker_n = st.selectbox("Fumador", ["yes", "no"])


sex_n = sex_dic[sex_n]
smoker_n = smoker_dic[smoker_n]


row = [[age,sex_n,bmi,children,smoker_n]]

print(row)

# Botón para predecir
if st.button("Calcular coste seguro"):
    prediction = model.predict(row)[0]
    st.write(f"Coste estimado del seguro: ${prediction:,.2f}")

