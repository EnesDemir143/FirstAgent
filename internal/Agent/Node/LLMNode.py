from langchain_openai import ChatOpenAI
from memory import AgentState
from langchain_core.messages import SystemMessage

def llm_node(llm: ChatOpenAI, state: AgentState) -> AgentState:
    '''This node is responsible for invoke llm.
    Then After the llm call depend on the response call the end or again use tool.'''

    system_message = SystemMessage(content='You are a very helpful assistant for read some documents.Then you get inference on them.But just about this documents.You are get the inference and if you need some research on internet.Then you ouse some Tools.')

    response = llm.invoke([system_message] + state['messages'])
    state['messages'].append(response)
    return state