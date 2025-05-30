from langchain_openai import ChatOpenAI
from memory import AgentState
from dotenv import load_dotenv

load_dotenv()

def llm_node(state: AgentState, llm: ChatOpenAI) -> AgentState:
    '''This node is responsible for invoke llm.
    Then After the llm call depend on the response call the end or again use tool.'''

    response = llm.invoke(state['messages'])
    state['messages'].append(response)
    return state