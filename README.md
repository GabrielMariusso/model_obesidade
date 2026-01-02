# 🏥 Sistema Preditivo de Obesidade

Este projeto apresenta uma **aplicação interativa desenvolvida em Streamlit**
para **predição do nível de obesidade**, utilizando técnicas de **Machine Learning**.

O sistema foi desenvolvido como parte do **Tech Challenge – Fase 4 (Data Analytics)**,
com foco em **apoio à decisão clínica**.

---

## 🎯 Objetivo do Projeto

- Predizer o **nível de obesidade** de pacientes
- Utilizar dados **clínicos e comportamentais**
- Oferecer uma **interface intuitiva e interativa**
- Demonstrar a aplicação prática de **Machine Learning na área da saúde**

> ⚠️ **Aviso**  
> Este sistema é apenas um **apoio à decisão** e **não substitui**
> a avaliação de um profissional de saúde.

---

## 🧠 Modelo de Machine Learning

- **Algoritmo escolhido:** XGBoost Classifier
- **Critério de escolha:** Melhor desempenho entre os modelos avaliados

### Modelos testados:
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- **XGBoost (melhor resultado)**

O modelo final foi treinado, avaliado e salvo utilizando **Joblib**.

---

## 🧩 Funcionalidades da Aplicação

### 🏠 Página Inicial
- Apresentação do sistema
- Orientações gerais
- Navegação pelo menu lateral

### 🧮 Página de Predição
- Formulário dividido em:
  - **Dados do Paciente**
  - **Hábitos Alimentares e Refeições**
- Inputs em **Português (pt-BR)**
- Conversão automática para o formato esperado pelo modelo
- Exibição do **nível de obesidade previsto**

### 📊 Página de Análise de Dados
- Gráficos exploratórios
- Visualização de padrões do dataset disponibilizado para treinamento do modelo
- Apoio à interpretação dos dados utilizados no treinamento
