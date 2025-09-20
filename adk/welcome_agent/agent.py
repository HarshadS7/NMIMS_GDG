from google.adk.agents import Agent
from google.genai import types 
from google.adk.tools import google_search


root_agent=Agent(
    name = "basic_search_agent",
    model="gemini-2.0-flash",
    description="this is a pirate era agent that loves to search the web",
    instruction="you are a pirate era agent that loves to search the web. you will be given a user query and you will search the web to find the best answer for the user",
    tools=[google_search]
)                                                     