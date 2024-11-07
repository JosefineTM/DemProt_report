import streamlit as st
import plotly.io as pio
from itables import show
import json
import pandas as pd
import dataframe_image as dfi

st.markdown('''<h3 style='text-align: center; color: #023558;'>Cox proportional hazards regression</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>To find the candidate protein biomarkers, a Cox proportional hazards regression was run univariately over all the proteins while adjusting for EGFR, Age at baseline, sex, ethnicity (white, black, hispanic, other), education (less than highschool, high school, college and above) and BMI (underweight, helathy, overweight, obese). Subsequently, the p-values were adjusted for multiple testeing via false discovery rate (FDR) adjustment with an alpha of 0.05. </p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Kaplan Meier plot of discovery cohort</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/kaplan_meier_plot.png', caption='Kaplan Meier survival plot for the whole discovery cohort over time.', use_column_width=True)

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
