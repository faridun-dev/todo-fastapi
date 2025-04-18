from fastapi import APIRouter, HTTPException, status
from api.models.todo_model import Todo
from api.schemas.todo import GetTodo, PostTodo, PutTodo


todo_router = APIRouter(prefix="/api/v1", tags=["Todo"])


@todo_router.get("/todos")
async def get_all_todos():
    data = Todo.all()
    return await GetTodo.from_queryset(data)


@todo_router.post("/add")
async def add_todo(body: PostTodo):
    row = await Todo.create(**body.dict(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(row)


@todo_router.put("/edit/{id}")
async def update_todo(id: int, body: PutTodo):
    data = body.dict(exclude_unset=True)
    exists = await Todo.filter(id=id).exists()
    if not exists:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=id).update(**data)
    return await GetTodo.from_queryset_single(Todo.get(id=id))


@todo_router.delete("/delete/{id}")
async def delete_todo(id: int):
    exists = await Todo.filter(id=id).exists()
    if not exists:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=id).delete()
    return "Todo deleted successfully"
