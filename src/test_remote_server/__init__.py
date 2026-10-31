
from fastmcp import FastMCP
import random
import json

# Create the MCP server
mcp = FastMCP("Test Remote MCP Server")


# Tool 1: Add two numbers
@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum."""
    return a + b


# Tool 2: Generate a random number between 1 and 100
@mcp.tool()
def generate_random_number() -> int:
    """Generate a random integer between 1 and 100, inclusive."""
    return random.randint(1, 100)


# Resource: Server information
@mcp.resource("server://info")
def server_info() -> str:
    """Return information about this MCP server."""

    info = {
        "name": "Test Remote MCP Server",
        "version": "1.0.0",
        "description": "A test remote MCP server with basic tools.",
        "tools": [
            {
                "name": "add_numbers",
                "description": "Add two numbers and return their sum."
            },
            {
                "name": "generate_random_number",
                "description": "Generate a random integer between 1 and 100."
            }
        ],
        "author": "Vivekananda"
    }

    return json.dumps(info, indent=2)


# Start the remote MCP server
if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )
