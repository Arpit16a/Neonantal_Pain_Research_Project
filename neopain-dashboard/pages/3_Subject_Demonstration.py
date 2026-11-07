import streamlit as st
from components.data_utils import load_csv, show_dataframe

st.set_page_config(page_title="Subject-wise Results | NeoPain", layout="wide")
st.title("Subject-wise Evaluation")
st.caption("Held-out subject metrics available in the saved evaluation output")

df = load_csv("all_per_subject_metrics.csv")

if df is None:
    st.warning("The all_per_subject_metrics.csv file was not found in the data folder.")
elif df.empty:
    st.warning("The subject metrics file is empty.")
else:
    st.write(f"Rows available: **{len(df)}**")
    st.dataframe(df, use_container_width=True, hide_index=True)

    possible_subject_cols = [
        c for c in df.columns
        if c.lower() in {"subject", "subject_id", "record identifier", "record_id", "infant"}
    ]
    if possible_subject_cols:
        col = possible_subject_cols[0]
        choices = sorted(df[col].dropna().astype(str).unique().tolist())
        selected = st.selectbox("Inspect a held-out subject", choices)
        st.dataframe(df[df[col].astype(str) == selected], use_container_width=True, hide_index=True)

st.info(
    "This page currently displays saved subject-level evaluation metrics. "
    "It does not yet show individual recording predictions because a row-level "
    "out-of-fold prediction export has not been confirmed in the repository."
)
st.caption(
    "A true prediction demonstration will be added after the LOSO evaluation "
    "pipeline exports each held-out recording's identifier, true label, predicted "
    "class and model score."
)
