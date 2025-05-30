from typing import TypedDict, Union, Optional
from langchain_core.messages import BaseMessage
from langchain_chroma import Chroma

class AgentState(TypedDict):
    messages = Optional[Union[BaseMessage]]
    vectordb = Optional[Chroma]