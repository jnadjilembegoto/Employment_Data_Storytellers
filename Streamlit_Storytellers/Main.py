import streamlit as st


from Pages_utiles.About_us  import about_us_page
from Pages_utiles.Dashboard_pop_active import dash_pop_active
from Pages_utiles.Accueil import accueil_load
from Pages_utiles.Secteur_prof_ais import dash_secteur_pro_ais
from Pages_utiles.Taux_emploi import dash_taux_emploi
from Pages_utiles.Taux_chomage import dash_chom
from Pages_utiles.Taux_emploi_informel import dash_sect_informel
from Pages_utiles.Chef_d_entreprise import dash_chef_entreprise
import altair as alt
import openpyxl


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
page = st.sidebar.selectbox("Aller à :", ["Accueil","Dynamique de la population active","Emploi-Activité économique","Aperçu de l'emploi","Coup d'oeil sur le chômage","Emploi informel","About Us"])

if page == "About Us":
    about_us_page()
elif page=="Dynamique de la population active":
    dash_pop_active()
elif page=="Emploi-Activité économique":
    dash_secteur_pro_ais()
elif page=="Aperçu de l'emploi":
    dash_taux_emploi()
elif page=="Coup d'oeil sur le chômage":
    dash_chom()
elif page=="Emploi informel":
    dash_sect_informel()
elif page=="Inégalité dans les postes manageriaux":
    dash_chef_entreprise()
else:
    accueil_load()

