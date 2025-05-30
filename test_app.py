import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_time_route(client):
    response = client.get('/time')
    assert response.status_code == 200
    data = response.get_json()
    assert 'time' in data
    assert data['time'] != 0
def test_metrics_route(client):
    # Сначала делаем запрос к /time, чтобы увеличить счётчик
    client.get('/time')
    response = client.get('/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert data['count'] == 1
  

