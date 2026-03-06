from pathlib import Path
import pickle
import joblib
import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Gurgaon Price Predictor", layout="wide")

# Project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load dataframe
with open(BASE_DIR / "datasets" / "df.pkl", "rb") as file:
    df = pickle.load(file)

# Load pipeline
pipeline = joblib.load(BASE_DIR / "datasets" / "pipeline.joblib")

# Title
st.title("🏠 Gurgaon Real Estate Price Predictor")

st.markdown("""
This app predicts **property prices in Gurgaon** using a Machine Learning model.  
Enter property details in the **sidebar** to estimate the property price.
""")

# Sidebar inputs
st.sidebar.header("Enter Property Details")

property_type = st.sidebar.selectbox(
    "Property Type",
    ["flat", "house"]
)

sector = st.sidebar.selectbox(
    "Sector",
    sorted(df["sector"].unique().tolist())
)

bedrooms = float(st.sidebar.selectbox(
    "Number of Bedrooms",
    sorted(df["bedRoom"].unique().tolist())
))

bathroom = float(st.sidebar.selectbox(
    "Number of Bathrooms",
    sorted(df["bathroom"].unique().tolist())
))

balcony = st.sidebar.selectbox(
    "Balconies",
    sorted(df["balcony"].unique().tolist())
)

property_age = st.sidebar.selectbox(
    "Property Age",
    sorted(df["agePossession"].unique().tolist())
)

built_up_area = float(st.sidebar.number_input(
    "Built Up Area (sqft)",
    min_value=100.0
))

servant_room = float(st.sidebar.selectbox(
    "Servant Room",
    [0.0, 1.0]
))

store_room = float(st.sidebar.selectbox(
    "Store Room",
    [0.0, 1.0]
))

furnishing_type = st.sidebar.selectbox(
    "Furnishing Type",
    sorted(df["furnishing_type"].unique().tolist())
)

luxury_category = st.sidebar.selectbox(
    "Luxury Category",
    sorted(df["luxury_category"].unique().tolist())
)

floor_category = st.sidebar.selectbox(
    "Floor Category",
    sorted(df["floor_category"].unique().tolist())
)

# Prediction button
if st.sidebar.button("Predict Price"):

    data = [[
        property_type,
        sector,
        bedrooms,
        bathroom,
        balcony,
        property_age,
        built_up_area,
        servant_room,
        store_room,
        furnishing_type,
        luxury_category,
        floor_category
    ]]

    columns = [
        "property_type",
        "sector",
        "bedRoom",
        "bathroom",
        "balcony",
        "agePossession",
        "built_up_area",
        "servant room",
        "store room",
        "furnishing_type",
        "luxury_category",
        "floor_category"
    ]

    one_df = pd.DataFrame(data, columns=columns)

    # Prediction
    base_price = np.expm1(pipeline.predict(one_df))[0]

    low = base_price - 0.22
    high = base_price + 0.22

    st.subheader("💰 Estimated Property Price")

    st.metric(
        label="Predicted Price",
        value=f"{round(base_price,2)} Cr"
    )

    st.write(
        f"📊 Expected Price Range: **{round(low,2)} Cr – {round(high,2)} Cr**"
    )