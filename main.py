from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return "Welcome to the To Do App"
