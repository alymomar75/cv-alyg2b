import streamlit as st
# Configuration de la page
st.set_page_config(page_title="CVAlyMomarDiallo", layout="wide")

# --- STYLE CSS PERSONNALISÉ (Fond Bleu Nuit Dégradé) ---
st.markdown("""
    <style>
    /* Dégradé de bleu de nuit vers bleu ciel */
    .stApp {
        background: linear-gradient(180deg, #001f3f 0%, #0074D9 50%, #7FDBFF 100%);
        color: white;
    }
    
    /* Adaptation des titres pour le fond sombre */
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* Boîtes de contenu semi-transparentes pour la lisibilité */
    .content-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
    }

    /* Style de la barre latérale */
    [data-testid="stSidebar"] {
        background-color: rgba(#e2f3f7);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Personnalisation des listes */
    .stMarkdown p, .stMarkdown li {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Infos de contact) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>📍 Contact</h2>", unsafe_allow_html=True)
    st.image("cv.png", width=100)
    st.write("👤 **Aly Momar DIALLO**")
    st.write("🏠 Dakar, Sénégal")
    st.write("📧 [alymomardiallo75@gmail.com](mailto:alymomardiallo75@gmail.com)")
    st.write("📞 sur demande")
    st.markdown("---")
    st.info("Contacter moi via mail pour la disponibilité ")

# --- EN-TÊTE ---
st.title("Etudiant en geomatique")
st.markdown("""
<div class="content-box">
   Etudiant en 2ème année de geomatique au CEDT-G15, je recherche un stage durant les vacances à partir de juillet 2026 afin de mettre en pratique et d’approfondir mes connaissances dans des projets liés à la géomatique. je suis motivé et prêt à intégrer une équipe professionnelle.
</div>
""", unsafe_allow_html=True)

# --- FORMATIONS ---
st.header("📚 Parcours Académique")
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("""
    <div class="content-box">
        <strong>Diplome</strong><br>
        🎓 BFEM
st.radio Institution Saint François D’assise de Tivaouane Peulh
Baccalauréat
juillet 2024
st.radio Anne Marie Javouhey
Aout 2021
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

with c1:
    with st.container():
        st.subheader("🌐 Géomatique & SIG")
        st.markdown("""
       st.subheader("Geomatique")
    st.write("* Acquisition et traitement des données")
    st.write("* Topographie")
    st.write("* Programmation avec HTML,Python")
    st.write("* Collecte de données avec drone")
    st.write("* Modélisation sur AutoCAD et SketcUp")
    st.write("* Français :* ★★★★★")
    st.write("* Anglais :* ★★★☆☆")
        """)

# --- EXPÉRIENCES ---
st.header("🏗️Experiences")
st.markdown("""* 🛠️STAGE 
    * Poste : Stage de juillet à octobre 2025
    * Entreprise: DIRECTION GENERAL DES IMPOTS ET DOMAINE DE GUEDIWAYE
    * à GUEDIWAYE""")

