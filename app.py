from fastapi import FastAPI, HTTPException

app = FastAPI()


tasks = [
    {"id":1, "title":"buy rice", "done":True},
    {"id":2, "title":"walk the dog", "done":True},
    {"id":3, "title":"attend sociology class","done":False}
    ]

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