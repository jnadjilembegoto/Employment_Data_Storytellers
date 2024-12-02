import streamlit as st

import pandas as pd
import plotly.graph_objects as go

import plotly.express as px

# Titre de l'application avec un fond blanc

from Datas.data_link import data_dir

def dash_taux_emploi():
    
    st.markdown("""
    <style>
    /* Ajuste la largeur totale du conteneur principal */
    [data-testid="stAppViewContainer"] {
        max-width: 100%; /* Ajustez la largeur à 95% de l'écran */
        padding-left: 0rem; /* Supprime les marges latérales */
        padding-right: 0rem;
        margin-left: auto;
        margin-right: auto;
    }

    /* Réduit les marges des blocs pour un meilleur alignement */
    [data-testid="block-container"] {
        padding: 1rem 0rem; /* Ajoute un espacement en haut et en bas uniquement */
    }

    /* Permet d'afficher plusieurs graphiques sur une même ligne */
    [data-testid="stHorizontalBlock"] > div {
        flex: 1; /* Répartit l'espace horizontalement */
        margin-right: 1rem; /* Ajoute un espace entre les colonnes */
    }

    /* Améliore la gestion des composants interactifs */
    [data-testid="stSidebar"] {
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)



    # Titre de l'application


    st.title("Apercu sur le taux d'emploi en Afrique")

    # Chargement des données
    # Load data
    #@st.cache_data
    def load_data():
         data_path=data_dir('base_streamlit_storytellers.xlsx')
         return pd.read_excel(data_path,sheet_name="Taux_emploi_chomage_Afrique")

    base = load_data()
    #""""""""""""""""""""""""""""""""""""""""""""""

    st.write("# 1.Analyse selon les régions Africaines")
    # importations toute la base
    st.write("##  1.1 Evolution du Taux d'emploi par Région et par sexe")
    


    Region_afrique=['Central Africa','Eastern Africa', 'Southern Africa', 'Western Africa','Northern Africa']

    data_region=base[base["Region"].isin(Region_afrique)]

    data_region_sexe=data_region[data_region["Age"]=="Age (Jeunes, adultes) : 15-64 ans"]


    # Sélection interactive de l'année


    selected_year = st.selectbox("Sélectionnez une année :", sorted(data_region_sexe["Annee"].unique()))

    # Filtrer les données pour l'année sélectionnée
    data_filtered = data_region_sexe[data_region_sexe["Annee"] == selected_year]

    # Pivot des données pour structurer les colonnes "Hommes", "Femmes", "Total"
    data_pivot = data_filtered.pivot(index="Region", columns="Sexe", values="Taux_emploi").reset_index()
    #col = st.columns((1,2), gap='medium')
    #with col[1]:
        # Création du graphique avec Plotly
    fig = go.Figure()

        # Ajout de la barre "Total"
    #if "Total" in data_pivot.columns:
    #       fig.add_trace(go.Bar(
    #           x=data_pivot['Region'],
    #          y=data_pivot['Total'],
    #         name="Total",
    #          marker_color='blue',
    #     ))

        # Ajout de la barre "Masculin"
    if "Masculin" in data_pivot.columns:
            fig.add_trace(go.Bar(
                x=data_pivot['Region'],
                y=data_pivot['Masculin'],
                name="Masculin",
                marker_color='red',
            ))

        # Ajout de la barre "Feminin"
    if "Feminin" in data_pivot.columns:
            fig.add_trace(go.Bar(
                x=data_pivot['Region'],
                y=data_pivot['Feminin'],
                name="Feminin",
                marker_color='cyan',
            ))

        # Mise en forme du graphique interactif avec Plotly
    fig.update_layout(
            title=f"Taux de d'emploi par région et sexe en {selected_year}",
            title_font_color="black",  # Couleur du titre en noir
            xaxis_title="Région",
            yaxis_title="Taux d'emploi (%)",
            xaxis_title_font_color="black",  # Couleur du titre de l'axe X
            yaxis_title_font_color="black",  # Couleur du titre de l'axe Y
            template="plotly_white",  # Utilisation du template Plotly White pour fond blanc
            barmode='group',  # Groupement des barres
            plot_bgcolor='white',  # Fond blanc pour le graphique
            paper_bgcolor='white',  # Fond blanc pour l'ensemble de l'application
            legend_title="Sexe",
            legend_title_font_color="black",  # Légende en noir
            legend_font_color="black",  # Texte de la légende en noir
            font=dict(color="black"),  # Texte général en noir
            height=600,  # Augmenter la hauteur du graphique pour une meilleure visibilité
        )

        # Affichage du graphique interactif dans Streamlit
    st.plotly_chart(fig)
    st.write("Source:Données issues de ILOSTAT")


    st.write("## 1.2 Analyse du taux d'emploi par Région et par Tranche d'âge de la population active")
    # Choix de la region
    selected_Region=st.selectbox("Filtrez selon la  Region d'Afrique :", Region_afrique)



    # Fonction pour tracer la courbe
    def plot_employment_rate_evolution(df, year_col='Annee', employment_col='Taux_emploi', age_col='Age'):
        """
        Tracer l'évolution du taux d'emploi en fonction des années et des catégories d'âge avec Plotly.

        Args:
            df (pd.DataFrame): DataFrame contenant les données.
            year_col (str): Nom de la colonne représentant les années.
            unemployment_col (str): Nom de la colonne représentant le taux de chômage.
            age_col (str): Nom de la colonne représentant les catégories d'âge.
            selected_age (str, optional): Tranche d'âge à afficher. Si None, toutes les catégories seront affichées.

        Returns:
            plotly.graph_objects.Figure: Graphique interactif.
        """
        
        fig = px.line (
            df,
            x=year_col,
            y=employment_col,
            color=age_col, 
            title="Évolution du taux de d'emploi",
            labels={"Année",  "Taux d'emploi",  "Tranche d'âge"}
        )
        fig.update_traces(mode="lines")  # Ajouter des points sur la courbe
        fig.update_layout(
            template="plotly_white",
            hovermode="x unified",
            xaxis_title="Année",
            yaxis_title="Taux d'emploi (%)",
            legend_title="Tranche d'âge"
        )
        return fig



    # Application Streamlit
    #st.title("Analyse de l'évolution du taux de d'emploi")
    #st.write("Sélectionnez une tranche d'âge pour visualiser son évolution ou affichez toutes les catégories.")



    data_region_age=data_region[data_region["Sexe"]=="Total"]

    # Affichage du graphique
    fig = plot_employment_rate_evolution(data_region_age[data_region_age["Region"]==selected_Region])
    st.plotly_chart(fig)
    #La source des données
    st.write("Source:Données issues de ILOSTAT")

    st.write("# 2.Analyse du taux de l'emploi selon les pays")
    Africa_pays=['Angola', 'Burundi', 'Benin', 'Burkina Faso', 'Botswana',
        "Côte d'Ivoire", 'Cameroon', 'Congo, Democratic Republic of the',
        'Congo', 'Comoros', 'Cabo Verde', 'Djibouti', 'Algeria', 'Egypt',
        'Ethiopia', 'Gabon', 'Ghana', 'Guinea', 'Gambia', 'Guinea-Bissau',
        'Kenya', 'Liberia', 'Libya', 'Lesotho', 'Morocco', 'Madagascar',
        'Mali', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi',
        'Namibia', 'Niger', 'Nigeria', 'Réunion', 'Rwanda', 'Sudan',
        'Senegal', 'Saint Helena', 'Sierra Leone', 'Somalia',
        'South Sudan', 'Sao Tome and Principe', 'Eswatini', 'Seychelles',
        'Chad', 'Togo', 'Tunisia', 'Tanzania, United Republic of',
        'Uganda','South Africa', 'Zambia', 'Zimbabwe']


    data_africa_pays=base[base["Region"].isin(Africa_pays)]


    #data1 = pd.read_excel("C:/Users/elias/Desktop/Competition/Taux_chomage.xlsx", sheet_name="Sexe_Age_Annee_Pays")

    #selected_pays = st.selectbox("Sélectionnez une année :", Africa_pays)
    data_africa_pays_age=data_africa_pays[data_africa_pays["Sexe"]=="Total"]

    select_pays=st.selectbox("Choisir le pays", Africa_pays)
    st.markdown(f"## 2.1 Evolution du Taux d'emploi dans le pays({select_pays}) suivant les catégories d'âges")
    data_select_pays=data_africa_pays_age[data_africa_pays_age["Region"]==select_pays]
    #st.title("Evolution du taux de chômage par pays et par âge")

    #col=st.columns(1,3)
    #witth col[1]:
    # Charger les données (ajustez cette ligne en fonction de votre source de données)
    # Exemple fictif de données


    def plot_employment_scatter_interactive(df: pd.DataFrame, age_col: str='Age', year_col: str='Annee', employment_col: str='Taux_emploi'):
        """
        Plots an interactive scatter plot of employment rate by age group and year.

        Args:
            df: The Pandas DataFrame containing the data.
            age_col: The column name for age.
            year_col: The column name for year.
            unemployment_col: The column name for employment rate.
        """
        # Create an interactive scatter plot using Plotly Express
        fig = px.scatter(
            df,
            x=year_col,
            y=employment_col,
            color=age_col,
            size=employment_col,  # Optional: size of points based on unemployment rate
            #title="Nuage de points : Taux de chômage par âge et par année",
            labels={year_col: "Année", employment_col: "Taux d'emploi", age_col: "Tranche d'âge"},
            hover_data={age_col: True, employment_col: True, year_col: True}
        )
        fig.update_layout(
            template="plotly_white",
            hovermode="closest"
        )
        # Show the interactive plot using Streamlit
        st.plotly_chart(fig)
    #La source des données
    st.write("Source:Données issues de ILOSTAT")


    st.write(f"Taux d'emploi par âge et par année  ({select_pays})")
    # Appel de la fonction pour afficher le graphique
    plot_employment_scatter_interactive(data_select_pays)


    st.write(f" ## 2.2 Evolution du Taux d'emploi par Sexe dans le pays  ({select_pays})")


    data_africa_pays_age=data_africa_pays[data_africa_pays["Age"]=="Age (Jeunes, adultes) : 15-64 ans"]

    data_africa_select_pays_age=data_africa_pays_age[data_africa_pays_age["Region"]==select_pays]

    data_africa_select_pays_age=data_africa_select_pays_age[data_africa_select_pays_age["Sexe"].isin(["Masculin","Feminin"])]
    def plot_employment_scatter_interactive(df: pd.DataFrame, Sexe_col: str='Sexe', year_col: str='Annee', employment_col: str='Taux_emploi'):
        """
        Plots an interactive scatter plot of employment rate by age group and year.

        Args:
            df: The Pandas DataFrame containing the data.
            age_col: The column name for age.
            year_col: The column name for year.
            employment_col: The column name for employment rate.
        """
        # Create an interactive scatter plot using Plotly Express
        fig = px.scatter(
            df,
            x=year_col,
            y=employment_col,
            color=Sexe_col,
            size=employment_col,  # Optional: size of points based on unemployment rate
            labels={year_col: "Année", employment_col: "Taux d'emploi", Sexe_col: "Sexe"},
            hover_data={Sexe_col: True,employment_col: True, year_col: True}
        )
        fig.update_layout(
            template="plotly_white",
            hovermode="closest"
        )
        # Show the interactive plot using Streamlit
        st.plotly_chart(fig)
    #La source des données
    st.write("Source:Données issues de ILOSTAT")
    plot_employment_scatter_interactive(data_africa_select_pays_age)



    st.write("## 3.Analyse comparative :Cartographie des pays Africains selon le taux d'emploi")
    st.write("### 3.1 Apercu général du taux d'emploi")
    data_africa_pays_age=data_africa_pays[data_africa_pays["Sexe"]=="Total"]
    data_africa_pays_Total=data_africa_pays_age[data_africa_pays_age["Age"]=="Age (Jeunes, adultes) : 15-64 ans"]

    selected_year=st.selectbox("Sélectionnez une année :", sorted(data_africa_pays_age["Annee"].unique()))
    # Selection de la couleur
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    ## Selection de l'année
    df_selected_year=data_africa_pays_Total[data_africa_pays_Total["Annee"]==selected_year]




    def make_choropleth(
        df_selected_year, 
        input_id, 
        input_column, 
        input_color_theme="red", 
        source_text="Source: Données officielles", 
        chart_title="Carte Choroplèthe - Taux d'emploi en Afrique en"+ " " +str(selected_year)
    ):
        """
        Crée une carte choroplèthe avec une interface personnalisée en blanc et détecte les pays sans données.

        Args:
            df_selected_year (pd.DataFrame): Données filtrées pour l'année sélectionnée.
            input_id (str): Colonne contenant les noms des pays.
            input_column (str): Colonne contenant les valeurs à afficher (ex. taux d'emploi).
            input_color_theme (str): Palette de couleurs à utiliser.
            source_text (str): Texte de la source à afficher en bas de la carte.
            chart_title (str): Titre de la carte.

        Returns:
            plotly.graph_objects.Figure: La carte choroplèthe.
        """
        
        # Vérifier si le DataFrame n'est pas vide
        if df_selected_year.empty or df_selected_year[input_column].isnull().all():
            st.error("Les données sont insuffisantes pour tracer la carte.")
            return None

        # Créer la carte choroplèthe
        choropleth = px.choropleth(
            data_frame=df_selected_year,
            locations=input_id,
            color=input_column,
            locationmode="country names",
            color_continuous_scale=input_color_theme,
            range_color=(0, max(df_selected_year[input_column])),
            scope="africa",
            labels={input_column: 'Taux emploi (%)'}
        )

        # Mise à jour de la mise en page avec un thème blanc
        choropleth.update_layout(
            template='plotly_white',  # Thème blanc
            plot_bgcolor='rgba(255, 255, 255, 1)',  # Couleur blanche pour le fond du graphique
            paper_bgcolor='rgba(255, 255, 255, 1)',  # Couleur blanche pour l'arrière-plan global
            margin=dict(l=0, r=0, t=50, b=50),  # Ajustement des marges
            height=400,  # Hauteur du graphique
            title=dict(
                text=chart_title,  # Titre personnalisé
                x=0.5,  # Centrage du titre
                xanchor='center',
                font=dict(size=16, color='black')  # Couleur et taille du texte du titre
            ),
            coloraxis_colorbar=dict(
                title="Taux d'emploi",
                tickvals=[0, max(df_selected_year[input_column]) / 2, max(df_selected_year[input_column])],
                ticktext=["Bas", "Moyen", "Haut"],
                titlefont=dict(size=14, color='black'),
                tickfont=dict(color='black')
            ),
            annotations=[
                dict(
                    text=source_text,  # Texte de la source
                    x=0.5,  # Position horizontale (centré)
                    y=-0.1,  # Position verticale (en bas, hors de la carte)
                    showarrow=False,  # Pas de flèche
                    xref="paper",  # Référence horizontale relative à la mise en page
                    yref="paper",  # Référence verticale relative à la mise en page
                    font=dict(size=12, color="black"),  # Style de police
                    align="center"  # Alignement du texte
                )
            ]
        )

        return choropleth


    ## Construction de la carte

    choropleth = make_choropleth(df_selected_year, "Region", "Taux_emploi",selected_color_theme)
    st.plotly_chart(choropleth, use_container_width=True)
    st.write("Sources:Données issues de ILOSTAT")
    #heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme)
    #st.altair_chart(heatmap, use_container_width=True)

    st.write("###  3.2 Analyse ds inégalités d'accès à l'emploi selon le sexe")
    st.write("### 3.2.1 Analyse comparative du taux d'emploi des hommes/Femmes en Afrique")
    #selected_sexe=st.selectbox("Filtre selon le sexe :",["Masculin","Feminin"])
    data_africa_pays_age=data_africa_pays[data_africa_pays["Sexe"]=="Masculin"]
    data_africa_pays_Total=data_africa_pays_age[data_africa_pays_age["Age"]=="Age (Jeunes, adultes) : 15-64 ans"]

    #selected_year=st.selectbox("Sélectionnez une année :", sorted(data_africa_pays_age["Annee"].unique()))
    # Selection de la couleur
    #color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    #selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    ## Selection de l'année

    df_selected_year_Hommes=data_africa_pays_Total[data_africa_pays_Total["Annee"]==selected_year]


    choropleth_hommes= make_choropleth(df_selected_year_Hommes,
                                "Region", 
                                "Taux_emploi", 
                                selected_color_theme,
                                source_text="Données issues de ILOSTAT",
                                chart_title="Taux d'emploi des Hommes en "+str(selected_year)

                                )



    data_africa_pays_age_Femmes=data_africa_pays[data_africa_pays["Sexe"]=="Feminin"]
    data_africa_pays_Total_Femmes=data_africa_pays_age_Femmes[data_africa_pays_age_Femmes["Age"]=="Age (Jeunes, adultes) : 15-64 ans"]

    df_selected_year_Femmes=data_africa_pays_Total_Femmes[data_africa_pays_Total_Femmes["Annee"]==selected_year]


    ## Cartographie Femmes

    choropleth_femmes= make_choropleth(df_selected_year_Femmes,
                                "Region", 
                                "Taux_emploi", 
                                selected_color_theme,
                                source_text="Source:Données issues de ILOSTAT",
                                chart_title="Taux d'emploi des Femmes en "+str(selected_year)

                                )


    col = st.columns(2)
    with col[0]:
        st.plotly_chart(choropleth_hommes, use_container_width=True)
    with col[1]:
        st.plotly_chart(choropleth_femmes, use_container_width=True)

    st.write("## 3.2 Inégalité d'accès à l'emploi selon l'âge")



    data_africa_pays_age1=data_africa_pays[data_africa_pays["Age"]=="Age (Jeunes, adultes) : 15-24 ans"]
    data_africa_pays_Total_age1=data_africa_pays_age1[data_africa_pays_age1["Sexe"]=="Total"]

    df_selected_year_age1=data_africa_pays_Total_age1[data_africa_pays_Total_age1["Annee"]==selected_year]

    choropleth_age1= make_choropleth(df_selected_year_age1,
                                "Region", 
                                "Taux_emploi", 
                                selected_color_theme,
                                source_text="Données issues de ILOSTAT",
                                chart_title="Taux d'emploi des jeunes de 15-24 ans en "+str(selected_year)

                                )



    st.write("Source:Données issues de ILOSTAT")
    #selected_color_theme="reds"
    # Inegalités dans l'accès à l'emploi les jeunes de 25-64 ans
    data_africa_pays_age2=data_africa_pays[data_africa_pays["Age"]=="Age (Jeunes, adultes) : 25-64 ans"]
    data_africa_pays_Total_age2=data_africa_pays_age2[data_africa_pays_age2["Sexe"]=="Total"]

    df_selected_year_age2=data_africa_pays_Total_age2[data_africa_pays_Total_age2["Annee"]==selected_year]

    choropleth_age2= make_choropleth(df_selected_year_age2,
                                "Region", 
                                "Taux_emploi", 
                                selected_color_theme,
                                source_text="Source:Données issues de ILOSTAT",
                                chart_title="Taux d'emploi des jeunes de 25-64ans en "+str(selected_year)

                                )
    col=st.columns(2)
    with col[0]:
        st.plotly_chart(choropleth_age1,use_container_width=True)
    with col[1]:
        st.plotly_chart(choropleth_age2, use_container_width=True)
