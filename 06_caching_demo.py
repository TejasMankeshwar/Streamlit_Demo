import streamlit as st

import time

st.title("Streamlit Caching Demo")

"""

Demonstrates @st.cache_data and @st.cache_resource for performance.

"""


@st.cache_data
def expensive_computation(n):
    time.sleep(2)  # Simulate slow computation

    return sum(range(n))


@st.cache_resource
def load_model():
    # Simulate loading a model

    time.sleep(1)

    return "Model Loaded"


st.write("Cached computation:")

n = st.slider("Number", 1, 1000000, 1000)

result = expensive_computation(n)

st.write(f"Sum: {result}")

st.write("Cached resource:")

model = load_model()

st.write(model)

st.write("Note: First run is slow, subsequent runs are fast due to caching.")
