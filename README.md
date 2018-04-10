# Flaskeleton: Flask-RESTful starter kit
 Flaskeleton is a starter kit for [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) applications. It provides code structure and basic authentication system based on [Json Web Token](https://jwt.io/).

![](https://fr.tintin.com/images/tintin/persos/rascar/C1232C3.jpg)

## Getting started
### Prerequisites
#### Python
- [Python 3.6.x](https://www.python.org/downloads/release/python-365/)
- [Pipenv](https://github.com/pypa/pipenv)

### Install dependencies
Run the following command into the `flaskeleton` directory:
```bash
$ pipenv install --python 3.6
```

### Configuration

You will find a configuration file under `api/config/conf.cfg`. Three profiles are stored:
  - DEV: local environment
  - PROD: production environment
  - TEST: test environment

### Launch server
Run this command into the `flaskeleton` directory:
```bash
# In development environment
$ pipenv run python server.py
# In production environment
$ pipenv run python server.py -c PROD
# In test environment
$ pipenv run python server.py -c TEST
```

### Todo list demo
To get familiar with how a Flask-RESTful application works you can run the *todo list* demo and investigate the code under `api/resources/demo`.

The *todo list* demo will let you know how to implement basic CRUD operations and how to protect your resources by connecting them to a JWT authentication system.
#### 1 - Get application's version
###### GET `/version`
After you launched the server verify it is up by requesting the version resource:
```bash
$ curl -X GET http://127.0.0.1:5005/version
```
Response should looks like this:
```bash
{
    "name": "flaskeleton",
    "version": "0.0.1",
    "error": null
}
```
#### 2 - Get logged in
###### POST `/login`
In order to consume *todo list* resources your requests have to be authenticated with an access token. This token is generated when credentials posted on `login` endpoint are valid. Then the token is sent back both in a cookie and in the response body.

For the purpose of the demo authentication has been simplified. User data are hard coded in the *login* resource under `api/resources/login.py`. In the future you will need to overwrite this part and implement your own user data access logic.

Get an access token by posting *flaskeleton* as username and password to the login resource:
```bash
$ curl -X POST http://127.0.0.1:5005/login \
-H 'content-type: application/json' \
-d '{
      "username": "flaskeleton",
      "password": "flaskeleton"
}'
```
Response should looks like this:
```bash
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDM4MTI4fQ.uzEkPtrqkBPyl3G67pniLyQktG5fMrljwjmXVSvBAmI",
    "error": null
}
```
Now you have an access token and can you use it in the next *todo list* requests.

#### 3 - Create a todo list
###### PUT `/todo-list`
Create a todo list prefilled with items with a *PUT* request:
```bash
$ curl -X PUT http://127.0.0.1:5005/todo-list \
-H 'content-type: application/json' \
-H 'Cookie: X-Access-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDM4MTI4fQ.uzEkPtrqkBPyl3G67pniLyQktG5fMrljwjmXVSvBAmI' \
-d '["make my code correct", "make my code clear"]'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "a8088e56-1fd1-436d-9153-c993754d3f35",
            "what": "make my code correct"
        },
        {
            "id": "09eb9c65-9cfd-4402-ae8e-f5a9e732d628",
            "what": "make my code clear"
        }
    ],
    "error": null
}
```

#### 4 - Read todo list's items
###### GET `/todo-list`
Retrieve todo list data with a *GET* request and passed todo's *id* as argument to access a specific todo:
```bash
$ curl -X GET http://127.0.0.1:5005/todo-list?id=a8088e56-1fd1-436d-9153-c993754d3f35 \
-H 'content-type: application/json' \
-H 'Cookie: X-Access-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDM4MTI4fQ.uzEkPtrqkBPyl3G67pniLyQktG5fMrljwjmXVSvBAmI'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "a8088e56-1fd1-436d-9153-c993754d3f35",
            "what": "make my code correct"
        }
    ],
    "error": null
}
```

### Declare new REST resource
To declare a new REST resource you can take inspiration

### Authors
    Martin Tovmassian <martin.tovmassian@protonmail.com>
