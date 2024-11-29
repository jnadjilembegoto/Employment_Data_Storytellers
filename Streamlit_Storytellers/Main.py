import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl
import os# utiliser pour le chemin d'accès

script_dir = os.path.dirname(__file__)
data_full_path = os.path.join(script_dir, "Datas/africa_employment_data.xlsx")


# Charger les données
@st.cache
def load_data():
    return pd.read_excel(data_full_path)

data = load_data()

# Titre de l'application
st.title("Analyse Interactive : Emploi et Insertion Professionnelle en Afrique")
st.markdown("""
    Explorez les données sur le marché du travail en Afrique avec des visualisations interactives et des analyses prédictives.
    Cette application combine des cartes, des graphiques et des modèles prédictifs pour fournir des insights clés.
""")

# Section : Sélecteurs pour filtrer les données
st.sidebar.header("Filtres")
year = st.sidebar.slider("Sélectionnez une année :", int(data["Year"].min()), int(data["Year"].max()), 2020)
countries = st.sidebar.multiselect("Choisissez les pays :", data["Country"].unique())

# Filtrage des données
filtered_data = data[data["Year"] == year]
if countries:
    filtered_data = filtered_data[filtered_data["Country"].isin(countries)]

# Section 1 : Carte interactive (Choropleth)
st.subheader("Carte Interactive : Taux de Chômage en Afrique")
fig_map = px.choropleth(
    data_frame=filtered_data,
    locations="Country",
    locationmode="country names",
    color="Unemployment Rate",
    title=f"Taux de chômage en {year}",
    color_continuous_scale="Viridis",
    labels={"Unemployment Rate": "Taux de chômage (%)"}
)
st.plotly_chart(fig_map)



# Section 3 : Prédiction du Taux de Chômage
st.subheader("Prédiction du Taux de Chômage")
st.markdown("""
    À partir des données historiques, nous prédisons le taux de chômage pour une année donnée en utilisant un modèle de régression linéaire.
""")



# Interface pour prédire un taux de chômage
input_data = {col: st.number_input(f"Entrez la valeur pour {col} :", min_value=0.0, max_value=100.0, step=1.0) for col in range(10)}
if st.button("Prédire"):
    st.write(f"**Taux de chômage prédit :** %")

# Section : Résumé et recommandations
st.subheader("Conclusions")
st.markdown("""
- Les cartes interactives révèlent des disparités géographiques importantes dans le taux de chômage.
- Les jeunes restent les plus vulnérables, ce qui nécessite des efforts accrus en matière de formation et d'insertion professionnelle.
- Les prédictions montrent le potentiel des données pour guider des politiques ciblées.
""")
