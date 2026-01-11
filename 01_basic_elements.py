import streamlit as st

st.title("Basic Streamlit Elements Demo")

"""

This demo shows basic layout elements in Streamlit:

- Text and headers

- Sidebar

- Input widgets

- Metrics

- Columns and layout

"""

st.header("Headers and Text")

st.subheader("Subheader")

st.text("This is plain text")

st.markdown("**Bold** and *italic* text")

st.code("print('Hello, World!')")

with st.sidebar:
    st.write("This is the sidebar")

    option = st.selectbox("Choose an option", ["A", "B", "C"])

st.write("Selected:", option)

name = st.text_input("Enter your name")

st.write(f"Hello, {name}!")

col1, col2 = st.columns(2)

with col1:
    st.metric("Metric 1", 100, 5)

with col2:
    st.metric("Metric 2", 200, -10)

st.divider()

st.write("End of demo")
