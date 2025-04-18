from fastapi import APIRouter

todo_router = APIRouter(prefix="/api/v1", tags=["Todo"])


@todo_router.get("/todos")
def get_all_todos():
    return "Not Implemented"


@todo_router.post("/add")
def add_todo():
    return "Not Implemented"


@todo_router.put("/edit/{id}")
def update_todo(id: int):
    return "Not Implemented"


@todo_router.delete("/delete/{id}")
def delete_todo(id: int):
    return "Not Implemented"
