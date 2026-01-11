import streamlit as st

st.title("Advanced Streamlit Features")

"""

Demonstrates session state, forms, containers, tabs, and expanders.

"""

# Session State

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")

# Forms

with st.form("my_form"):
    name = st.text_input("Name")

    age = st.number_input("Age", min_value=0)

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Name: {name}, Age: {age}")

# Containers

with st.container():
    st.write("Inside a container")

    st.button("Button in container")

# Tabs

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Content of Tab 1")

with tab2:
    st.write("Content of Tab 2")

# Expander

with st.expander("Click to expand"):
    st.write("Expanded content")
