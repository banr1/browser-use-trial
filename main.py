from browser_use import Agent, ChatGoogle
import asyncio

from dotenv import load_dotenv

async def example():
    # browser = Browser(
    #     # use_cloud=True,  # Uncomment to use a stealth browser on Browser Use Cloud
    # )
    load_dotenv()

    llm = ChatGoogle(model='gemini-flash-latest')

    agent = Agent(
        task="Find the number of stars of the tsl-formal-verification GitHub repository",
        llm=llm,
        # browser=browser,
    )

    history = await agent.run()
    return history

if __name__ == "__main__":
    history = asyncio.run(example())
