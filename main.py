"""
Health Universe A2A Agent Template

This is a minimal agent template. Customize the MyAgent class to build your agent.

Run with:
    uv run python main.py

Your agent will be available at http://localhost:8000
"""

import os

import uvicorn

from health_universe_a2a import Agent, AgentContext, create_app


class MyAgent(Agent):
    """A simple echo agent - replace with your own logic."""

    def get_agent_name(self) -> str:
        return "My Agent"

    def get_agent_description(self) -> str:
        return "A simple agent that echoes back the user's message"

    async def process_message(self, message: str, context: AgentContext) -> str:
        # Send a progress update
        await context.update_progress("Processing your message...", progress=0.5)

        # Your agent logic goes here
        result = f"You said: {message}"

        return result


# Create the ASGI app
app = create_app(MyAgent())

if __name__ == "__main__":
    # Configuration from environment
    port = int(os.getenv("PORT", os.getenv("AGENT_PORT", "8000")))
    host = os.getenv("HOST", "0.0.0.0")
    reload = os.getenv("RELOAD", "false").lower() == "true"

    # Run the server
    uvicorn.run(
        "main:app" if reload else app,
        host=host,
        port=port,
        reload=reload,
        log_level="info",
    )
