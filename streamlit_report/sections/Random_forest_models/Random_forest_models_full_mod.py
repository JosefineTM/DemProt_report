import streamlit as st
import plotly.io as pio
import json

st.markdown('''<h3 style='text-align: center; color: #023558;'>full_mod</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Model with all confounders and all candidate proteins</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Heatmap of feature importance in the models over time.</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/full_mod/heatmap_importances_split.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Heatmap of feature importance rank in the models over time.</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/full_mod/heatmap_rank_split.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)