import streamlit as st

def explain_loso():
    st.markdown("""
    **Leave-One-Subject-Out (LOSO) evaluation**

    In each fold, recordings belonging to one subject are held out for testing,
    while the remaining eligible subjects are used for training. The process
    repeats across subjects. This tests generalisation to held-out subjects
    within the available dataset; it is not external validation on an independent
    dataset or hospital.
    """)

def explain_auc():
    st.markdown("""
    **Mean subject-level AUC and pooled out-of-fold AUC are different summaries.**

    Mean subject-level AUC is calculated by computing AUC separately for eligible
    held-out subjects and then averaging those values. Pooled OOF AUC combines
    held-out predictions across subjects and computes one AUC over the combined
    set. They answer different questions and should not be interchanged.
    """)
