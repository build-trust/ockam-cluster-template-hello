import os
import sys

from ockam import Agent, Model, Node, info


async def main(node):
    agent = await Agent.start(
        node=node,
        model=Model(name="bedrock/amazon.titan-text-lite-v1"),
        instructions="""
            You are Henry, an expert legal assistant.
            You have in-depth knowledge of United States corporate law.
        """,
    )

    await agent.repl(listen_address=f"127.0.0.1:{sys.argv[1]}")

    # Wait for CTRL+C
    try:
        await node.stop_on_sigint()
    except asyncio.exceptions.CancelledError:
        pass


if __name__ == "__main__":
    node_name = f"{os.environ['CLUSTER']}-{os.environ['ZONE']}-{os.environ['NODE']}"
    print(f"Starting node {node_name}", flush=True)
    Node.start(main, name=node_name, ticket=os.environ['ENROLLMENT_TICKET'])
