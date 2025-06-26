from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_jogadores_online():
    response = client.get("/jogadores_online")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
