from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.routes.todo import todo_router

app = FastAPI()
app.include_router(todo_router)
register_tortoise(
    app=app,
    db_url="sqlite://todo.db",
    add_exception_handlers=True,
    generate_schemas=True,
    modules={
        "models": [
            "api.models.todo_model",
        ],
    },
)


@app.get("/")
def index():
    return {
        "status": "todo-api is running :D",
    }
