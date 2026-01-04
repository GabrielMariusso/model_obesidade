import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Análise Exploratória",
    page_icon="📊",
    layout="wide"
)

# CSS para padronizar altura dos cards
st.markdown(
    """
    <style>
    div[data-testid="stVerticalBlock"] > div:has(> div[data-testid="stContainer"]) {
        min-height: 520px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Análise Exploratória dos Dados")
st.markdown(
    "Esta seção apresenta a análise exploratória dos dados utilizados "
    "no treinamento do modelo de classificação de obesidade."
)

st.divider()

# =========================
# CONSTANTES VISUAIS
# =========================
FIG_SIZE = (5.5, 4)
palette_gender = {'Homem': '#4C72B0', 'Mulher': '#DD5A8F'}

ordem_obesity = [
    'Insufficient_Weight','Normal_Weight',
    'Overweight_Level_I','Overweight_Level_II',
    'Obesity_Type_I','Obesity_Type_II','Obesity_Type_III'
]

map_obesity_pt = {
    'Insufficient_Weight':'Abaixo do peso',
    'Normal_Weight':'Peso normal',
    'Overweight_Level_I':'Sobrepeso I',
    'Overweight_Level_II':'Sobrepeso II',
    'Obesity_Type_I':'Obesidade I',
    'Obesity_Type_II':'Obesidade II',
    'Obesity_Type_III':'Obesidade III'
}

# =========================
# FUNÇÃO CARD
# =========================
def card(titulo, fig):
    with st.container(border=True):
        st.markdown(f"#### {titulo}")
        fig.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

# =========================
# CARREGAMENTO DOS DADOS
# =========================
df = pd.read_csv("./Data/Obesity.csv")
df_tratado = df.copy()

for col in ['Age','FCVC','NCP','CH2O','FAF','TUE']:
    df_tratado[col] = df_tratado[col].round()

df_tratado['Gender'] = df_tratado['Gender'].map({'Male': 'Homem', 'Female': 'Mulher'})

# =====================================================
# SESSÃO 1 — PERFIL DEMOGRÁFICO E ALIMENTAÇÃO
# =====================================================
st.subheader("👥 Perfil demográfico e hábitos alimentares")

col1, col2 = st.columns(2)

with col1:
    obesity_levels = ['Obesity_Type_I','Obesity_Type_II','Obesity_Type_III']
    df_obese = df_tratado[df_tratado['Obesity'].isin(obesity_levels)].copy()

    bins = [10,14,19,24,29,34,39,44,49,54,59,100]
    labels = ['10–14','15–19','20–24','25–29','30–34','35–39',
              '40–44','45–49','50–54','55–59','60+']
    df_obese['Faixa etária'] = pd.cut(df_obese['Age'], bins=bins, labels=labels)

    piramide = df_obese.groupby(['Faixa etária','Gender']).size().reset_index(name='Total')
    homens = piramide[piramide['Gender']=='Homem'].copy()
    mulheres = piramide[piramide['Gender']=='Mulher'].copy()
    homens['Total'] *= -1

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.barh(homens['Faixa etária'], homens['Total'], color='#4C72B0', label='Homem')
    ax.barh(mulheres['Faixa etária'], mulheres['Total'], color='#DD5A8F', label='Mulher')
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: abs(int(x))))
    ax.legend()

    card("Distribuição de obesos por faixa etária e gênero", fig)

with col2:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.countplot(data=df_tratado, x='FAVC', hue='Gender', palette=palette_gender, ax=ax)
    ax.set_ylabel("Contagem")
    ax.set_xticklabels(['Não','Sim'])
    card("Consumo de alimentos calóricos", fig)

# =====================================================
# SESSÃO 2 — HÁBITOS DE CONSUMO
# =====================================================
st.subheader("🥗 Hábitos de consumo alimentar")

col3, col4 = st.columns(2)

with col3:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.countplot(data=df_tratado, x='FCVC', hue='Gender', palette=palette_gender, ax=ax)
    ax.set_ylabel("Contagem")
    ax.set_xticklabels(['Raramente','Às vezes','Sempre'])
    card("Consumo de vegetais", fig)

with col4:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.countplot(data=df_tratado, x='NCP', hue='Gender', palette=palette_gender, ax=ax)
    ax.set_ylabel("Contagem")
    card("Número de refeições por dia", fig)

# =====================================================
# SESSÃO 3 — ESTILO DE VIDA
# =====================================================
st.subheader("🍺 Estilo de vida e comportamento")

col5, col6 = st.columns(2)

with col5:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.countplot(
        data=df_tratado,
        x='CALC',
        order=['no','Sometimes','Frequently','Always'],
        hue='Gender',
        palette=palette_gender,
        ax=ax
    )
    ax.set_ylabel("Contagem")
    ax.set_xticklabels(['Não','Às vezes','Frequentemente','Sempre'])
    card("Consumo de álcool", fig)

with col6:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.countplot(data=df_tratado, x='TUE', hue='Gender', palette=palette_gender, ax=ax)
    ax.set_ylabel("Contagem")
    ax.set_xticklabels(['0–2h','3–5h','>5h'])
    card("Tempo de uso de dispositivos eletrônicos", fig)

# =====================================================
# SESSÃO 4 — HÁBITOS × OBESIDADE
# =====================================================
st.subheader("⚖️ Hábitos associados ao nível de obesidade")

col7, col8 = st.columns(2)

with col7:
    favc_tab = pd.crosstab(
        df_tratado['Obesity'],
        df_tratado['FAVC'],
        normalize='index'
    ).loc[ordem_obesity]

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    favc_tab.plot(kind='bar', stacked=True, color=["#807F7F", "#FD8F54"], ax=ax)

    ax.set_xticklabels([map_obesity_pt[o] for o in ordem_obesity], rotation=30, ha='right')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0%}'))
    ax.legend(['Não','Sim'])

    card("Consumo de alimentos calóricos por nível de obesidade", fig)

with col8:
    df_ch2o = (
        df_tratado
        .groupby('Obesity')['CH2O']
        .value_counts(normalize=True)
        .rename('percentual')
        .reset_index()
    )

    df_ch2o['Consumo de água'] = df_ch2o['CH2O'].map({
        1:'Menos de 1L', 2:'1 a 2L', 3:'Mais de 2L'
    })

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.barplot(
        data=df_ch2o,
        x='Obesity',
        y='percentual',
        hue='Consumo de água',
        order=ordem_obesity,
        palette='Blues',
        ax=ax
    )

    ax.set_xticklabels([map_obesity_pt[o] for o in ordem_obesity], rotation=30, ha='right')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0%}'))

    card("Consumo diário de água por nível de obesidade", fig)

# =====================================================
# SESSÃO 5 — ATIVIDADE FÍSICA
# =====================================================
st.subheader("🏃 Atividade física e obesidade")

col9, col10 = st.columns(2)

with col9:
    df_faf_gender = df_tratado.copy()

    # A coluna 'Gender' já foi traduzida para 'Homem'/'Mulher' no início do script
    df_faf_gender['Gênero'] = df_faf_gender['Gender']

    df_faf_gender['Frequência'] = df_faf_gender['FAF'].map({
        0: 'Nenhuma',
        1: '1–2x/sem',
        2: '3–4x/sem',
        3: '≥5x/sem'
    })

    df_faf_gender = (
        df_faf_gender
        .groupby(['Gênero', 'Frequência'], as_index=False)
        .size()
        .rename(columns={'size': 'total'})
    )

    df_faf_gender['percentual'] = (
        df_faf_gender
        .groupby('Gênero')['total']
        .transform(lambda x: x / x.sum())
    )

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    sns.barplot(
        data=df_faf_gender,
        x='Frequência',
        y='percentual',
        hue='Gênero',
        palette={'Homem': '#4C72B0', 'Mulher': '#DD5A8F'},
        ax=ax
    )

    ax.set_ylabel('Percentual')
    ax.set_xlabel('')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0%}'))
    ax.legend(title='Gênero')

    card("Frequência de atividade física por gênero", fig)

with col10:
    df_faf_obs = (
        df_tratado
        .groupby('Obesity')['FAF']
        .value_counts(normalize=True)
        .rename('percentual')
        .reset_index()
    )

    df_faf_obs['Frequência'] = df_faf_obs['FAF'].map({
        0:'Nenhuma',1:'1–2x/sem',2:'3–4x/sem',3:'≥5x/sem'
    })

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    sns.barplot(
        data=df_faf_obs,
        x='Obesity',
        y='percentual',
        hue='Frequência',
        order=ordem_obesity,
        palette='Greens',
        ax=ax
    )

    ax.set_xticklabels([map_obesity_pt[o] for o in ordem_obesity], rotation=30, ha='right')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0%}'))

    card("Frequência de atividade física por nível de obesidade", fig)
