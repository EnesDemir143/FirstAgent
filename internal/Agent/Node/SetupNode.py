from memory import AgentState
from langchain_core.messages import SystemMessage

def setup_node(state:AgentState) -> AgentState:
    '''This node is just setup some messages.'''
    system_message = SystemMessage(content='You are a very helpful assistant for read some documents.Then you get inference on them.But just about this documents.You are get the inference and if you need some research on internet.Then you ouse some Tools.')

    state['messages'] = [system_message]
    return state