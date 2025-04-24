from ockam import Agent, Model, Node
from sys import argv


async def main(node):
    agent = await Agent.start(
        node=node,
        model=Model("bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0"),
        instructions="""
            You are Henry, an expert legal assistant.
            You have in-depth knowledge of United States corporate law.
        """,
    )

    await agent.repl(argv[1])


Node.run(main)
