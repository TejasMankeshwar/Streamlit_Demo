import streamlit as st

st.title("Interactive Widgets Demo")

"""

Demonstrates various interactive widgets:

- Sliders

- Buttons

- Multiselect

- File upload

- Radio buttons

- Checkboxes

"""

slider_val = st.slider("Select a value", 0, 100, 50)

st.write(f"Slider value: {slider_val}")

if st.button("Click me"):
    st.write("Button clicked!")

options = st.multiselect("Choose multiple", ["Apple", "Banana", "Cherry"])

st.write("Selected:", options)

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

radio_choice = st.radio("Choose one", ["Option 1", "Option 2", "Option 3"])

st.write(f"Radio choice: {radio_choice}")

checkbox = st.checkbox("Check me")

if checkbox:
    st.write("Checkbox is checked")
