import pandas as pd
import joblib
import streamlit as st

st.set_page_config(
    page_title="Formulário Preditivo de Obesidade",
    page_icon="",
    layout="centered"
)

# =========================
# CARREGAR MODELO
# =========================
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# =========================
# TÍTULO
# =========================
st.title("Formulário Preditivo de Obesidade")

# =========================
# MAPAS PT-BR → EN (MODELO)
# =========================
gender_map = {
    "Masculino": "Male",
    "Feminino": "Female"
}

yn_map = {
    "Sim": "yes",
    "Não": "no"
}

caec_map = {
    "Não": "no",
    "Às vezes": "Sometimes",
    "Frequentemente": "Frequently",
    "Sempre": "Always"
}

calc_map = {
    "Não consome": "no",
    "Às vezes": "Sometimes",
    "Frequentemente": "Frequently",
    "Sempre": "Always"
}

transport_map = {
    "Transporte público": "Public_Transportation",
    "Automóvel": "Automobile",
    "Caminhada": "Walking",
    "Motocicleta": "Motorbike",
    "Bicicleta": "Bike"
}
# =========================
# FORMULÁRIO
# =========================
with st.form("form_obesidade"):

    # =========================
    # 1. DADOS DO PACIENTE
    # =========================
    st.markdown("### 🧍‍♂️ Dados do paciente")
    col1, col2 = st.columns(2)

    with col1:
        Gender = gender_map[st.selectbox("Gênero", gender_map)]
        Age = st.number_input("Idade", min_value=1, max_value=100, value=25)
        Height = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.70)
        Weight = st.number_input("Peso (kg)", min_value=30.0, max_value=300.0, value=70.0)
        family_history = yn_map[st.selectbox("Histórico familiar de obesidade?", yn_map)]

    with col2:
        FAF = st.slider("Frequência de atividade física", 0.0, 3.0, 1.0)
        TUE = st.slider("Tempo de uso de tecnologia", 0.0, 3.0, 1.0)
        SMOKE = yn_map[st.selectbox("Fuma?", yn_map)]
        SCC = yn_map[st.selectbox("Monitora calorias?", yn_map)]
        MTRANS = transport_map[
            st.selectbox("Meio de transporte", transport_map)
        ]

    st.divider()

    # =========================
    # 2. HÁBITOS ALIMENTARES
    # =========================
    st.markdown("### 🍽️ Hábitos alimentares e refeições")
    col3, col4 = st.columns(2)

    with col3:
        FAVC = yn_map[st.selectbox("Consome alimentos altamente calóricos?", yn_map)]
        FCVC = st.slider("Consumo de vegetais", 1.0, 3.0, 2.0)
        NCP = st.slider("Número de refeições por dia", 1.0, 4.0, 3.0)

    with col4:
        CAEC = caec_map[
            st.selectbox("Come entre as refeições?", caec_map)
        ]
        CH2O = st.slider("Consumo diário de água", 1.0, 3.0, 2.0)
        CALC = calc_map[
            st.selectbox("Consumo de álcool", calc_map)
        ]

    submit = st.form_submit_button("🔍 Prever nível de obesidade")

# =========================
# PREDIÇÃO
# =========================
if submit:
    input_data = {
        # BINÁRIOS
        "Gender": 1 if Gender == "Male" else 0,
        "family_history": 1 if family_history == "yes" else 0,
        "FAVC": 1 if FAVC == "yes" else 0,
        "SMOKE": 1 if SMOKE == "yes" else 0,
        "SCC": 1 if SCC == "yes" else 0,

        # ORDINAIS
        "CAEC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}[CAEC],
        "CALC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}[CALC],

        # NUMÉRICOS
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "FCVC": FCVC,
        "NCP": NCP,
        "CH2O": CH2O,
        "FAF": FAF,
        "TUE": TUE,

        # DUMMIES DE TRANSPORTE
        "transporte_Automobile": 0,
        "transporte_Bike": 0,
        "transporte_Motorbike": 0,
        "transporte_Public_Transportation": 0,
        "transporte_Walking": 0
    }

    # Ativa o transporte escolhido
    input_data[f"transporte_{MTRANS}"] = 1

    # DataFrame final
    input_df = pd.DataFrame([input_data])

    # Predição
    prediction = model.predict(input_df)[0]

    st.success(f"✅ **Nível de obesidade previsto:** {prediction}")

    st.info(
        "⚠️ Este resultado é um apoio à decisão clínica e não substitui "
        "a avaliação de um profissional de saúde."
    )