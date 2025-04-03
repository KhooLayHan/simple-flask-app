import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    response = client.get('/')
    assert b"Hello, DevOps World!" in response.data