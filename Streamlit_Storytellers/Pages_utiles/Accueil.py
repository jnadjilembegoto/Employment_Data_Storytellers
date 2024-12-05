import streamlit as st
from PIL import Image
from Photos.photo_link import main_dir

logo_path = main_dir("logo_issea.jpg")
logo = Image.open(logo_path)


def accueil_load(): 
    st.markdown("""
        <style>
        .stApp {
            background-color: #eaf6ff; /* Bleu clair inspiré de Stata */
        }
        .sidebar .sidebar-content {
            background-color: #d0e6f5; /* Bleu encore plus clair pour la barre latérale */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #1f77b4; /* Bleu Stata pour les titres */
        }
        .stButton>button {
            background-color: #1f77b4; /* Boutons Stata */
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    # Titre de l'application
        # Sidebar
    with st.sidebar:
        st.title('🏠 Accueil')
         
    
    col = st.columns((1.5, 4.5), gap='medium')
    with col[0]:
        st.image(logo,use_column_width=True)
    with col[1]:
        st.title("Compétition de Visualisation de Données - Journée Alumni ISSEA")
    st.markdown('---')
    st.title("Analyse Interactive : Emploi et Insertion Professionnelle en Afrique")
    st.markdown('Créé par DATA STorytellers Team')
    st.sidebar.markdown('---')
    st.sidebar.markdown("## Base de données utilisée")
    st.sidebar.markdown("""[*Données appurées*](https://github.com/jnadjilembegoto/Employment_Data_Storytellers)
                        """)
    st.sidebar.markdown('---')
    st.sidebar.markdown("## Scripts de l'application")
    st.sidebar.markdown("""[*Code de l'application*](https://github.com/jnadjilembegoto/Employment_Data_Storytellers)
                        """)
    st.markdown('---')
    st.markdown(
        """
        ### Résumé
        Explorez les données sur le marché du travail en Afrique avec des visualisations interactives.
        Cette application combine des cartes et des graphiques pour fournir des insights clés.

        Les détails de notre travail sont donnés dans le [*Notebook*](https://github.com/jnadjilembegoto/Employment_Data_Storytellers)
        
        """
    )
    st.markdown('---')

    st.markdown(
        """
        ### Utilisation de l'application

        A gauche se trouve le ménu déroulant pour naviguer dans les différents tableaux de board :

        - **Accueil:** We are here!
        - **Dynamique de la population active:** Un aperçu sur la proportion des personnes âgées de 15 à 64 ans dans un pays
        - **Emploi-Activité économique:** Une description des trois secteurs d'activités clés (agriculture, industrie et service)
        - **Aperçu de l'emploi:** Des analyses par pays, régionales et comparatives sur le taux d'emploi
        - **Coup d'oeil sur le chômage:** Des analyses similaires au taux d'emploi sont effectuées sur le taux de chômage
        - **Emploi informel:** Des analyses sur le taux d'emploi informel par région, pays et des analyses comparatives
        - **About us:** Une présentation de tous les membres de la Data Storytellers Team.
        - **Inégalité dans les postes manageriaux:** Une visualisation des proportions des chefs d'entreprises dans les pays au cours du temps
       """
    )
    st.markdown("---")
    st.markdown("""
                Version 1.0 du 2 décembre 2024
                """)
