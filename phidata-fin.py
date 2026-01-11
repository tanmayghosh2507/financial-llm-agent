from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
import openai
import os
from dotenv import load_dotenv

load_dotenv()

web_search_agent = Agent(
    name="Financial Web Search Agent",
    role="Search the web for financial information using DuckDuckGo and provide accurate responses.",
    model="grok-preview", #OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include source and use markdown formatting."],
    show_tool_calls=True,
    markdown=True,
)

openai.api_key = os.getenv("OPENAI_API_KEY")
# print(os.getenv("OPENAI_API_KEY"))
web_search_agent.print_response("Tell me about OpenAI Sora?", stream=True)