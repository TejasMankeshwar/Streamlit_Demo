import streamlit as st

import time

import pandas as pd

import numpy as np

st.title("Real-time Charts and Progress Bars")

"""

Demonstrates real-time updates with progress bars and dynamic charts.

"""

# Progress bar

progress_bar = st.progress(0)

status_text = st.empty()

for i in range(100):
    progress_bar.progress(i + 1)

    status_text.text(f"Progress: {i+1}%")

    time.sleep(0.01)

status_text.text("Done!")

# Real-time chart

chart_placeholder = st.empty()

data = pd.DataFrame(np.random.randn(100, 2), columns=["A", "B"])

for i in range(10):
    new_data = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])

    data = pd.concat([data, new_data])

    chart_placeholder.line_chart(data)

    time.sleep(0.5)

st.write("Real-time chart update complete")
