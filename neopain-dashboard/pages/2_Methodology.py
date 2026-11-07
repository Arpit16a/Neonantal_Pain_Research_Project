import streamlit as st
from components.data_utils import FIGURE_DIR

st.set_page_config(page_title="Methodology | NeoPain", layout="wide")
st.title("Dataset and Methodology")
st.caption("Source dataset context and the current project workflow")

st.markdown("## 1. UCL source dataset")
st.write(
    "The dataset titled “EEG, behavioural, and physiological responses to a painful "
    "procedure in human neonates with relevant medical history” was created by "
    "Jones, Laudano-Dray and colleagues and deposited with the UK Data Service "
    "(2023 record; DOI: 10.5255/UKDA-SN-853204)."
)
st.write(
    "The source study measured cortical responses from 112 human neonates using "
    "EEG during a clinically required blood test, alongside behavioural and "
    "physiological responses recorded as part of the Premature Infant Pain Profile (PIPP)."
)

c1, c2, c3 = st.columns(3)
c1.metric("Study cohort", "112 neonates")
c2.metric("EEG montage", "20 channels")
c3.metric("Epoch length", "4 seconds")

st.markdown("### Stimulus conditions")
conditions = [
    ("L01", "Heel lance", "Painful clinical procedure"),
    ("C01", "Control", "Control stimulus"),
    ("A01", "Auditory", "Auditory stimulus"),
]
for code, name, description in conditions:
    x, y, z = st.columns([1, 2, 5])
    x.markdown(f"**{code}**")
    y.markdown(f"**{name}**")
    z.write(description)

st.markdown("### EEG file organisation")
st.write(
    "According to the dataset file-organisation note, the “Stimulation information” "
    "workbook contains a sheet for each of the three stimulus types. The second "
    "column gives the EEG file name. The file name combines the infant record "
    "identifier with the stimulus identifier."
)
st.code("Example pattern: <record identifier>L01 / C01 / A01", language="text")
st.warning(
    "Documented exception: trial 260701 had a technical issue and the control "
    "stimulation was repeated. The database and corresponding EEG file refer to "
    "the second control stimulus, 260701C02, recorded two minutes after the first."
)
st.write(
    "The organisation note states that EEG files are stored in 112 infant folders "
    "under the EEG directory, with the three stimulus epochs represented as "
    "MATLAB .mat files in each infant folder."
)

st.markdown("## 2. Project processing and feature engineering")
st.write(
    "The current project pipeline uses EEG, ECG and respiration-derived information. "
    "The source dataset description specifically describes EEG, behavioural and "
    "physiological measurements; the exact availability and processing of each "
    "modality should be traced to the project's own processed files and notebooks."
)

st.markdown("### Current 69-feature schema (notebook audit)")
feature_rows = [
    ("EEG channel features", "54"),
    ("GFP and channel-count features", "3"),
    ("ECG features", "4"),
    ("Respiration features", "2"),
    ("PIPP-associated physiological features", "6"),
]
for label, count in feature_rows:
    left, right = st.columns([4, 1])
    left.write(label)
    right.write(f"**{count}**")

st.warning(
    "The six PIPP-associated features are present in the currently inspected "
    "feature matrix. Their provenance and potential overlap with PIPP components "
    "are still under investigation; do not interpret this as a resolved leakage audit."
)

st.markdown("## 3. Classifier and evaluation")
st.markdown("**Classifier:** XGBoost")
m1, m2, m3 = st.columns(3)
m1.metric("n_estimators", "300")
m2.metric("max_depth", "3")
m3.metric("learning_rate", "0.03")

st.markdown("### Leave-One-Subject-Out evaluation")
st.write(
    "A subject is held out for testing while the remaining eligible subjects "
    "are used for training. This is repeated across subjects. It evaluates "
    "subject-independent performance within this dataset, not external validation."
)

st.markdown("## 4. Dataset roles and limitations")
st.write(
    "**UCL dataset:** primary dataset for the current classifier workflow."
)
st.write(
    "**PICS PhysioNet:** separate ECG/R-peak/HRV preprocessing-validation resource; "
    "it is not an external validation cohort for the UCL classifier."
)
st.write(
    "PIPP is a composite pain assessment measure. Dataset-defined labels and "
    "model outputs should not be described as direct measurements of subjective "
    "pain or as clinical diagnoses."
)

st.caption(
    "Dataset description supplied from the UK Data Service record and the "
    "project's EEG file-organisation note. Project-specific feature and model "
    "details come from the inspected research notebooks."
)
