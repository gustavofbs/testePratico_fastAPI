from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []
task_id_counter = 1

class Task(BaseModel):
    title: str
    description: Optional[str] = None


class UpdateTaskStatus(BaseModel):
    status: str


@app.post('/tasks')
def create_task(task: Task):
    global task_id_counter
    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "status": "pending"
    }

    tasks.append(new_task)
    task_id_counter += 1
    return new_task

@app.get('/tasks')
def list_tasks():
    return tasks

@app.put('/tasks/{task_id}')
def update_task(task_id: int, update: UpdateTaskStatus):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = update.status
            return task
    raise HTTPException(status_code=404, detail='Task Not Found')

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return {"message": "Task deleted sucessfuly"}
