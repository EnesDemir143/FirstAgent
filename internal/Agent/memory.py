from typing import TypedDict, Union, Optional
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages = Optional[Union[BaseMessage]]