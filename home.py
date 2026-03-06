import streamlit as st

st.set_page_config(page_title="HOME")
st.title("🏢 Gurgaon Real Estate Intelligence System")

st.markdown(
"""
This application provides **data-driven insights for Gurgaon real estate** using machine learning and analytics.
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🏢 Apartment Recommendation")
    st.write(
        "Find apartments similar to a selected property using a similarity-based recommendation system."
    )

with col2:
    st.subheader("💰 Price Prediction")
    st.write(
        "Predict apartment prices using a trained machine learning regression model."
    )

with col3:
    st.subheader("📊 Market Analytics")
    st.write(
        "Explore real estate trends through interactive visualizations and data analysis."
    )


    st.header("📈 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Apartments", "3500+")
col2.metric("Locations Covered", "60+")
col3.metric("Features Used", "25+")
col4.metric("ML Models", "3+")

st.header("🧠 Machine Learning Pipeline")

st.markdown("""
1️⃣ Data Collection  
2️⃣ Data Cleaning and Preprocessing  
3️⃣ Feature Engineering  
4️⃣ Model Training  

• Recommendation System → Cosine Similarity  
• Price Prediction → Regression Model  
• Analytics → Data Visualization
""")

st.header("⚙️ Technologies Used")

st.markdown("""
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Plotly  
- Machine Learning
""")

st.header("🚀 How to Use")

st.markdown("""
Use the **sidebar navigation** to explore the different modules:

• 📊 Analytics → Explore market trends  
• 💰 Price Predictor → Estimate property price  
• 🏢 Apartment Recommender → Discover similar properties
""")




