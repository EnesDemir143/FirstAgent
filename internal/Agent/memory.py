from typing import Any, Dict, TypedDict, Optional, List
from langchain_core.messages import BaseMessage
from langchain_chroma import Chroma


class AgentState(TypedDict):
    messages: List[BaseMessage]
    vectordb:  Optional[Any]
    tools_dict:  Dict 