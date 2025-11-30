from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.agent import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[TavilyTools(), YFinanceTools()],
    debug_mode=True,
)

agent.print_response("Qual é a cotação da petrobras?")
