from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Financial Risk Analyzer API"}


def test_docs():
    """Test the Swagger UI documentation."""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "Swagger UI" in response.text


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/portfolio/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_404_error():
    """Test accessing a non-existent route."""
    response = client.get("/non-existent")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"
