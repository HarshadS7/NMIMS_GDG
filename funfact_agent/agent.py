from google.adk.agents import Agent
from google.genai import types 
from google.adk.tools import google_search

# funfact_agent/agent.py

# Define the agent instance (must be named `agent` for ADK CLI)
root_agent = Agent(
    name="finance_funfact",
    model="gemini-2.0-flash",
    description="You are a finance fun fact agent that loves to search the web",
    instruction=(
        "You are a finance fun fact agent that loves to search the web. "
        "You will be given a user query and you will search the web to find "
        "the best answer for the user, and advise with a fun fact about finance "
        "when given the keyword funfact."
    ),
    tools=[google_search]
)

# Example function to query the agent with custom temperature
async def query_agent(user_query: str, temp: float = 0.7):
    """
    Sends a query to the agent with a custom temperature.

    :param user_query: The question you want the agent to answer
    :param temp: Creativity level (0 = deterministic, 1 = very creative)
    :return: Agent's response
    """
    response = await agent.chat(user_query, temperature=temp)
    return response
