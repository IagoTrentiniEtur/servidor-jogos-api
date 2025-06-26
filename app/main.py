from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/status")
def read_status():
    return {"status": "ok"}

@app.get("/jogadores_online")
def get_jogadores():
    with open("app/data/jogadores.json") as f:
        return json.load(f)
