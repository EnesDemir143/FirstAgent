import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from pathlib import Path
from langchain.tools import tool
from internal.Agent.memory import AgentState
from langchain_community.embeddings import HuggingFaceEmbeddings


@tool
def document_loader(state: AgentState, path: str) -> AgentState:
    '''This Tool is uses for reading documents then load to a vector database.Vectordb is storeing in state.'''
    if not os.path.exists(path):
        raise FileNotFoundError(f"PDF file not found: {path}")

    if not path.lower().endswith('.pdf'):
        doc = PyPDFLoader(path)

    pages = doc.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
        )
    
    pages_split = text_splitter.split_documents(pages)

    dir_name = 'internal/DataBase/VectorBase'
    file_name = 'vectordb'

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    embedding = HuggingFaceEmbeddings(
        model_name="internal/Agent/Models/models--intfloat--e5-large",
        encode_kwargs={"normalize_embeddings": True} 
    )
    
    try:
        if 'vectordb' in state and state['vectordb'] is not None:
            state['vectordb'].add_documents(pages_split)
        else:
            vector_store = Chroma.from_documents(
                documents=pages_split,
                embedding=embedding,
                persist_directory=dir_name,
                collection_name=file_name
            )
            state['vectordb'] = vector_store

        print("Updated ChromaDB vector store!")
    
    except Exception as e:
        print(f"Error setting up ChromaDB: {str(e)}")
        raise

    return state
        



