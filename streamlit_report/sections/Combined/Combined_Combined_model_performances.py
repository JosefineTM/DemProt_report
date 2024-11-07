import streamlit as st
import plotly.io as pio
import json

st.markdown('''<h3 style='text-align: center; color: #023558;'>Combined model performances</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Combined plot of AUCs</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Combined AUCs</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/dynamic_AUC_COMBINED.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)
