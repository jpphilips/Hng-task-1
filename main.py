from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI(
    title="College API",
    description="An api endoint that returns a json response for Hng internship",
    version="1",
)


@app.get("/")
def home():

    return {
        "slackUsername": "Jp",
        "backend": True,
        "age": 26,
        "bio": "Life is Uncertain; eat first"
    }
