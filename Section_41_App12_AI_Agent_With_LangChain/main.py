import os
import uuid

import gradio as gr
from anyio.lowlevel import checkpoint

from dotenv import load_dotenv
from datetime import datetime
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

load_dotenv(verbose=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def get_date():
    """Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")


conn = sqlite3.connect("agent_memory.sqlite", check_same_thread=False)
checkpointer = SqliteSaver(conn)

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
    checkpointer=checkpointer,
    tools=[
        get_date
    ]
)


# user_query = input("Enter a Query: ")

# print("AI Answer:", ai_answer)

def chat(message, history, thread_id):
    config = {"configurable": {"thread_id": thread_id}}
    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    },
        config=config
    )

    all_messages = response["messages"]
    # ai_answer = all_messages[-1].content[0]['text']
    ai_answer = all_messages[-1].content
    return ai_answer


with gr.Blocks() as demo:
    gr.Markdown("# AI Agent")
    thread_id = gr.State(value = lambda: str(uuid.uuid4()))
    gr.ChatInterface(fn=chat, additional_inputs=[thread_id])

demo.launch()
