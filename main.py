from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
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
