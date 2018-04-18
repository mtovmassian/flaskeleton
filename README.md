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
$ pipenv run python server.py -c <config profile>
```

### Todo list demo
To get familiar with how a Flask-RESTful application works you can run the *todo list* demo and investigate the code under `api/resources/demo`.

The *todo list* demo will let you know how to implement basic CRUD operations and how to protect your resources by connecting them to a JWT authentication system.

#### ● GET `/version`
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
#### ● POST `/login`
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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDQwMzk5fQ.4uEdaR6qUIg-76NcS2q40xXUJH3Plzl4fKwvRb5HEf8",
    "error": null
}
```
Now you have an access token and can you use it in the next *todo list* requests.

#### ● PUT `/demo/todo-list`
**Create** a prefilled todo list with a *PUT* request:
```bash
$ curl -X PUT http://127.0.0.1:5005/todo-list \
-H 'content-type: application/json' \
-H 'Cookie: X-Access-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDQwMzk5fQ.4uEdaR6qUIg-76NcS2q40xXUJH3Plzl4fKwvRb5HEf8' \
-d '["make my code correct", "make my code clear"]'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "b716cdd1-31f0-49c0-82cd-0f01acb4af3a",
            "what": "make my code correct"
        },
        {
            "id": "2ce6086a-5bba-45f9-ae9c-7a05166e9705",
            "what": "make my code clear"
        }
    ],
    "error": null
}
```

#### ● GET `/demo/todo-list`
**Read** todo list items with a *GET* request and passed item's *id* as argument to select specific element:
```bash
$ curl -X GET http://127.0.0.1:5005/todo-list?id=b716cdd1-31f0-49c0-82cd-0f01acb4af3a \
-H 'content-type: application/json' \
-H 'Cookie: X-Access-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDQwMzk5fQ.4uEdaR6qUIg-76NcS2q40xXUJH3Plzl4fKwvRb5HEf8'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "b716cdd1-31f0-49c0-82cd-0f01acb4af3a",
            "what": "make my code correct"
        }
    ],
    "error": null
}
```

#### ● POST `/demo/todo-list`
**Update** todo list with new items with a *POST* request:
```bash
$ curl -X POST http://127.0.0.1:5005/todo-list \
-H 'content-type: application/json' \
-H 'Cookie: X-Access-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDQwMzk5fQ.4uEdaR6qUIg-76NcS2q40xXUJH3Plzl4fKwvRb5HEf8' \
-d '["make my code concise", "make my code fast"]'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "b716cdd1-31f0-49c0-82cd-0f01acb4af3a",
            "what": "make my code correct"
        },
        {
            "id": "2ce6086a-5bba-45f9-ae9c-7a05166e9705",
            "what": "make my code clear"
        },
        {
            "id": "7a50909c-d811-4000-a723-a02a182b85d7",
            "what": "make my code concise"
        },
        {
            "id": "07b37bc2-9c51-4c5e-b1f8-cc22e9797e7b",
            "what": "make my code fast"
        }
    ],
    "error": null
}
```

#### ● DELETE `/demo/todo-list` (need administrator privillege)
To illustrate privillege management this operation require an administrator role. The token you used previously is no more valid since the way you authenticated yourself did not give you enough privillege. To do so get an administrator access token by posting this infos to the login resource:
```bash
$ curl -X POST http://127.0.0.1:5005/login \
-H 'content-type: application/json' \
-d '{
      "username": "flaskeleton",
      "password": "flaskeleton",
      "is_admin": "true"
}'
```
Response should looks like this:
```bash
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiaXNfYWRtaW4iOnRydWUsImV4cCI6MTUyNDEyODQ1OX0.H4hXusyj2SpcuTOUkfOApVfs_sA88qJRlrOtL6BMO9g",
    "error": null
}
```
**Delete** item from todo list with a *DELETE* request (X-Access-Token should be updated with new one) and item's *id* passed as argument.
```bash
$ curl -X DELETE http://127.0.0.1:5005/todo-list?id=b716cdd1-31f0-49c0-82cd-0f01acb4af3a \
-H 'content-type: application/json' \
-H 'Cookie: X-Access-Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiaXNfYWRtaW4iOnRydWUsImV4cCI6MTUyNDEyODQ1OX0.H4hXusyj2SpcuTOUkfOApVfs_sA88qJRlrOtL6BMO9g'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "2ce6086a-5bba-45f9-ae9c-7a05166e9705",
            "what": "make my code clear"
        },
        {
            "id": "7a50909c-d811-4000-a723-a02a182b85d7",
            "what": "make my code concise"
        },
        {
            "id": "07b37bc2-9c51-4c5e-b1f8-cc22e9797e7b",
            "what": "make my code fast"
        }
    ],
    "error": null
}
```

### Authors
    Martin Tovmassian <martin.tovmassian@protonmail.com>
