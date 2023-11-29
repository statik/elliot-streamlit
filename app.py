import streamlit as st
import pandas as pd

st.write(
    """
# My first app
Hello *world!*
"""
)

df = pd.DataFrame([5, 1, 5, 10, 5, 3])

st.line_chart(df)
