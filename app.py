import streamlit as st
import numpy as np

st.title("Student Performance Analyzer")

marks_input = st.text_input("Enter marks separated by comma")

if marks_input:
    marks = np.array([int(i) for i in marks_input.split(",")])

    st.write("Marks:", marks)
    st.write("Average:", np.mean(marks))
    st.write("Max:", np.max(marks))
    st.write("Min:", np.min(marks))