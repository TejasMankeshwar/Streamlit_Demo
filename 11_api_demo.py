import streamlit as st

import json

st.title("API Demo (Offline)")

"""

Demonstrates fetching and displaying local JSON data (simulating API call).

"""

# Simulate API call by reading local JSON

try:
    with open("sample_data.json", "r") as f:
        data = json.load(f)

    st.write("Fetched Data:")

    st.json(data)

    st.write("Message:", data["message"])

    st.write("Data List:", data["data"])

except FileNotFoundError:
    st.error("sample_data.json not found. Please ensure the file exists.")

# Note: For real API, use requests.get(url).json() but here offline.
