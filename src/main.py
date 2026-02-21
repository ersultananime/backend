print("Hello World!")
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World! Сәлем, бұл біздің жеткізу қызметінің API-ы"}
