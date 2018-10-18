import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import Server

def get_authentication_header(is_admin=False) -> dict:
    app = Server(config_profile="test").app.test_client()
    credentials = {"username": "flaskeleton", "password": "flaskeleton", "is_admin": is_admin}
    response = app.post('/login', data=json.dumps(credentials), content_type='application/json')
    jwt = json.loads(response.get_data())["token"]
    return {"Cookie": "X-Access-Token=" + jwt}

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

def test_get_todolist_whitout_authentication_should_raise_unauthorized_exception():
    app = Server(config_profile="test").app.test_client()
    response = app.get('/demo/todo-list')
    assert response.status_code == 401

def test_post_todolist_should_create_todolist():
    app = Server(config_profile="test").app.test_client()
    auth_header = get_authentication_header()
    todolist = ["foo", "bar"]
    response = app.post(
        '/demo/todo-list',
        data=json.dumps(todolist), 
        content_type='application/json',
        headers={**auth_header}
    )
    body = json.loads(response.get_data())
    assert response.status_code == 200
    assert len(body["todo_list"]) == 2

def test_put_todolist_should_update_todolist():
    app = Server(config_profile="test").app.test_client()
    auth_header = get_authentication_header()
    todolist = ["foo", "bar", "baz"]
    response = app.post(
        '/demo/todo-list',
        data=json.dumps(todolist), 
        content_type='application/json',
        headers={**auth_header}
    )
    body = json.loads(response.get_data())
    assert response.status_code == 200
    assert len(body["todo_list"]) == 3
    
def test_delete_todolist_should_remove_item_from_todolist():
    app = Server(config_profile="test").app.test_client()
    auth_header = get_authentication_header(is_admin=True)
    todolist = ["foo"]
    response1 = app.post(
        '/demo/todo-list',
        data=json.dumps(todolist), 
        content_type='application/json',
        headers={**auth_header}
    )
    body1 = json.loads(response1.get_data())
    assert len(body1["todo_list"]) == 1
    item_id = body1["todo_list"][0]["id"]

    response2 = app.delete(
        '/demo/todo-list?id={0}'.format(item_id),
        headers={**auth_header}
    )
    body2 = json.loads(response2.get_data())
    assert response2.status_code == 200
    assert len(body2["todo_list"]) == 0