from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_something():
    return {"mesage": "hello wolrd"}
