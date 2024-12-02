import streamlit as st
from PIL import Image
from Photos.photo_link import main_dir

logo_path = main_dir("logo_issea.jpg")
logo = Image.open(logo_path)
def accueil_load(): 
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
        Explorez les données sur le marché du travail en Afrique avec des visualisations interactives et des analyses prédictives.
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
        - **About us:** Une présentation de tous les membres de la Data Storytellers Team.
       """
    )
    st.markdown("---")
    st.markdown("""
                Version 1.0 du 2 décembre 2024
                """)
