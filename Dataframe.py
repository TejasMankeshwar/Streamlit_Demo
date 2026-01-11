import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError


# Cache the data loading function
@st.cache_data
def get_un_data() -> pd.DataFrame:
    return pd.read_csv("agri.csv", index_col="Region")


st.title("Agricultural Production Dashboard")
st.write("This interactive demo visualizes agricultural production by country.")

try:
    # Load data
    df = get_un_data()

    # Country selection
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )

    if not countries:
        st.error("Please select at least one country.")
    else:
        # Extract data
        data = df.loc[countries]
        data /= 1_000_000.0

        st.subheader("Gross Agricultural Production ($B)")
        st.dataframe(data.sort_index())

        # Prepare for Altair
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )

        # Altair area chart
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )

        st.altair_chart(chart, use_container_width=True)

except URLError as e:
    st.error(f"This demo requires internet access. Connection error: {e.reason}")
