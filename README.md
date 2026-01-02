🏥 Sistema Preditivo de Obesidade

Este projeto tem como objetivo desenvolver uma aplicação interativa em Streamlit para predição do nível de obesidade de pacientes, utilizando Machine Learning, com foco em apoio à decisão clínica.

O sistema foi desenvolvido como parte do Tech Challenge – Fase 4 (Data Analytics) e utiliza o algoritmo XGBoost, selecionado após avaliação comparativa com outros modelos.

🎯 Objetivo do Projeto

Predizer o nível de obesidade com base em dados clínicos e comportamentais

Facilitar a interação por meio de uma interface amigável

Disponibilizar uma análise exploratória dos dados

Demonstrar a aplicação prática de Machine Learning em saúde

⚠️ Este sistema não substitui a avaliação de um profissional de saúde.
Ele deve ser utilizado apenas como apoio à tomada de decisão.

🧠 Modelo de Machine Learning

Algoritmo escolhido: XGBoost Classifier

Motivo da escolha: Melhor desempenho entre os modelos testados

Modelos avaliados:

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting

XGBoost (melhor desempenho)

O modelo final foi treinado, avaliado e salvo utilizando joblib.

🧩 Funcionalidades da Aplicação
🏠 Página Inicial

Apresentação do sistema

Orientações gerais

Navegação via menu lateral

🧮 Página de Predição

Formulário dividido em:

Dados do Paciente

Hábitos Alimentares e Refeições

Inputs em Português (pt-BR)

Conversão automática para o formato esperado pelo modelo

Exibição do nível de obesidade previsto

📊 Página de Análise de Dados

Gráficos exploratórios

Visualização de padrões do dataset

Apoio à interpretação dos dados utilizados no treinamento

🚀 Tecnologias Utilizadas

Python 3

Streamlit

Pandas

Scikit-learn

XGBoost

Matplotlib / Seaborn

Joblib

⚙️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone <url-do-repositorio>
cd modelo_obesidade

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv


Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

3️⃣ Instalar as dependências
pip install -r requirements.txt

4️⃣ Executar a aplicação
streamlit run app.py

📌 Observações Importantes

Os dados de entrada são tratados para respeitar o formato usado no treinamento

O sistema utiliza One-Hot Encoding para o meio de transporte

Os valores dos sliders seguem os limites do dataset original

A navegação entre páginas é feita pelo menu lateral do Streamlit