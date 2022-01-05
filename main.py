from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ========== Start: SPECIFY AllOWED ORIGIN(S) ==========
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== End: SPECIFY AllOWED ORIGIN(S) ==========

# ========== Start: FAKE DATABASE ==========
todos = []
# ========== End: FAKE DATABASE ==========


@app.get("/")
async def read_todos():
    return todos


class Todo(BaseModel):
    item: str


@app.post("/")
async def create_todo(todo: Todo):
    todo = todo.dict()
    todo["status"] = False
    todos.append(todo)
