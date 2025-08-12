import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.mark.hello
def test_hello_world(client):
    response = client.get('/hello')
    data = response.get_json()
    assert response.status_code == 200
    assert data['message'] == 'World!'


@pytest.mark.favorites
def test_favorites_valid_topic(client):
    response = client.get('/favorites?topic=animal')
    data = response.get_json()
    assert response.status_code == 200
    assert data['message'] == "Kevin's Favorite animal is 'dog'!"


@pytest.mark.favorites
def test_favorites_invalid_topic(client):
    response = client.get('/favorites?topic=invalid_topic')
    data = response.get_json()
    assert response.status_code == 200
    assert 'error' in data


@pytest.mark.joke
def test_joke(client):
    response = client.get('/joke')
    data = response.get_json()
    assert response.status_code == 200
    assert 'joke' in data


if __name__ == '__main__':
    pytest.main()
