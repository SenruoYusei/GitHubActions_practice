# test_app.py
import pytest
from src.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json == []

def test_create_todo(client):
    response = client.post(
        '/todos',
        json={
            'title': 'Test Todo',
            'description': 'This is a test todo'
        }
        )
    assert response.status_code == 201
    assert response.json['title'] == 'Test Todo'
    assert response.json['description'] == 'This is a test todo'
    assert response.json['done'] == False

def test_get_todo(client):
    client.post(
        '/todos',
        json={
            'title': 'Test Todo',
            'description': 'This is a test todo'
        }
        )
    response = client.get('/todos/1')
    assert response.status_code == 200
    assert response.json['title'] == 'Test Todo'
    assert response.json['description'] == 'This is a test todo'
    assert response.json['done'] == False

def test_update_todo(client):
    client.post(
        '/todos',
        json={
            'title': 'Test Todo',
            'description': 'This is a test todo'
        }
        )
    response = client.put(
        '/todos/1',
        json={
            'title': 'Updated Todo',
            'description': 'This is an updated test todo',
            'done': True
        }
        )
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Todo'
    assert response.json['description'] == 'This is an updated test todo'
    assert response.json['done'] == True

def test_delete_todo(client):
    client.post(
        '/todos',
        json={
            'title': 'Test Todo',
            'description': 'This is a test todo'
        }
        )
    response = client.delete('/todos/1')
    assert response.status_code == 204
    response = client.get('/todos/1')
    assert response.status_code == 404

def test_get_nonexistent_todo(client):
    response = client.get('/todos/999')
    assert response.status_code == 404
    assert response.json == {'error': 'Todo not found'}

def test_update_nonexistent_todo(client):
    response = client.put(
        '/todos/999', 
        json={
            'title': 'Updated Todo',
            'description': 'This is an updated test todo',
            'done': True
        }
    )
    assert response.status_code == 404
    assert response.json == {'error': 'Todo not found'}

def test_delete_nonexistent_todo(client):
    response = client.delete('/todos/999')
    assert response.status_code == 204

def test_create_todo_without_description(client):
    response = client.post(
        '/todos',
        json={
            'title': 'Test Todo'
        }
    )
    assert response.status_code == 201
    assert response.json['title'] == 'Test Todo'
    assert response.json['description'] == ''
    assert response.json['done'] == False

def test_create_todo_without_title(client):
    response = client.post(
        '/todos',
        json={
            'description': 'This is a test todo'
        }
    )
    assert response.status_code == 400  # Assuming your app returns 400 for missing title