from langchain_openai import ChatOpenAI
from memory import AgentState
from lana

def llm_node(llm: ChatOpenAI, state: AgentState) -> AgentState:
    '''This node is responsible for invoke llm.
    Then After the llm call depend on the response call the end or again use tool.'''
    system_message = 