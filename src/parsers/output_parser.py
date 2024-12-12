from langchain.schema import AgentAction, AgentFinish
from langchain.agents import AgentOutputParser
from typing import Union
import re

class CustomOutputParser(AgentOutputParser):
    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        """
        Analisa e ajusta a saída do modelo para garantir o formato correto.
        """
        if "Final Answer:" in text:
            # Caso a saída contenha uma resposta final
            return AgentFinish(
                return_values={"output": text.split("Final Answer:")[-1].strip()},
                log=text
            )

        # Regex para identificar ação e entrada
        match = re.search(r"Action: (.*?)\nAction Input: (.*)", text, re.DOTALL)
        if match:
            action = match.group(1).strip()
            action_input = match.group(2).strip()
            return AgentAction(tool=action, tool_input=action_input, log=text)

        # Força um formato válido se a saída for inválida
        return AgentFinish(
            return_values={"output": "A saída foi ajustada automaticamente devido a problemas de formatação."},
            log=f"Saída inválida foi corrigida:\n{text}"
        )
