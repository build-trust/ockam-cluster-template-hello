from ockam import Agent, Node


async def main(node):
    agent = await Agent.start(node, "You are Jack Sparrow.", "jack")


Node.start(main)
