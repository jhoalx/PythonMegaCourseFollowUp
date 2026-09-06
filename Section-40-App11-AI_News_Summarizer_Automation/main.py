import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(verbose=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(
    model="gemini-3.5-flash-lite",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY,
)

# # To stop the AFC Calling Warning, Assuming 'model' is already initialized...
# model_no_afc = model.bind(
#     automatic_function_calling=AutomaticFunctionCallingConfig(disable=True)
# )


response = model.invoke("Whats the difference between a deterministic and a probabilistic model?")

print(response.text)