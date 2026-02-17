import streamlit as st

# Configuration
st.set_page_config(page_title="CV de Aly", layout="wide")

# --- Titre principal ---
st.title("Curriculum Vitae - Aly Momar Diallo")

# --- Division en colonnes (70% / 30%) ---
col1, col2 = st.columns([7, 3])

# --- Partie gauche (70%) ---
with col1:
    st.header("Profil")
    st.write("Étudiant en 2eme années de BTS Géomatique")

    st.header("Formation")
    st.write("""
    - BTS Géomatique à Dakar  
    - Spécialisation en SIG et topographie  
    - Cours complémentaires en photogrammétrie et télédétection
    """)

    st.header("Expériences")
    st.write("""
    - Stage en cartographie urbaine  
    - Projet de suivi aéronautique et automatisation de workflows  
    - Développement de mini-guides Python pour filières SIG
    """)

# --- Partie droite (30%) ---
with col2:
    st.subheader("Contact")
    st.write("""
    📧 Email : alymomardiallo75@gmail.com  
    📱 Téléphone : (sur demande)  
    🌍 Dakar, Sénégal
    """)

    st.subheader("Compétences")
    st.write("""
    - SIG (QGIS, ArcMap)  
    - Webmapping (Leaflet, HTML/CSS)  
    - Programmation (Python, Streamleat)  
    - Topographie et pilotage drone
    """)

    st.subheader("Langues")
    st.write("""
    - Français (courant)  
    - Anglais (avancé)
    """)

    st.subheader("Centres d'intérêt")
    st.write("""
    - Aviation  
    - Geopolitique  
    """)
