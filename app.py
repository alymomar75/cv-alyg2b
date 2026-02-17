import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV de Aly Momar Diallo", page_icon="📍", layout="wide")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stHeader {
        color: #1e3d59;
    }
    </style>
    """, unsafe_allow_headers=True)

# --- SIDEBAR (Informations personnelles & Langues) ---
with st.sidebar:
    st.image(scr="cv.png") 
    st.title("Aly Momar Diallo")
    st.subheader("Étudiant en Géomatique")
    
    st.markdown("---")
    st.markdown("### 📍 Coordonnées")
    st.write("🏠 Cité Safco 3, Keur Massar, Dakar")
    st.write("📞 +221 7X XXX XX XX")
    st.write("📧 alymomardiallo75@gmail.com")
    
    st.markdown("---")
    st.markdown("### 🚗 Informations")
    st.write("**Disponibilité :** Dès maintenant")
    st.write("**Permis :** A1 / B")
    st.write("**Nationalité :** Sénégalaise")
    
    st.markdown("---")
    st.markdown("### 🗣️ Langues")
    st.write("**Français :** ★★★★★")
    st.write("**Anglais :** ★★★☆☆")

# --- CONTENU PRINCIPAL ---

# En-tête / Profil
st.header("📍 Profil Professionnel")
st.info("""
Étudiant en **2ème année de géomatique** au CEDT-G15, je recherche un stage durant les vacances 
**à partir de juillet 2026** afin de mettre en pratique et d'approfondir mes connaissances 
dans des projets liés à la géomatique. Je suis motivé et prêt à intégrer une équipe professionnelle.
""")

col1, col2 = st.columns([6, 4])

with col1:
    st.header("🎓 Formations")
    
    with st.expander("**BTS en GÉOMATIQUE** (En cours)", expanded=True):
        st.write("**CEDT-G15** | Octobre 2024 - Présent")
        st.caption("Centre d'Entreprenariat et de Développement Technique")
        st.write("Focus : SIG, Topographie, Photogrammétrie et Télédétection.")

    with st.expander("**Baccalauréat**"):
        st.write("**Institution Saint François D'assise de Tivaouane Peulh** | Juillet 2024")

    with st.expander("**BFEM**"):
        st.write("**Anne Marie Javouhey** | Août 2021")

    st.header("💼 Expériences Professionnelles")
    st.write("**STAGE - (DGID) Cadastre de Guediawaye**")
    st.write("*Juillet à Octobre 2025*")
    st.markdown("""
    - Appui aux opérations cadastrales.
    - Mise à jour de plans parcellaires.
    - Digitalisation et archivage de données foncières.
    """)

with col2:
    st.header("🛠️ Compétences Techniques")
    st.success("""
    - **SIG :** QGIS, ArcGIS, ArcMap
    - **CAO/DAO :** AutoCAD, Microstation, SketchUp 3D
    - **Base de Données :** MySQL
    - **Terrain :** Topographie, Collecte (Satellite, Drone, GPS)
    - **Bureautique :** Pack Office (Word, Excel, PowerPoint)
    - **Dév :** Python, Streamlit, HTML/CSS
    """)

    st.header("🎨 Centres d'intérêt")
    interests = ["🎬 Audiovisuel", "🌍 Géopolitique", "🚗 Automobile", "✈️ Aviation"]
    for item in interests:
        st.write(item)
