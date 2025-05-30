from typing import Dict, TypedDict, Union, Optional
from langchain_core.messages import BaseMessage
from langchain_chroma import Chroma

class AgentState(TypedDict):
    messages = Optional[Union[BaseMessage]]
    vectordb = Optional[Chroma]
    tools_dict = Dict 