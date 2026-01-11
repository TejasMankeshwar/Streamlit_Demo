import streamlit as st

import altair as alt

import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

st.title("Plotting with Altair and Matplotlib")

"""

Demonstrates charts using Altair and Matplotlib.

"""

# Sample data

data = pd.DataFrame({"x": np.arange(10), "y": np.random.randn(10)})

# Altair chart

chart = alt.Chart(data).mark_line().encode(x="x", y="y")

st.altair_chart(chart, use_container_width=True)

# Matplotlib chart

fig, ax = plt.subplots()

ax.plot(data["x"], data["y"])

ax.set_title("Matplotlib Plot")

st.pyplot(fig)
