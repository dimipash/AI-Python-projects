from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data, including the research topic, summary, sources, and tools used, to a text file. Use this tool to save the final research output.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Searches the web using DuckDuckGo. Use this tool to find information on a wide range of topics, including current events, news, and general knowledge.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=4000)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
wiki_tool = Tool(
    name="wikipedia",
    func=wiki.run,
    description="Searches Wikipedia for concise factual information and summaries on specific entities, concepts, or historical events. Use this for quick overviews and to gather background information, not for up-to-date news or opinions.",
)
