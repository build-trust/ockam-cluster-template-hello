from ockam import Agent, Node


async def main(node):
    await Agent.start(node, "You are Jack Sparrow.", "jack")


Node.start(main)
