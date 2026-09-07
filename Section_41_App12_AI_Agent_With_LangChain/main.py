import os
import gradio as gr

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

# user_query = input("Enter a Query: ")

# print("AI Answer:", ai_answer)

def chat(message, history):
    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    })

    all_messages = response["messages"]
    # ai_answer = all_messages[-1].content[0]['text']
    ai_answer = all_messages[-1].content
    return ai_answer


with gr.Blocks() as demo:
    gr.Markdown("# AI Agent")
    gr.ChatInterface(fn=chat)

demo.launch()