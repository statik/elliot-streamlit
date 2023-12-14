import streamlit as st
import pandas as pd

st.write(
    """
# My first streamlit app
This is a line chart of a pandas DataFrame.
"""
)

df = pd.DataFrame([5, 1, 5, 10, 5, 3])

st.line_chart(df)
