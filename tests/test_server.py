import os
import sys
import json
from datetime import datetime
from datetime import timedelta
from server import Server
from api.middlewares.auth import generate_access_token

def _get_authorization_token(is_admin=False) -> str:
    user = {"username": "flaskeleton", "first_name": 'Flask', 'last_name': 'Eleton', 'is_admin': is_admin}
    expiration = datetime.utcnow() + timedelta(days=1)
    return generate_access_token(user, expiration)

def test_get_version_should_return_api_version():
    app = Server(config_profile="test").app.test_client()
    response = app.get('/version')
    body = json.loads(response.get_data())
    assert response.status_code == 200
    assert body["version"] == "1.0.0"

def test_post_login_should_return_jwt():
    app = Server(config_profile="test").app.test_client()
    credentials = {"username":"flaskeleton", "password":"flaskeleton"}
    response = app.post(
        '/login',
        data=json.dumps(credentials),
        content_type='application/json'
    )
    body = json.loads(response.get_data())
    assert response.status_code == 200
    assert body["token"] is not None

def test_post_todolist_should_create_todolist_of_two_todos():
    app = Server(config_profile="test").app.test_client()
    todolist = ["foo", "bar"]
    response = app.post(
        '/demo/todo-list',
        data=json.dumps(todolist), 
        content_type='application/json',
        headers={"Authorization": "Bearer " + _get_authorization_token()}
    )
    body = json.loads(response.get_data())
    assert response.status_code == 200
    assert len(body["todo_list"]) == 2

def test_put_todolist_should_update_todolist():
    app = Server(config_profile="test").app.test_client()
    todolist = ["foo", "bar", "baz"]
    response = app.post(
        '/demo/todo-list',
        data=json.dumps(todolist), 
        content_type='application/json',
        headers={"Authorization": "Bearer " + _get_authorization_token()}
    )
    body = json.loads(response.get_data())
    assert response.status_code == 200
    assert len(body["todo_list"]) == 3
    
def test_delete_todolist_should_remove_item_from_todolist():
    app = Server(config_profile="test").app.test_client()
    todolist = ["foo"]
    response1 = app.post(
        '/demo/todo-list',
        data=json.dumps(todolist), 
        content_type='application/json',
        headers={"Authorization": "Bearer " + _get_authorization_token(is_admin=True)}
    )
    body1 = json.loads(response1.get_data())
    assert len(body1["todo_list"]) == 1
    item_id = body1["todo_list"][0]["id"]

    response2 = app.delete(
        '/demo/todo-list?id={0}'.format(item_id),
        headers={"Authorization": "Bearer " + _get_authorization_token(is_admin=True)}
    )
    body2 = json.loads(response2.get_data())
    assert response2.status_code == 200
    assert len(body2["todo_list"]) == 0