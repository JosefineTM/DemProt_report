import plotly.io as pio
import json
import pandas as pd
import streamlit as st
import dataframe_image as dfi
from itables import show

st.markdown('''<h3 style='text-align: center; color: #023558;'>Cox proportional hazards regression</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Description for subsection</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Kaplan Meier plot of discovery cohort</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/kaplan_meier_plot.png', caption='Caption for kaplan meier', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Volcano plot of Cox regression results</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/COX_volcano.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Cox regression results</h4>''', unsafe_allow_html=True)
df = pd.read_excel('example_data/DemProt/COX_regression.xlsx')
st.dataframe(df, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Coefficient dependcy on alpha penalizer</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/COX_paths.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)
