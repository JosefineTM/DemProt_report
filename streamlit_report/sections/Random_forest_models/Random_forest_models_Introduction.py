import plotly.io as pio
import streamlit as st
import json

st.markdown('''<h3 style='text-align: center; color: #023558;'>Introduction</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>description of RFs</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Recoding of cases to non-cases over time.</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/cases_recoding.png', caption='Illustration of the idea behind recoding of the cases and non-cases based on year cut-off. ', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>N cases and cases over time.</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/intro/cases_non_cases_time.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)
