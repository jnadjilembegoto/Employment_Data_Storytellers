import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from Datas.data_link import data_dir

def dash_secteur_pro_ais():
     #######################
    # Load data
    #@st.cache_data
    def load_data():
         data_path=data_dir('base_streamlit_storytellers.xlsx')
         return pd.read_excel(data_path,sheet_name="Secteur_prof_ais")

    df_reshaped = load_data()
        #######################
    # Sidebar
    with st.sidebar:
        st.title("🌾 🏭 🛍️ Professions clés de l'économie")
        
        year_list = list(df_reshaped.Annee.unique())[::-1]
        selected_year = st.selectbox('Choisir une année', year_list)
        
        Pays=list(df_reshaped.Pays.unique())
        selected_pays=st.selectbox('Choisir le pays', Pays)

        
        df_selected_year = df_reshaped[df_reshaped.Annee == selected_year]
        df_selected_pays=df_selected_year[df_selected_year.Pays==selected_pays]
###########
    st.subheader(f"Contribution des trois secteurs clés dans l'économie ({selected_pays}) en {selected_year}")
    col = st.columns((1.5, 1.5, 1.5), gap='medium')
    
    colonnes_secteurs = [
        "Agriculture, valeur ajoutée (% du PIB)",
        "Service, valeur ajoutée (% du PIB)",
        "Industrie, valeur ajoutée (% du PIB)",
    ]
    
    for i in range(3):
        with col[i]:
            var=colonnes_secteurs[i]
            valeur = df_selected_pays[var].iloc[0]
            st.metric(label=var, value=f"{valeur:.2f}")
    
    st.markdown('---')
    st.subheader(f"Proportion des emplois générés par les top 3 des domaines d'activité ({selected_pays}) en {selected_year}")
################
    def make_donut(input_response, input_text, input_color):
        if input_color == 'blue':
            chart_color = ['#29b5e8', '#155F7A']
        if input_color == 'green':
            chart_color = ['#27AE60', '#12783D']
        if input_color == 'orange':
            chart_color = ['#F39C12', '#875A12']
        if input_color == 'red':
            chart_color = ['#E74C3C', '#781F16']

        source = pd.DataFrame({
            "Topic": ['', input_text],
            "% value": [100-input_response, input_response]
        })
        source_bg = pd.DataFrame({
            "Topic": ['', input_text],
            "% value": [100, 0]
        })

        plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
            theta="% value",
            color= alt.Color("Topic:N",
                            scale=alt.Scale(
                                #domain=['A', 'B'],
                                domain=[input_text, ''],
                                # range=['#29b5e8', '#155F7A']),  # 31333F
                                range=chart_color),
                            legend=None),
        ).properties(width=130, height=130)

        text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
        plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
            theta="% value",
            color= alt.Color("Topic:N",
                            scale=alt.Scale(
                                # domain=['A', 'B'],
                                domain=[input_text, ''],
                                range=chart_color),  # 31333F
                            legend=None),
        ).properties(width=130, height=130)
        return plot_bg + plot + text
    
    gen_emploi=["Emplois dans l'agriculture (% du total des emplois)","Emplois dans les services (% du total des emplois)","Emplois dans l'industrie (% du total des emplois)"]
    col = st.columns((1.5, 1.5, 1.5), gap='medium')
    for i in range(3):
        var=gen_emploi[i]
        val=round(df_selected_pays[var].iloc[0],1)
        with col[i]:
            if val<20:
                color="red"
            elif val<50:
                color="yellow"
            else:
                color='green'
            donut_chart = make_donut(val, var,color )
            st.write(f'{var}')
            st.altair_chart(donut_chart)


    st.markdown('---')    
    st.subheader(f"Proportion des emplois générés par les top 3 des domaines d'activité ({selected_pays}) en {selected_year}")
    ag_emploi=["Employées, agriculture, femmes (% d'emploi des femmes)","Employés, agriculture, hommes (% d'emploi des hommes)"]
    ind_emploi=["Employées, industrie, femmes (% d'emploi des femmes)","Employés, industrie, hommes (% d'emploi des hommes)"]
    serv_emploi=["Employées, services, femmes (% d'emploi des femmes)","Employés, services, hommes (% d'emploi des hommes)"]

        