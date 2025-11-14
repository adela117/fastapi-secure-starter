from fastapi.testclient import TestClient
from app.main import app

c = TestClient(app)


def test_health():
    r = c.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_echo():
    r = c.post("/echo", json={"message": "hi", "count": 2})
    assert r.status_code == 200
    body = r.json()
    assert body["echo"] == "hi"
    assert body["count"] == 2
