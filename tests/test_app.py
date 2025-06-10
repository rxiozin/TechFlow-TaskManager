import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Tarefas' in rv.data or b'Bem-vindo' in rv.data

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Testar API'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Testar API'
    assert data['completed'] is False

def test_get_tasks(client):
    client.post('/tasks', json={'title': 'Outra Tarefa'})
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any(task['title'] == 'Outra Tarefa' for task in data)

def test_update_task(client):
    # Criar uma tarefa
    response = client.post('/tasks', json={'title': 'Para atualizar'})
    task_id = response.get_json()['id']
    # Atualizar
    response = client.put(f'/tasks/{task_id}', json={'title': 'Atualizada', 'completed': True})
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Atualizada'
    assert data['completed'] is True

def test_delete_task(client):
    # Criar
    response = client.post('/tasks', json={'title': 'Para deletar'})
    task_id = response.get_json()['id']
    # Deletar
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 204
    # Verificar que não existe mais
    response = client.get('/tasks')
    data = response.get_json()
    assert all(task['id'] != task_id for task in data)
