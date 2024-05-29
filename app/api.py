import uvicorn
from fastapi import FastAPI, Request

app = FastAPI(
    title="DevOps Test API",
    version="1.0",
)


@app.get("/api")
def hello(request: Request):
    return {
        "name": "Hello",
        "description": "World",
        "url": str(request.url)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4444)
