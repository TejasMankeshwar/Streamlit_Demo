import streamlit as st

import pandas as pd

st.title("Page 2: Data Visualization")

"""

Shows a simple chart in multipage app.

"""

data = pd.DataFrame({'x': [1,2,3,4], 'y': [10,20,15,25]})

st.line_chart(data)