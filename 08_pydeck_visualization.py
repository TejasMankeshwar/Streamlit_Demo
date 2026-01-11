import streamlit as st

import pydeck as pdk

import pandas as pd

import numpy as np

st.title("PyDeck Interactive Visualization")

"""

Demonstrates interactive map visualization with PyDeck.

"""

# Sample data

np.random.seed(42)

data = pd.DataFrame(
    {
        "lat": np.random.uniform(38.7, 38.8, 100),
        "lon": np.random.uniform(-122.5, -122.3, 100),
        "value": np.random.uniform(0, 100, 100),
    }
)

# PyDeck chart

layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position=["lon", "lat"],
    get_color=[200, 30, 0, 160],
    get_radius=100,
)

view_state = pdk.ViewState(
    latitude=38.7749,
    longitude=-122.4194,
    zoom=10,
    pitch=0,
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "Value: {value}"},
)

st.pydeck_chart(deck)
