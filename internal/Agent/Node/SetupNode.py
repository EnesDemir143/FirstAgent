from langchain_openai import ChatOpenAI
from internal.Agent.Tools.PdfThings import document_loader
from internal.Agent.Tools.RetrieverInVB import retriever_in_db
from memory import AgentState
from langchain_core.messages import SystemMessage

def setup_node(state:AgentState) -> AgentState:
    '''This node is just setup some messages.'''
    system_message = SystemMessage(content='You are a very helpful assistant for read some documents.Then you get inference on them.But just about this documents.You are get the inference and if you need some research on internet.Then you ouse some Tools.')

    state['messages'] = [system_message]
    tools = [document_loader, retriever_in_db]
    state['tools_dict'] = {our_tool.name: our_tool for our_tool in tools}
    llm = ChatOpenAI(temperature=0.0, model='gpt-4o-mini').bind_tools(tools=tools)
    return state, llm