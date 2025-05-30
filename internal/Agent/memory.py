from typing import Dict, TypedDict, Optional, List
from langchain_core.messages import BaseMessage
from langchain_chroma import Chroma
from operator import add as add_messages


class AgentState(TypedDict):
    messages = List[BaseMessage]
    vectordb = Optional[Chroma]
    tools_dict = Dict 