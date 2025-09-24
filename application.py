from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from openai import OpenAI

# load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_CLIENT = OpenAI(api_key=OPENAI_API_KEY)

application = FastAPI()


@application.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    if not user_message:
        return {"error": "No message provided"}

    # call OpenAI Responses API
    response = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4o-mini",   # or gpt-4o, gpt-3.5-turbo, etc.
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response.choices[0].message.content
    return {"response": bot_reply}
