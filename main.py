from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todo = []


@app.get("/todos")
async def get_todos():
    return {"data": todo}


@app.get("/todos/{todo_id}")
async def get_todos(todo_id: int):
    for t in todo:
        if t.id == todo_id:
            return {"data": t}
    return {"message": "Todo not found"}


@app.post("/todos")
async def create_todo(todo_item: Todo):
    todo.append(todo_item)
    return {"message": "Todo item added"}


@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_item: Todo):
    for t in todo:
        if t.id == todo_id:
            t.item = todo_item.item
            return {"message": "Todo item updated"}
    return {"message": "Todo not found"}


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for t in todo:
        if t.id == todo_id:
            todo.remove(t)
            return {"message": "Todo item deleted"}
    return {"message": "Todo not found"}
