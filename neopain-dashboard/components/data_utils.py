from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
FIGURE_DIR = BASE_DIR / "assets" / "figures"

@st.cache_data(show_spinner=False)
def load_csv(filename):
    path = DATA_DIR / filename
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except Exception as exc:
        st.error(f"Could not read {filename}: {exc}")
        return None

def show_dataframe(df, title=None):
    if title:
        st.markdown(f"#### {title}")
    if df is None:
        st.info("This file is not available yet.")
    elif df.empty:
        st.warning("The file exists but contains no rows.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)
