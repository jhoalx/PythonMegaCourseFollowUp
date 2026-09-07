import os

from dotenv import load_dotenv
from datetime import datetime
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(verbose=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def get_date():
    """Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")


# llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    openai_api_key="none"
)

system_prompt = """
You are a helpful Assistant.
use the get_date tool if the uer is asking about the today's date
"""

agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    tools=[
        get_date
    ]
)

user_query = input("Enter a Query: ")

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": user_query
        }
    ]
})

all_messages = response["messages"]
#ai_answer = all_messages[-1].content[0]['text']
ai_answer = all_messages[-1].content

print("AI Answer:", ai_answer)