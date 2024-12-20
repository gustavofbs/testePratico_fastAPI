from typing import Literal, Optional

from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from pydantic import BaseModel

app = FastAPI()

tasks = []
task_id_counter = 1


class Task(BaseModel):
    title: str
    description: Optional[str] = None

# Optei em alterar o UpdateTaskStatus tendo em vista que o status deve ser 'pending' ou 'completed'
class UpdateTaskStatus(BaseModel):
    status: Literal['pending', 'completed']


@app.post('/tasks')
def create_task(task: Task):
    global task_id_counter

    # Exceção para quando o title estiver vazio
    if len(task.title.strip()) == 0:
        raise HTTPException(
            status_code=400, detail="Bad Request"
        )
    
    new_task = {
        'id': task_id_counter,
        'title': task.title,
        'description': task.description,
        'status': 'pending',
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
    task_found = False  # Como um "sentinela", ele muda o estado de False para True na condição abaixo, caso o "id" da exclusão exista

    # Percorre a lista, inserindo aquelas tarefas que não fazem parte do "id" escolhido pelo usuário, isso se ela existir
    tasks = [
        task
        for task in tasks
        if not (task['id'] == task_id and (task_found := True))
    ]

    if not task_found:
        raise HTTPException(status_code=404, detail='Task Not Found')

    return {'message': 'Task deleted successfully'}
