import streamlit as st
import numpy as np
import time

st.title("Live Updating Line Chart with Progress Bar")

# Set up sidebar widgets
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Initial random data
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows, use_container_width=True)

# Update loop
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

# Remove the progress bar after completion
progress_bar.empty()

# Re-run button
st.button("Rerun")
