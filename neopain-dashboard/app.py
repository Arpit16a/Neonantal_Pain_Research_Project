from pathlib import Path
import streamlit as st

from components.data_utils import DATA_DIR, FIGURE_DIR, load_csv

st.set_page_config(
    page_title="NeoPain | Research Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp { background: #F8FAFC; }
[data-testid="stSidebar"] { background: #0F172A; }
[data-testid="stSidebar"] * { color: #F8FAFC; }
.hero {
  background: #0F172A; color: #F8FAFC; padding: 28px 30px;
  border-radius: 16px; margin-bottom: 18px;
}
.hero h1 { color: #F8FAFC; font-size: 2rem; margin: 0 0 8px 0; }
.hero p { color: #CBD5E1; margin: 0; font-size: 1rem; }
.info-card {
  background: white; border: 1px solid #E2E8F0; border-radius: 12px;
  padding: 18px; min-height: 132px;
}
.info-card h3 { color: #0F172A; margin: 0 0 8px 0; font-size: 1.05rem; }
.info-card p { color: #64748B; margin: 0; font-size: .92rem; }
.section-note { color: #64748B; font-size: .9rem; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🧠 NeoPain AI")
    st.caption("Neonatal pain research demonstration")
    st.divider()
    st.markdown("**Project**")
    st.write("Multimodal physiological-signal analysis")
    st.divider()
    st.caption("Use the pages in the navigation panel to explore performance, methodology and subject-level results.")

st.markdown("""
<div class="hero">
  <h1>Multimodal Neonatal Pain Classification</h1>
  <p>Machine-learning analysis of EEG, ECG and respiratory features</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Research overview")
st.write(
    "This project investigates whether features derived from multiple physiological "
    "signals can help distinguish dataset-defined neonatal stimulation conditions. "
    "The dashboard presents the dataset context, feature-engineering workflow and "
    "subject-independent model evaluation."
)

st.info(
    "Dataset context: the original UCL study collected EEG, behavioural and "
    "physiological responses around a clinically required painful procedure and "
    "control stimuli. This project applies a machine-learning analysis to selected "
    "recordings and derived features; it is not a clinical diagnostic system."
)

st.markdown("### UCL dataset at a glance")
cols = st.columns(4)
items = [
    ("112", "neonates in the original study"),
    ("20-channel", "EEG recording"),
    ("4 seconds", "epoch duration"),
    ("3", "stimulus types: heel lance, control, auditory"),
]
for col, (value, label) in zip(cols, items):
    with col:
        st.metric(label, value)

st.caption(
    "The 112-neonate cohort, 20-channel EEG and 4-second epochs describe the source "
    "dataset. The project's local processing audit separately reports 308 of 310 "
    "recordings processed; these figures have different scopes and denominators."
)

st.markdown("### Physiological modalities")
c1, c2, c3 = st.columns(3)
for col, title, body in [
    (c1, "EEG", "Cortical electrical activity. The current feature workflow includes frequency-band and other EEG-derived features."),
    (c2, "ECG", "Cardiac activity. Derived features include heart-rate and heart-rate-variability measures."),
    (c3, "Respiration", "Breathing-related signal information represented by statistical features in the current feature matrix."),
]:
    with col:
        st.markdown(f'<div class="info-card"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown("### Machine-learning workflow")
steps = [
    ("01", "Source recordings", "EEG epochs aligned to heel-lance, control and auditory stimuli; associated study information."),
    ("02", "Preprocessing", "Signal preparation, quality checks and alignment with recording metadata."),
    ("03", "Feature extraction", "EEG, ECG and respiration-derived numerical features."),
    ("04", "Feature matrix", "Current notebook workflow uses a selected 69-feature schema."),
    ("05", "Classifier", "XGBoost binary classification under the current notebook configuration."),
    ("06", "Evaluation", "Leave-One-Subject-Out (LOSO) evaluation to hold out subjects during testing."),
]
for num, title, desc in steps:
    a, b, c = st.columns([0.7, 2.2, 6])
    a.markdown(f"**{num}**")
    b.markdown(f"**{title}**")
    c.write(desc)
    st.divider()

st.markdown("### Current notebook model configuration")
m1, m2, m3 = st.columns(3)
m1.metric("Estimators", "300")
m2.metric("Maximum depth", "3")
m3.metric("Learning rate", "0.03")
st.caption(
    "These values describe the currently inspected notebook configuration. "
    "They are not asserted to be the exact configuration used to generate every "
    "camera-ready paper result."
)

st.markdown("### Research figures")
if FIGURE_DIR.exists():
    images = sorted([p for p in FIGURE_DIR.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg"}])
    if images:
        preferred = next((p for p in images if "ucl_single_file_signals" in p.name.lower()), images[0])
        st.image(str(preferred), caption=preferred.name, use_container_width=True)
    else:
        st.caption("No figures found in assets/figures yet.")
else:
    st.caption("Create assets/figures and copy the repository's existing research figures there.")

st.markdown("### Research scope and limitations")
st.warning(
    "For academic demonstration only. Model outputs are not clinical diagnoses, "
    "and the dashboard does not establish clinical validity or external validation."
)
st.caption(
    "The PICS PhysioNet data used elsewhere in the project is a separate ECG/HRV "
    "preprocessing-validation resource, not an external validation cohort for the UCL classifier."
)
