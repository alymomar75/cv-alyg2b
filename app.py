import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CV Aly Momar Diallo", layout="wide")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .stApp {background: #f9f9f9; color: #000;}
    h1, h2, h3 {color: #003366 !important;}
    .content-box {
        background: rgba(0,51,102,0.05);
        padding: 15px; border-radius: 10px; margin-bottom: 15px;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg,#001f3f 0%,#003366 100%);
        color: white;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("cv.png", width=220)
    st.write("👤 **Aly Momar DIALLO**")
    st.write("🏠 Dakar, Sénégal")
    st.write("📧 [alymomardiallo75@gmail.com](mailto:alymomardiallo75@gmail.com)")
    st.info("Contactez-moi par mail pour la disponibilité")

# --- EN-TÊTE ---
st.title("Étudiant en Géomatique")
st.markdown("""
<div class="content-box">
  Étudiant en 2ème année de géomatique au CEDT-G15,
  je développe des compétences solides dans l’analyse spatiale,
  la cartographie numérique et l’utilisation des outils SIG et photogrammétriques.
  Rigoureux et passionné par les sciences géographiques, 
  je m’investis pleinement dans mes projets académiques 
  afin de renforcer ma maîtrise des technologies géospatiales 
  et de contribuer à des solutions innovantes dans le domaine de la géomatique. 
</div>
""", unsafe_allow_html=True)

# --- EXPÉRIENCES ---
st.header("🏗️ Expériences professionnelles")
st.markdown("""
<div class="content-box">
  <p><strong>Stage</strong> (Juillet – Octobre 2025)<br>
  Direction Générale des Impôts et Domaines de Guédiawaye<br>
  Poste : Stage en géomatique</p>
</div>
""", unsafe_allow_html=True)

# --- FORMATIONS ---
st.header("📚 Parcours Académique")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="content-box">
      <p><strong>2026 – Présent</strong> (En cours)<br>
      BTS Géomatique – CEDT G15</p>
   <p><strong>2026 – Présent</strong> (En cours)<br>
      Licence en art graphique et numérique – UVS </p>
      <p><strong>2024</strong> (Juillet 2024)<br>
      Baccalauréat</p>

      <p><strong>2021</strong> (Août 2021)<br>
      BFEM</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="content-box">
        <strong>CEDT Le G15</strong><br>
        🎓 BTS en Géomatique (actuellement en cours)
    </div>
    """, unsafe_allow_html=True)

# --- COMPÉTENCES ---
st.header("🛠️ Compétences")
col_c1, col_c2 = st.columns(2)

with col_c1:
    st.markdown("""
    <div class="content-box">
        <strong>Techniques</strong><br>
        - SIG (QGIS, ArcMap)<br>
        - Topographie<br>
        - Programmation (HTML, Python)<br>
        - Collecte de données avec GPS, drone<br>
        - Modélisation (AutoCAD, SketchUp)
    </div>
    """, unsafe_allow_html=True)

with col_c2:
    st.markdown("""
    <div class="content-box">
        <strong>Langues</strong><br>
        - Français ★★★★★<br>
        - Anglais ★★★☆☆
    </div>
    """, unsafe_allow_html=True)
