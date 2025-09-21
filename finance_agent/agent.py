from google.adk.agents import Agent
from google.genai import types 
from google.adk.tools import google_search

# funfact_agent/agent.py

# Define the agent instance (must be named `agent` for ADK CLI)
root_agent = Agent(
    name="finance_agent",
    model="gemini-2.0-flash",
    description="You are an agentic AI that helps plan a user's monthly income efficiently",
    instruction=(
        "You are an agentic AI that helps users plan their monthly income. "
    "As soon as the user says 'hi' or interacts, you will ask for their "
    "monthly income, existing debt, financial goals, and the time horizon "
    "for these goals. Using this information, you will create a personalized "
    "plan to help manage debt, save money, and reach financial goals effectively."
    ),
    tools=[google_search]
)
#monthly income 50000, emi 20000 per month, save 100000, time 6 years

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
