from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="College API",
    description="An api endoint that returns a json response for Hng internship",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_headers=['*'])


@app.get("/")
def home():
    return {
        "slackUsername": "Jp",
        "backend": True,
        "age": 26,
        "bio": "Life is Uncertain; eat first"
    }
