import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(page_title="Apartment Recommender", layout="wide")

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
@st.cache_data
def load_data():
    with open('/Users/apple/Documents/abc/Capstone_project_part2/datasets/location_df.pkl', 'rb') as f:
        location_df = pickle.load(f)

    with open('/Users/apple/Documents/abc/Capstone_project_part2/datasets/cosine_sim1.pkl', 'rb') as f:
        cosine_sim1 = pickle.load(f)

    with open('/Users/apple/Documents/abc/Capstone_project_part2/datasets/cosine_sim2.pkl', 'rb') as f:
        cosine_sim2 = pickle.load(f)

    with open('/Users/apple/Documents/abc/Capstone_project_part2/datasets/cosine_sim3.pkl', 'rb') as f:
        cosine_sim3 = pickle.load(f)

    return location_df, cosine_sim1, cosine_sim2, cosine_sim3


location_df, cosine_sim1, cosine_sim2, cosine_sim3 = load_data()

# ---------------------------------------------------
# Recommendation Function
# ---------------------------------------------------
def recommend_properties_with_scores(property_name, top_n=5):

    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    try:
        idx = location_df.index.get_loc(property_name)
    except KeyError:
        st.error("Property not found in dataset.")
        return pd.DataFrame()

    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]

    top_properties = location_df.index[top_indices].tolist()

    recommendations_df = pd.DataFrame({
        "PropertyName": top_properties,
        "SimilarityScore": top_scores
    })

    return recommendations_df


# ---------------------------------------------------
# App Title
# ---------------------------------------------------
st.title("🏢 Gurgaon Apartment Recommendation System")

# ---------------------------------------------------
# Location Radius Search
# ---------------------------------------------------
st.header("📍 Search Apartments Near a Location")

col1, col2 = st.columns(2)

with col1:
    selected_location = st.selectbox(
        "Select Location",
        sorted(location_df.columns.to_list())
    )

with col2:
    radius = st.number_input(
        "Radius (in km)",
        min_value=1,
        max_value=20,
        value=5
    )

if st.button("Search Nearby Apartments"):

    result_ser = location_df[
        location_df[selected_location] < radius * 1000
    ][selected_location].sort_values()

    if len(result_ser) == 0:
        st.warning("No apartments found in this radius.")
    else:
        st.subheader("Apartments within radius")

        for key, value in result_ser.items():
            st.write(f"• {key} — {round(value/1000,2)} km")


# ---------------------------------------------------
# Apartment Recommendation
# ---------------------------------------------------
st.header("🤖 Recommend Similar Apartments")

selected_apartment = st.selectbox(
    "Select an Apartment",
    sorted(location_df.index.to_list())
)

top_n = st.slider(
    "Number of recommendations",
    1,
    10,
    5
)

if st.button("Recommend Apartments"):

    recommendation_df = recommend_properties_with_scores(
        selected_apartment,
        top_n
    )

    if not recommendation_df.empty:
        st.subheader("Recommended Apartments")
        st.dataframe(recommendation_df, use_container_width=True)