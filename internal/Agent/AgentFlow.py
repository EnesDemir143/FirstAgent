from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from .memory import AgentState
from dotenv import load_dotenv
from Node.LLMNode import llm_node
from Node.SetupNode import setup_node

load_dotenv()

def create_agent():
    llm = ChatOpenAI(temperature=0.0, model='gpt-4o-mini')

    graph = StateGraph(AgentState)

    graph.add_node('setup_node', setup_node)
    graph.add_node('llm_node', llm_node)


