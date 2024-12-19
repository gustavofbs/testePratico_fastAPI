# testePratico_fastAPI

## Requisitos para executar o teste prático:

Poetry | Versão utilizada: 1.8.5
Python | Versão utilizada: 3.12.8


## Como executar

Entre na pasta do projeto:

```bash
cd toDo_list
```
Inicie o servidor

```bash
fastapi dev todo_list/app.py
```

## Dependências Instaladas

### FastAPI

```bash
poetry add 'fastapi[standard]'
```

## Documentação Automática do Swagger UI

### GET

<center> 

![GET](./assets/getDoc.png)

| Parâmetro    | Tipo | Obrigatório | Descrição                |
|--------------|------|-------------|--------------------------|

</center>

___

### POST

<center>

![POST](./assets/postDoc.png)

| Parâmetro    | Tipo | Obrigatório | Descrição                |
|--------------|------|-------------|--------------------------|
| title        | str  | Sim         | O título da tarefa       |
| description  | str  | Não         | A descrição da tarefa    |

</center>

___

### PUT

<center>

![PUT](./assets/putDoc.png)

| Parâmetro    | Tipo | Obrigatório | Descrição                |
|--------------|------|-------------|--------------------------|
| task_id      | str  | Sim         | O ID da tarefa           |
| status       | str  | Sim         | Novo status da tarefa    |

</center>

___

### DELETE

<center>

![DELETE](./assets/deleteDoc.png)

| Parâmetro    | Tipo | Obrigatório | Descrição                |
|--------------|------|-------------|--------------------------|
| task_id      | str  | Sim         | O ID da tarefa           |

</center>