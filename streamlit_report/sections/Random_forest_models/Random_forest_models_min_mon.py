import streamlit as st
import json

st.markdown('''<h3 style='text-align: center; color: #023558;'>min_mon</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Model with only age and sex as confounders</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Kaplan Meier plot of discovery cohort</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/kaplan_meier_plot.png', caption='Kaplan Meier survival plot for the whole discovery cohort over time.', use_column_width=True)
