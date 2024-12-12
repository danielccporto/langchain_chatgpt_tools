from src.agents.gemini_agent import create_agent

def main():
    agent = create_agent()
    print("Digite sua consulta (ou 'sair' para encerrar):")
    while True:
        user_input = input("> ")
        if user_input.lower() == "sair":
            break
        response = agent.run(user_input)
        print(response)

if __name__ == "__main__":
    main()
