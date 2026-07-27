from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#in-memory list
tasks = [
    {"id":1, "title":"buy rice", "done":True},
    {"id":2, "title":"walk the dog", "done":True},
    {"id":3, "title":"attend sociology class","done":False}
    ]

#input schema

class CreateTask(BaseModel):
    title:str

#root api
@app.get("/")
def read_roots() -> dict:
    return {
        "name":"Task API",
        "version":"1.0",
        "endpoints":["/tasks"]
    }

#health check api
@app.get("/health")
def health_check() -> dict:
    return {"status":"ok"}

#get api to retunr the whole tasks
@app.get("/tasks")
def get_tasks() -> list:
    return tasks

#get a particular task by id
@app.get("/tasks/{task_id}")
def get_task(task_id:int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task 
    raise HTTPException(status_code=404, detail =  {"error": "Task not found"})

#post a new task
@app.post("/tasks", status_code = 202)
def create_task(task: CreateTask):
    if not task.title or not task.title.strip():
        raise HTTPException(status_code=400, detail = "404 not found")
    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id":new_id, "title":task.title, "done":False}
    return new_task
