import pytest
from fastapi.testclient import TestClient
from main import app

class TestHealthCheck:

    @pytest.fixture()
    def client(self):
        return TestClient(app)
    
    def test_health_check(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy", "message": "Service is running"}
