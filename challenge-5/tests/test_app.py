import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_analyze(client):
    response = client.post('/analyze', data={'text': 'I love this!'})
    assert response.status_code == 200
    assert 'label' in response.json[0]
