from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: int
    title: Optional[str] = None


app = FastAPI()

# "Database" giả lập - dict để tra cứu nhanh theo id
db: dict[int, Todo] = {}


def get_all_todos() -> list[Todo]:
    """Chuyển đổi dữ liệu lưu trữ (dict) sang dạng trả về API (list)."""
    return list(db.values())


def get_todo_or_404(id: int) -> Todo:
    """Lấy 1 todo theo id, tự raise lỗi nếu không tìm thấy."""
    todo: Todo | None = db.get(id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo {id} not found")
    return todo


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items", response_model=Todo)
def create_item(todo: Todo):
    db[todo.id] = todo
    return todo


@app.get("/items", response_model=list[Todo])
def read_items():
    return get_all_todos()


@app.get("/items/{id}", response_model=Todo)
def read_item(id: int):
    return get_todo_or_404(id)