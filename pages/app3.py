import streamlit as st

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    
    # Afficher les statistiques des données
    st.write("Statistics for the CSV file:")
    st.write(bytes_data.describe())
    
    # Créer un widget de sélection des colonnes
    col = st.multiselect("colonne ", bytes_data.col)

    if col:
        # Afficher les statistiques des colonnes sélectionnées
        st.write("statistique de la colonne:")
        st.write(bytes_data[col].describe())

st.sidebar.title("Menu")