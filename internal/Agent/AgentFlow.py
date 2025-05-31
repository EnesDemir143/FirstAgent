from langgraph.graph import START, END, StateGraph
from internal.Agent.Node.ToolExecute import tool_execute_node
from internal.Agent.memory import AgentState
from internal.Agent.Node.LLMNode import llm_node
from internal.Agent.Node.SetupNode import setup_node

def should_tool_call(state: AgentState):
    """Check if the last message contains tool calls."""
    result = state['messages'][-1]
    return hasattr(result, 'tool_calls') and len(result.tool_calls) > 0

def create_agent()  :
    graph = StateGraph(AgentState)

    graph.add_node('setup_node', setup_node)
    graph.add_node('llm_node', llm_node)
    graph.add_node('tool_execute_node', tool_execute_node)

    graph.add_edge(START, 'setup_node')
    graph.add_edge('setup_node', 'llm_node')
    graph.add_conditional_edges(
        'llm_node',
        should_tool_call,
        {
            True: 'tool_execute_node',
            False: END
        }
    )
    graph.add_edge('tool_execute_node', 'llm_node')

    agent = graph.compile()
    return agent 
