import pytest
from app import app

# Sample mock data
MOCK_MEDICINES = [
    {"Medicine": "Paracetamol"},
    {"Medicine": "Aspirin"},
    {"Medicine": "Ibuprofen"},
]


@pytest.fixture
def client(monkeypatch):
    """
    Flask test client with mocked read_medicines
    """

    def mock_read_medicines():
        return MOCK_MEDICINES

    # Patch read_medicines inside app module
    monkeypatch.setattr("app.read_medicines", mock_read_medicines)

    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_get(client):
    response = client.get("/")
    assert response.status_code == 200
    for med in MOCK_MEDICINES:
        assert med["Medicine"] in response.get_data(as_text=True)