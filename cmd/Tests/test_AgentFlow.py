from internal.Agent.AgentFlow import create_agent
from langchain_core.messages import HumanMessage

def test_agent_without_streaming():
    agent = create_agent()
    state = {'messages': [HumanMessage(content='Merhaba benim adım enes.')]}  
    result = agent.invoke(state)
    assert 'messages' in result

test_agent_without_streaming()