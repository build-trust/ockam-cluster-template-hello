from ockam import Agent, Node, Repl
from sys import argv


async def main(node):
    agent = await Agent.start(node, "You are Jack Sparrow.")
    await Repl.start(agent, argv[1])


Node.start(main)
