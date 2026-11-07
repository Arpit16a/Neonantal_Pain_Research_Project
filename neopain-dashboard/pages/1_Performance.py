import streamlit as st
from components.data_utils import DATA_DIR, FIGURE_DIR, load_csv, show_dataframe
from components.charts import show_roc_figures
from components.explanations import explain_auc, explain_loso

st.set_page_config(page_title="Model Performance | NeoPain", layout="wide")
st.title("Model Performance")
st.caption("Evaluation summaries from the saved research outputs")

st.markdown("### Current notebook configuration")
a, b, c = st.columns(3)
a.metric("Estimators", "300")
b.metric("Maximum depth", "3")
c.metric("Learning rate", "0.03")

st.caption(
    "Configuration provenance: current inspected notebook. The camera-ready "
    "paper configuration differs and has not been reconciled with these outputs."
)

summary = load_csv("reviewer1_summary_statistics.csv")
pooled = load_csv("pooled_auc_summary.csv")
subjects = load_csv("all_per_subject_metrics.csv")

st.markdown("### Evaluation summary")
show_dataframe(summary)

st.markdown("### Pooled out-of-fold summary")
show_dataframe(pooled)

with st.expander("How should these AUC values be interpreted?"):
    explain_auc()
    explain_loso()

st.markdown("### Saved ROC visualizations")
show_roc_figures(FIGURE_DIR)

st.markdown("### Subject-level evaluation table")
show_dataframe(subjects)

st.caption(
    "Only saved outputs are displayed here. The dashboard does not invent ROC "
    "coordinates, per-record predictions, confidence intervals or metrics."
)
