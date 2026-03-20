from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

root_agent = LlmAgent(
    name="weather_time_agent",
    model="gemini-2.5-flash",
    description="Agent to answer questions about the weather in a city.",
    instruction="You are a helpful agent who can answer user questions about the weather in a city. "
    "Use the geocoding tool to find coordinates for a city name, then use weather_forecast to get the weather. "
    "If geocoding returns no results, use your knowledge to estimate the coordinates. "
    "You can respond in the user's language.",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "open-meteo-mcp-server"],
                ),
            ),
        ),
    ],
)
