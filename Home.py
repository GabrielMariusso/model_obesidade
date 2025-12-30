import streamlit as st

st.set_page_config(
    page_title="Sistema Preditivo de Obesidade",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Sistema Preditivo de Obesidade")

st.markdown("""
### 👋 Bem-vindo!

Este sistema utiliza **Machine Learning (XGBoost)** para:
- Predizer o **nível de obesidade**
- Analisar padrões comportamentais e clínicos
- Apoiar a tomada de decisão em saúde

📌 Use o **menu lateral** para navegar entre as funcionalidades.
""")

st.info("⚠️ Este sistema é apenas um apoio à decisão e não substitui avaliação médica.")
