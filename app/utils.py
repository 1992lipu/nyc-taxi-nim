import streamlit as st

def display_info():
    st.markdown("""
        This app integrates the NYC Taxi dataset with AI-powered functionalities:
        - **SQL Generator**: Allows users to generate SQL queries dynamically based on their input.
        - **Image Generator**: Uses Stable Diffusion or other AI models to generate images based on a description.
        - **Data Query**: Queries the NYC taxi dataset using SQL and displays the results.
    """)
