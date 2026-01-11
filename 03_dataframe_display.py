import streamlit as st

import pandas as pd

import numpy as np

st.title("DataFrame Display and Styling")

"""

Shows how to display DataFrames with styling.

"""

# Create sample data

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 92, 78, 88],
}

df = pd.DataFrame(data)

st.dataframe(df)

st.dataframe(df.style.highlight_max(axis=0))

st.table(df)

# With styling


def color_negative_red(val):
    color = "red" if val < 80 else "green"

    return f"background-color: {color}"


styled_df = df.style.applymap(color_negative_red, subset=["Score"])

st.dataframe(styled_df)
