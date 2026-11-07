from pathlib import Path
import streamlit as st

def show_roc_figures(figure_dir: Path):
    if not figure_dir.exists():
        st.info("The figures folder is not available.")
        return
    figures = sorted(
        p for p in figure_dir.iterdir()
        if p.suffix.lower() in {".png", ".jpg", ".jpeg"}
        and "roc" in p.name.lower()
    )
    if not figures:
        st.info(
            "No saved ROC image was found. Add the existing ROC figure from "
            "outputs/figures/paper_figures; this page will not generate a substitute."
        )
        return
    for fig in figures:
        st.image(str(fig), caption=fig.name, use_container_width=True)
