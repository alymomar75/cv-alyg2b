import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV Aly Momar Diallo", layout="wide")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #001f3f 0%, #0074D9 50%, #7FDBFF 100%);
        color: white;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .content-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
    }
    [data-testid="stSidebar"] {
        background-color: #e2f3f7;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stMarkdown p, .stMarkdown li {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("cv.png", width=100)
    st.write("👤 **Aly Momar DIALLO**")
    st.write("🏠 Dakar, Sénégal")
    st.write("📧 [alymomardiallo75@gmail.com](mailto:alymomardiallo75@gmail.com)")
    st.write("📞 sur demande")
    st.markdown("---")
    st.info("Contactez-moi par mail pour la disponibilité")

# --- EN-TÊTE ---
st.title("Étudiant en Géomatique")
st.markdown("""
<div class="content-box">
   Étudiant en 2ème année de géomatique au CEDT-G15, je recherche un stage durant les vacances à partir de juillet 2026 afin de mettre en pratique et d’approfondir mes connaissances dans des projets liés à la géomatique. Je suis motivé et prêt à intégrer une équipe professionnelle.
</div>
""", unsafe_allow_html=True)

# --- FORMATIONS ---
st.header("📚 Parcours Académique")
col_f1, col_f2 = st.columns(2)

with col_f1:
    st.markdown("""
    <div class="content-box">
        <strong>Diplômes 🎓</strong><br>
        - BFEM (Août 2021) Institution Saint François d’Assise de Tivaouane Peulh<br>
        - Baccalauréat (Juillet 2024) Anne Marie Javouhey
    </div>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
    <div class="content-box">
        <strong>CEDT Le G15</strong><br>
        🎓 BTS en Géomatique
    </div>
    """, unsafe_allow_html=True)

# --- COMPÉTENCES ---
st.header("🛠️ Compétences & Expertises")
st.markdown("""
<div class="content-box">
    <strong>🌐 Géomatique</strong><br>
    - Acquisition et traitement des données<br>
    - Topographie<br>
    - Programmation avec HTML, Python<br>
    - Collecte de données avec drone<br>
    - Modélisation sur AutoCAD et SketchUp<br>
    - Français ★★★★★<br>
    - Anglais ★★★☆☆
</div>
""", unsafe_allow_html=True)

# --- EXPÉRIENCES ---
st.header("🏗️ Expériences")
st.markdown("""
<div class="content-box">
    <strong>🛠️ Stage</strong><br>
    - Juillet à Octobre 2025<br>
    - Direction Générale des Impôts et Domaines de Guédiawaye<br>
    - Poste : Stagiaire en géomatique
</div>
""", unsafe_allow_html=True)
