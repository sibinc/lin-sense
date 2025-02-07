from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search():
    response = client.post("/api/v1/search", json={"query": "BCOM-IFA-2022 revaluation report 2nd sem"})
    assert response.status_code == 200
    assert "menu" in response.json()
    assert "entities" in response.json()