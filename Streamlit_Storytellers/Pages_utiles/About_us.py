import streamlit as st

def about_us_page():
    st.title("À propos de nous")
    st.write("""
    La Data Stotytellers Team est constitué de Cinq élèves ingénieurs statisticiens économistes en formation à l'ISSEA.
             
    """)
    st.markdown('---')
    st.markdown(
        f"""
        ##### AZAPMO TAZO Dylan 
        - Email:  <student.dilane.tazo@issea-cemac.org>
        - GitHub: https://

        ##### MPOLAH SOH Natacha Flaire
        - Email: <eliassetiao@gmail.com>
        - Linkdin: https://

        ##### NADJILEM BEGOTO
        - Email: <jnadjilembegoto@gmail.com> ou <student.begoto.nadjilem@issea-cemac.org>
        - Linkdin: https://

        ##### TEYANBAYE BERTORNGAI Christian
        - Email: <teyanchrist@gmail.com>
        - Linkdin: https://

        ##### TIAO Eliasse
        - Email: <eliassetiao@gmail.com>
        - Linkdin: https://
        """,
        unsafe_allow_html=True,
    )
    
