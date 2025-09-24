from fastapi import FastAPI, Request
from agent import ask_agent
import uvicorn

application = FastAPI()


@application.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_msg = body.get("message")
    if not user_msg:
        return {"error": "No message provided"}

    # Call the agent
    response = await ask_agent(user_msg)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run("application:application", host="127.0.0.1", port=8000, reload=True)
