from fastapi import FastAPI
from fastapi_blog.core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def hello():
    return {"message": "Hello from FastAPI with Poetry!"}
