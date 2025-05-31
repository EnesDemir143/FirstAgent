from langchain_openai import ChatOpenAI
from internal.Agent.Tools.PdfThings import document_loader
from internal.Agent.Tools.RetrieverInVB import retriever_in_db
from internal.Agent.memory import AgentState
from dotenv import load_dotenv
import os

load_dotenv('internal/.env')

def llm_node(state: AgentState) -> AgentState:
    '''This node is responsible for invoke llm.
    Then After the llm call depend on the response call the end or again use tool.'''
    tools = [document_loader, retriever_in_db]
    llm = ChatOpenAI(temperature=0.0, model='gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY')).bind_tools(tools=tools)
    response = llm.invoke(list(state['messages']))
    state['messages'].append(response)
    return state