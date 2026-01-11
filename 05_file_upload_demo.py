import streamlit as st

import pandas as pd

st.title("File Upload and CSV Handling")

"""

Demonstrates uploading CSV files, displaying data, and basic transformations.

"""

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data:")

    st.dataframe(df)

    # Basic transformations

    if st.button("Show Summary"):
        st.write(df.describe())

    if st.button("Filter by Column"):
        column = st.selectbox("Select column to filter", df.columns)

        value = st.text_input("Enter value to filter")

        if value:
            filtered = df[df[column].astype(str).str.contains(value, case=False)]

            st.dataframe(filtered)

else:
    st.write("Please upload a CSV file.")

# Sample data for demo

st.write("Sample Data:")

sample_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NY", "LA", "Chicago"],
}

sample_df = pd.DataFrame(sample_data)

st.dataframe(sample_df)
