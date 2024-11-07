import streamlit as st
import plotly.io as pio
import json

st.markdown('''<h3 style='text-align: center; color: #023558;'>Clinical model</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'>Model with only confounders which are easy to test in the clinic.</p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Heatmap of feature importance in the models over time.</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/clini_moc/heatmap_importances_split.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Heatmap of feature importance rank in the models over time.</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/clini_moc/heatmap_importances_combined.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>ROC curves of models over time.</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/clini_moc/ROC_curve_combined_best.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>AUC over time</h4>''', unsafe_allow_html=True)

with open('example_data/DemProt/clini_moc/dynamic_AUC.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)
