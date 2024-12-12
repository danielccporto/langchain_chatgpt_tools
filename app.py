import streamlit as st
from src.agents.gemini_agent import create_agent

# Configuração inicial
st.set_page_config(page_title="LangChain ChatGPT Demo", layout="wide")

# Título da aplicação
st.title("LangChain Agent com ChatGPT")

# Inicializar o agente
st.sidebar.header("Configuração do Agente")
agent = create_agent()
st.sidebar.success("Agente inicializado com sucesso!")

# Entrada do usuário
user_input = st.text_input("Digite sua consulta (ex: previsão do tempo, notícias):")

# Botão para executar
if st.button("Enviar"):
    if user_input:
        try:
            response = agent.run(user_input)
            st.write(response)
        except Exception as e:
            st.error(f"Erro durante a execução: {str(e)}")
    else:
        st.warning("Por favor, insira uma consulta!")
