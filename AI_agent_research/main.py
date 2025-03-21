from dotenv import load_dotenv
from pydantic import BaseModel, field_validator
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

    @field_validator("topic", "summary")
    def check_non_empty_strings(cls, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Must be a non-empty string")
        return value

    @field_validator("sources", "tools_used")
    def check_non_empty_lists(cls, value):
        if not isinstance(value, list):
            raise ValueError("Must be a list")
        if not all(isinstance(item, str) for item in value):
            raise ValueError("All list items must be strings")
        if not value:
            raise ValueError("List cannot be empty")
        return value


def select_llm(model_name: str):
    """Selects the LLM based on user input."""
    if model_name.startswith("claude"):
        return ChatAnthropic(model=model_name)
    elif model_name.startswith("gpt"):
        return ChatOpenAI(model=model_name)
    else:
        raise ValueError(f"Unsupported model: {model_name}")
        # Default to a safe option, e.g., a smaller, faster model.
        # return ChatAnthropic(model="claude-3-5-sonnet-20241022")


parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a research assistant that will help generate a research paper.
Answer the user query and use neccessary tools. 
Wrap the output in this format and provide no other text\n{format_instructions}
""",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{query}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
).partial(format_instructions=parser.get_format_instructions())


tools = [search_tool, wiki_tool, save_tool]


def run_agent_with_selected_llm(query: str, model_name: str = "claude-3-5-sonnet-20241022"):
    """Runs the agent with the specified LLM and query."""
    try:
        llm = select_llm(model_name)
    except ValueError as e:
        print(e)
        return None

    agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
    agent_executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
    )
    try:
        raw_response = agent_executor.invoke(
            {"query": query, "chat_history": []}  # Initialize chat_history
        )
        return raw_response
    except Exception as e:
        print(f"Error during agent execution: {e}")
        print("Please check your environment and API keys.")
        return None


if __name__ == "__main__":
    model_name = input(
        "Enter the LLM model name (e.g., claude-3-5-sonnet-20241022, gpt-3.5-turbo-0125): "
    )
    query = input("What can I help you research today? ")

    raw_response = run_agent_with_selected_llm(query, model_name)

    if raw_response:
        try:
            structured_response = parser.parse(raw_response.get("output"))
            print(structured_response)
        except Exception as e:
            print(f"Error parsing response: {e}")
            print("Raw response from agent:", raw_response)
