#2
def test_metrics_route(client):
    # Сначала делаем запрос к /time, чтобы увеличить счётчик
    client.get('/time')
    response = client.get('/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert data['count'] == 1
  
