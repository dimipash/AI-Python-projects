from langchain_anthropic import ChatAnthropic
from browser_use import Agent, Browser, BrowserConfig, Controller
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List

load_dotenv()

import asyncio


class Post(BaseModel):
    caption: str
    url: str


class Posts(BaseModel):
    posts: List[Post]


controller = Controller(output_model=Posts)

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    )
)

llm = ChatAnthropic(
    model_name="claude-3.5-sonnet-20240620",
    temperature=0.0,
    timeout=100,
)


async def main():
    initial_actions = [
        {"open_tab": {"url": "https://www.instagram.com/thepashi/"}},
    ]
    agent = Agent(
        task="Go the ThePashi Instagram page and get the 5 latest posts.",
        llm=llm,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions,
    )
    result = await agent.run()
    print(result.final_result())
    data = result.final_result()
    Posts = Posts.model_validate_json(data)
    await browser.close()


asyncio.run(main())
