from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from .memory import AgentState
from dotenv import load_dotenv
from Node.LLMNode import llm_node

load_dotenv()

graph = StateGraph(AgentState)

graph.add_node('llm_node', llm_node)



