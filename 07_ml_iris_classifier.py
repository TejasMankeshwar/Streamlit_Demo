import streamlit as st

from sklearn.datasets import load_iris

from sklearn.ensemble import RandomForestClassifier

import pandas as pd

st.title("Iris Flower Classifier")

"""

Simple ML demo: Train a Random Forest on Iris dataset and make predictions.

"""

# Load data

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["target"] = iris.target

st.write("Iris Dataset:")

st.dataframe(df.head())

# Train model

model = RandomForestClassifier()

model.fit(iris.data, iris.target)

# Prediction interface

st.header("Make a Prediction")

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)

sepal_width = st.slider("Sepal Width", 2.0, 5.0, 3.0)

petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)

petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    species = iris.target_names[prediction[0]]

    st.write(f"Predicted Species: {species}")
