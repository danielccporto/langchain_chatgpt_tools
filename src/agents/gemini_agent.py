import logging
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
from src.tools.weather_tool import get_weather
from src.tools.news_tool import get_news
from src.memory.memory_setup import get_memory
from src.parsers.output_parser import CustomOutputParser
from src.utils.api_keys import OPENAI_API_KEY

# Configuração de logging
logging.basicConfig(level=logging.DEBUG)

def create_agent():
    logging.info("Inicializando o agente com ChatGPT e ferramentas configuradas...")

    # Configuração do modelo ChatGPT
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        temperature=0.7,
        model="gpt-4",  # Alternativamente, "gpt-3.5-turbo"
    )

    # Lista de ferramentas
    tools = [
        Tool(name="Weather Tool", func=get_weather, description="Consulta condições climáticas."),
        Tool(name="News Tool", func=get_news, description="Busca notícias atualizadas.")
    ]

    # Configuração de memória
    memory = get_memory()

    # Inicialização do agente com parser personalizado
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5,  # Reduzindo para evitar loops longos
        max_execution_time=60,  # Tempo máximo por consulta
        output_parser=CustomOutputParser()
    )
