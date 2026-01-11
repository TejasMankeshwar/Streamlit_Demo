import streamlit as st

st.title("Page 1: Widgets")

"""

Demonstrates basic widgets in a multipage app.

"""

name = st.text_input("Enter your name")

st.write(f"Hello, {name}!")

slider = st.slider("Select value", 0, 100)

st.write(f"Value: {slider}")