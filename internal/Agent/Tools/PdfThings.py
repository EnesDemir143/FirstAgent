import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from pathlib import Path
from langchain.tools import tool
from internal.Agent.memory import AgentState

@tool
def document_loader(state: AgentState, path: str) -> AgentState:
    '''This Tool is uses for reading documents then load to a vector database.Vectordb is storeing in state.'''
    if not os.path.exists(path):
        raise FileNotFoundError(f"PDF file not found: {path}")

    if path in '.pdf':
        doc = PyPDFLoader(path)

    pages = doc.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
        )
    
    pages_split = text_splitter.split_documents(pages)

    dir_name = 'internal/DataBase/VectorBase'
    file_name = str(Path(path).stem)

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    embedding = None
    
    try:
        vector_store = Chroma(
            document=pages_split,
            collection_name=file_name,
            persist_directory=dir_name,
            embedding=embedding
        )
        state['vectordb'] = vector_store
        print("Created ChromaDB vector store!")
    
    except Exception as e:
        print(f"Error setting up ChromaDB: {str(e)}")
        raise

    return state
        



