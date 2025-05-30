from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode
from internal.Agent.Tools.PdfThings import document_loader
from .memory import AgentState
from Node.LLMNode import llm_node
from Node.SetupNode import setup_node

def should_tool_call() -> str:
    pass

def create_agent() -> None:
    graph = StateGraph(AgentState)

    tools = [document_loader]

    graph.add_node('setup_node', setup_node)
    graph.add_node('llm_node', llm_node)
    graph.add_node('tool_nodes', ToolNode(tools=tools))

    graph.add_edge(START, 'setup_node')
    graph.add_edge('setup_node', 'llm_node')
    graph.add_conditional_edges(
        'llm_node',
        should_tool_call,
        {
            'CoT': 'tool_nodes',
            'end': END
        }
    )

