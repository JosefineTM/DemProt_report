import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="DementiaProteomics",
    page_icon="example_data/mona_logo.png",
)
st.logo("example_data/mona_logo.png")

st.markdown(
    """<h1 style='text-align: center; color: #023858;'>DementiaProteomics</h1>""",
    unsafe_allow_html=True,
)

sections_pages = {}
homepage = st.Page("Home/homepage.py", title="Homepage")
sections_pages["Home"] = [homepage]

Imputation = st.Page("Data_Cleaning/Data_Cleaning_Imputation.py", title="Imputation")
Normalization = st.Page(
    "Data_Cleaning/Data_Cleaning_Normalization.py", title="Normalization"
)
sections_pages["Data Cleaning"] = [Imputation, Normalization]

Cox_proportional_hazards_regression = st.Page(
    "Discovery/Discovery_Cox_proportional_hazards_regression.py",
    title="Cox proportional hazards regression",
)
sections_pages["Discovery"] = [Cox_proportional_hazards_regression]

Random_survival_forests = st.Page(
    "Survival_models/Survival_models_Random_survival_forests.py",
    title="Random survival forests",
)
sections_pages["Survival models"] = [Random_survival_forests]

Introduction = st.Page(
    "Random_forest_models/Random_forest_models_Introduction.py", title="Introduction"
)
Full_model = st.Page(
    "Random_forest_models/Random_forest_models_Full_model.py", title="Full model"
)
Minimal_model = st.Page(
    "Random_forest_models/Random_forest_models_Minimal_model.py", title="Minimal model"
)
Clinical_model = st.Page(
    "Random_forest_models/Random_forest_models_Clinical_model.py",
    title="Clinical model",
)
sections_pages["Random forest models"] = [
    Introduction,
    Full_model,
    Minimal_model,
    Clinical_model,
]

Combined_model_performances = st.Page(
    "Combined/Combined_Combined_model_performances.py",
    title="Combined model performances",
)
Conclusion = st.Page("Combined/Combined_Conclusion.py", title="Conclusion")
sections_pages["Combined"] = [Combined_model_performances, Conclusion]

report_nav = st.navigation(sections_pages)
report_nav.run()
