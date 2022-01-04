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


@app.get("/")
async def read_todos():
    data = [
        {
            "key": "1",
            "item": "Learn Next.js",
            "status": "Done",
        },
        {
            "key": "2",
            "item": "Learn FastAPI",
            "status": "Not Done Yet",
        },
    ]

    return data


class Item(BaseModel):
    item: str
    status: str


@app.post("/")
async def create_todo(item: Item):
    return item
