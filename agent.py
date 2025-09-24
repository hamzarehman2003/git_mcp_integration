import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY environment variable")


async def ask_agent(user_message: str) -> str:
    """Send a user message through an Agent configured with the Git MCP server."""
    # Configure how to start the MCP server (stdio transport)
    git_mcp = MCPServerStdio(
        params={
            "command": "uvx",
            "args": ["mcp-server-git"]
        },
        name="git",
        client_session_timeout_seconds=10
    )

    # Use context manager so that subprocess is cleaned up
    async with git_mcp as mcp_server:
        agent = Agent(
            name="MyAgent",
            instructions="You are a helpful assistant. Use git tools when needed.",
            mcp_servers=[mcp_server]
        )

        result = await Runner.run(agent, user_message)
        print("skbsd")
        return result.final_output
