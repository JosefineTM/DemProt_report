import streamlit as st
st.set_page_config(layout="wide", page_title="DementiaProteomics", page_icon="example_data/mona_logo.png")
st.logo("example_data/mona_logo.png")

st.markdown('''<h1 style='text-align: center; color: #023858;'>DementiaProteomics</h1>''', unsafe_allow_html=True)

sections_pages = {}
homepage = st.Page('home/homepage.py', title='Homepage')
sections_pages['Home'] = [homepage]

Imputation = st.Page('Data_Cleaning/Data_Cleaning_Imputation.py', title='Imputation')
Normalization = st.Page('Data_Cleaning/Data_Cleaning_Normalization.py', title='Normalization')
sections_pages['Data Cleaning'] = [Imputation, Normalization]

Cox_proportional_hazards_regression = st.Page('Discovery/Discovery_Cox_proportional_hazards_regression.py', title='Cox proportional hazards regression')
Cox_regression = st.Page('Discovery/Discovery_Cox_regression.py', title='Cox regression')
Edge_list = st.Page('Discovery/Discovery_Edge_list.py', title='Edge list')
sections_pages['Discovery'] = [Cox_proportional_hazards_regression, Cox_regression, Edge_list]

report_nav = st.navigation(sections_pages)
report_nav.run()