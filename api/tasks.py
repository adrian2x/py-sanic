from sanic import Blueprint, Request
from sanic.response import HTTPResponse, text

tasks = Blueprint("tasks")


async def my_task():
    print("running...")

@tasks.get("/tasks/news")
async def get_news(request: Request) -> HTTPResponse:
    """Start the function in the background."""
    request.app.add_task(my_task())
    return text("Started", 202)
