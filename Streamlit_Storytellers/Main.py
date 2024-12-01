import streamlit as st
import sys
from pathlib import Path

# Ajouter le dossier parent au PYTHONPATH
sys.path.append(str(Path(__file__).parent.resolve()))

from Pages_utiles.About_us  import about_us_page
#from Streamlit_Storytellers.Pages_utiles.Dashboard_pop_active import dash_pop_active
from Pages_utiles.Accueil import accueil_load
import altair as alt
import openpyxl
import os# utiliser pour le chemin d'accès

def main_dir(script_path):
    main=os.path.dirname(__file__)
    return  os.path.join(main_dir, script_path)
#data_full_path = os.path.join(main_dir, "Datas/africa_employment_data.xlsx")
#@st.cache
#def load_data():
#    return pd.read_excel(data_full_path)

st.set_page_config(
    page_title="African Employment Dashboard",
    page_icon="🧑‍💼",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
display: flex;
justify-content: center;
align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

</style>
""", unsafe_allow_html=True)

# Barre latérale pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Aller à :", ["Accueil","Dashboard_pop_active","About Us"])

if page == "About Us":
    about_us_page()
elif page=="Dashboard_pop_active":
    st.write("hello")#dash_pop_active()
else:
    st.write("accueil")
    #accueil_load()

