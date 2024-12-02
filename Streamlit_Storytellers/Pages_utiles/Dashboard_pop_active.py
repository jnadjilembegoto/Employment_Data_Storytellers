######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from Datas.data_link import data_dir
#######################
# Page configuration
def dash_pop_active():
     #######################
    # Load data
    #@st.cache_data
    def load_data():
         data_path=data_dir('base_streamlit_storytellers.xlsx')
         return pd.read_excel(data_path,sheet_name="Pop_active_Af_pays")

    df_reshaped = load_data()


    #######################
    # Sidebar
    with st.sidebar:
        st.title('🏂 Population active')
        
        #year_list = list(df_reshaped.Annee.unique())[::-1]
        #selected_year = st.selectbox('Choisir une année', year_list)
        selected_year = st.sidebar.slider("Sélectionnez une année :", int(df_reshaped.Annee.min()), int(df_reshaped.Annee.max()), 2020)

        sexe=list(df_reshaped.Sexe.unique())
        selected_sexe=st.selectbox('Choisir le genre', sexe)


        df_selected_year = df_reshaped[df_reshaped.Annee == selected_year]
        df_selected_year_sorted = df_selected_year.sort_values(by="Proportion_de_population_active(%)", ascending=False)
        df_selected_final=df_selected_year_sorted[df_selected_year_sorted.Sexe==selected_sexe]

        color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
        selected_color_theme = st.selectbox('Choisir une mise en forme de la carte', color_theme_list)

    # Choropleth map
    def make_choropleth(input_df, input_id, input_column, input_color_theme):
        choropleth = px.choropleth(input_df, locations=input_id, color=input_column, locationmode="country names",
                                color_continuous_scale=input_color_theme,
                                range_color=(0, max(df_selected_year["Proportion_de_population_active(%)"])),
                                scope="africa",
                                labels={'Proportion_de_population_active(%)':'Population active(%)'}
                                )
        choropleth.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            margin=dict(l=0, r=0, t=0, b=0),
            height=350
        )
        return choropleth


    # Heatmap
    def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
        heatmap = alt.Chart(input_df).mark_rect().encode(
                y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
                x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
                color=alt.Color(f'max({input_color}):Q',
                                legend=None,
                                scale=alt.Scale(scheme=input_color_theme)),
                stroke=alt.value('black'),
                strokeWidth=alt.value(0.25),
            ).properties(width=900
            ).configure_axis(
            labelFontSize=12,
            titleFontSize=12
            ) 
        # height=300
        return heatmap
    
    #######################
    # Dashboard Main Panel
    col = st.columns((1.5, 4.5, 2), gap='medium')

    with col[0]:
        st.markdown('#### proportion totale de la Population active en Afrique (%)')
        


    with col[1]:
        st.markdown(f'#### Proportion de la population active en {selected_year}')
        
        choropleth = make_choropleth(df_selected_year, 'Pays', 'Proportion_de_population_active(%)', selected_color_theme)
        st.plotly_chart(choropleth, use_container_width=True)
        

    with col[2]:
        st.markdown(f'#### Classement des pays par population active en {selected_year}')

        st.dataframe(df_selected_final,
                    column_order=("Pays", "Proportion_de_population_active(%)"),
                    hide_index=True,
                    width=None,
                    column_config={
                        "Pays": st.column_config.TextColumn(
                            "Pays",
                        ),
                        "Proportion_de_population_active(%)": st.column_config.ProgressColumn(
                            "Population active (%)",
                            format="%f",
                            min_value=0,
                            max_value=max(df_selected_year_sorted["Proportion_de_population_active(%)"]),
                        )}
                    )
        
        with st.expander('About', expanded=False):
            st.write('''
                - Source: [BIT](https://ilostat.ilo.org/fr/data.html).
                - :orange[**Population active**]: Une population active qui croît peut s’expliquer par l’entrée sur le marché du travail de nouvelles personnes en quête d’emplo
                ''')

    heatmap = make_heatmap(df_reshaped, 'Annee', 'Pays', 'Proportion_de_population_active(%)', selected_color_theme)
    
    st.markdown(f'#### Proportion des populations actives par pays entre {int(df_reshaped.Annee.min())} et {int(df_reshaped.Annee.max())}')
    st.altair_chart(heatmap, use_container_width=True)
    st.write("Source: ILOSTAT")


