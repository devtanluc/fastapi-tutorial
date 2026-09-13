import uuid

from typing import Annotated, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=100)]
    desc: Annotated[Optional[str], Field(min_length=1, max_length=1000)] = None


class TodoUpdate(BaseModel):
    title: Annotated[Optional[str], Field(min_length=1, max_length=100)] = None
    desc: Annotated[Optional[str], Field(min_length=1, max_length=1000)] = None


class TodoResponse(BaseModel):
    todo_id: str
    title: str
    desc: Optional[str] = None


app = FastAPI()

db: dict[str, TodoResponse] = {}


def new_id() -> str:
    """Tạo id ngẫu nhiên."""
    return uuid.uuid4().hex


def get_todo_or_404(todo_id: str) -> TodoResponse:
    todo: TodoResponse | None = db.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")
    return todo


@app.get("/items", response_model=list[TodoResponse])
def read_items():
    return list(db.values())


@app.post("/items", response_model=TodoResponse, status_code=201)
def create_item(payload: TodoCreate):
    todo_id: str = new_id()
    new_todo = TodoResponse(todo_id=todo_id, **payload.model_dump())
    db[todo_id] = new_todo
    return new_todo


@app.patch("/items/{todo_id}", response_model=TodoResponse)
def update_item(todo_id: str, todo: TodoUpdate):
    existing: TodoResponse = get_todo_or_404(todo_id)
    updated: TodoResponse = existing.model_copy(update=todo.model_dump(exclude_unset=True))
    db[todo_id] = updated
    return updated


@app.delete("/items/{todo_id}", status_code=204)
def delete_item(todo_id: str):
    get_todo_or_404(todo_id)
    del db[todo_id]