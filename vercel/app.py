from rasa.core.agent import Agent
from sanic import Sanic, response
from sanic.request import Request
from typing import Text

app = Sanic(__name__)

agent = Agent.load("models/")

@app.route("/webhooks/rest/webhook", methods=["POST"])
async def webhook(request: Request) -> response.HTTPResponse:
    data = request.json
    response_text = await agent.handle_text(data["message"])
    return response.json(response_text)

if __name__ == "__main__":
    app.run(port=8000)