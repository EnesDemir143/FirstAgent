from langchain.tools import tool

from internal.Agent.memory import AgentState

@tool
def retriever_in_db(state: AgentState, query: str) -> str:
    '''This tool is using query parameters for searching most releated things on vector db.'''
    retriever = state['vectordb'].as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5} 
    )
    docs = retriever.invoke(query)

    results = []
    for i, doc in enumerate(docs):
        results.append(f"Document {i+1}:\n{doc.page_content}")
    
    return "\n\n".join(results)
    