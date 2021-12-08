from fastapi import FastAPI, status, HTTPException
from schema.todo import BaseModel, Todo, validator
from fastapi.responses import JSONResponse

app = FastAPI()

todo_list = [{"title": "Python API", "description": "Are you working", "priority": 0}]

@app.get("/")
def home():
    return {"Welcome": "Home"}

@app.get("/api/v1/todos")
def main_get():
    return todo_list

@app.post("/api/v1/todos", status_code=status.HTTP_201_CREATED, response_model=Todo)
def main_post(todo:Todo):
    todo_list.append(todo.dict())
    if todo:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message" : "User created successfully", "data": todo.dict()}
        )

