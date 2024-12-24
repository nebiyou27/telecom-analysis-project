import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Connect to PostgreSQL database using SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:neba@localhost/telecom_db')

# Fetch data from the database
df = pd.read_sql("SELECT * FROM user_scores", engine)

# Streamlit page configuration
st.set_page_config(page_title="User Scores Dashboard", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ("User Overview Analysis", "User Engagement Analysis", "Experience Analysis", "Satisfaction Analysis"))

# User Overview Analysis Page
if page == "User Overview Analysis":
    st.title("User Overview Analysis")
    st.write("This section provides an overview of the user data.")
    
    # Show the first few rows of the data
    st.write(df.head())
    
    # Plot the overall engagement score distribution
    engagement_fig = px.histogram(df, x="engagement_score", title="User Engagement Score Distribution")
    st.plotly_chart(engagement_fig)

# User Engagement Analysis Page
elif page == "User Engagement Analysis":
    st.title("User Engagement Analysis")
    st.write("This section focuses on the engagement scores of users.")
    
    # Plot the engagement score distribution
    engagement_fig = px.histogram(df, x="engagement_score", title="User Engagement Score Distribution")
    st.plotly_chart(engagement_fig)

# Experience Analysis Page
elif page == "Experience Analysis":
    st.title("User Experience Analysis")
    st.write("This section visualizes the experience scores of users.")
    
    # Plot the experience score distribution
    experience_fig = px.histogram(df, x="experience_score", title="User Experience Score Distribution")
    st.plotly_chart(experience_fig)

# Satisfaction Analysis Page
elif page == "Satisfaction Analysis":
    st.title("User Satisfaction Analysis")
    st.write("This section visualizes the satisfaction scores of users.")
    
    # Plot the satisfaction score distribution
    satisfaction_fig = px.histogram(df, x="satisfaction_score", title="User Satisfaction Score Distribution")
    st.plotly_chart(satisfaction_fig)