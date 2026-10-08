import asyncio
import os
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[r"mcp\server.py"],
        cwd=r"C:\Users\Bindu\OneDrive\Documents\AI-IT-Helpdesk",
        env={
            **os.environ,
            "PYTHONPATH": r"C:\Users\Bindu\OneDrive\Documents\AI-IT-Helpdesk"
        }
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("MCP server connected successfully!")

            tools = await session.list_tools()

            print("\nAvailable MCP tools:")

            for tool in tools.tools:
                print("-", tool.name)


asyncio.run(main())