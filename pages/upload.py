import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Streamlit App",
    page_icon="🧊",
    layout="wide"
)

# Titre de la page
st.title("Upload files")


# File Uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame in Streamlit
    st.dataframe(df)
