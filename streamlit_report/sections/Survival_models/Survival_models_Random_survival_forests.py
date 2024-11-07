import plotly.io as pio
import streamlit as st
import json

st.markdown('''<h3 style='text-align: center; color: #023558;'>Random survival forests</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Random survival forests</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Kaplan Meier plot of discovery cohort</h4>''', unsafe_allow_html=True)

st.image('example_data/DemProt/kaplan_meier_plot.png', caption='Kaplan Meier survival plot for the whole discovery cohort over time.', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Volcano plot of Cox regression results</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/COX_volcano.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)
