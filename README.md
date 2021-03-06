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

You will find a configuration file under `api/config/config.yml`. Three profiles are stored:
  - *dev*: local environment
  - *prod*: production environment integrated with Docker
  - *test*: test environment

### Database

By default *dev* and *test* environment rely on a [MySQL](https://www.mysql.com/fr/downloads/) database but it is possible to use an other DMBS. If so you will need to change accordingly the connection string in the configuration file.

### Launch server
Run this command into the `flaskeleton` directory:
```bash
$ pipenv run python server.py --profile <config profile> --db-init
```
Or use this pipenv alias to directly launch the server in development mode:
```bash
$ pipenv run start
```

### Launch tests
```bash
$ pipenv run tests
```

### Todo list demo
To get familiar with how a Flask-RESTful application works you can run the *todo list* demo and investigate the code under `api/resources/todolist.py`.

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
    "version": "1.0.0",
    "status_code": 200
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
    "status_code": 200
}
```
Now you have an access token and can you use it in the next *todo list* requests.

#### ● POST `/demo/todo-list`
**Create** a prefilled todo list with a *POST* request:
```bash
$ curl -X POST http://127.0.0.1:5005/demo/todo-list \
-H 'content-type: application/json' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDQwMzk5fQ.4uEdaR6qUIg-76NcS2q40xXUJH3Plzl4fKwvRb5HEf8' \
-d '["make my code correct", "make my code clear"]'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "1",
            "what": "make my code correct"
        },
        {
            "id": "2",
            "what": "make my code clear"
        }
    ],
    "status_code": 200
}
```

#### ● GET `/demo/todo-list`
**Read** todo list items with a *GET* request:
```bash
$ curl -X GET http://127.0.0.1:5005/demo/todo-list \
-H 'content-type: application/json' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDQwMzk5fQ.4uEdaR6qUIg-76NcS2q40xXUJH3Plzl4fKwvRb5HEf8'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "1",
            "what": "make my code correct"
        },
        {
            "id": "2",
            "what": "make my code clear"
        }
    ],
    "status_code": 200
}
```

#### ● PUT `/demo/todo-list`
**Update** todo list with new items with a *PUT* request:
```bash
$ curl -X PUT http://127.0.0.1:5005/demo/todo-list \
-H 'content-type: application/json' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiZXhwIjoxNTIzNDQwMzk5fQ.4uEdaR6qUIg-76NcS2q40xXUJH3Plzl4fKwvRb5HEf8' \
-d '["make my code concise", "make my code fast"]'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "1",
            "what": "make my code correct"
        },
        {
            "id": "2",
            "what": "make my code clear"
        },
        {
            "id": "3",
            "what": "make my code concise"
        },
        {
            "id": "4",
            "what": "make my code fast"
        }
    ],
    "status_code": 200
}
```

#### ● DELETE `/demo/todo-list` (need administrator privillege)
To illustrate privillege management this operation require an administrator role. The token you used previously is no more valid since the way you authenticated yourself did not give you enough privillege. To do so get an administrator access token by posting this infos to the login resource:
```bash
$ curl -X POST http://127.0.0.1:5005/login \
-H 'content-type: application/json' \
-d '{
      "username": "admin",
      "password": "admin",
}'
```
Response should looks like this:
```bash
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiaXNfYWRtaW4iOnRydWUsImV4cCI6MTUyNDEyODQ1OX0.H4hXusyj2SpcuTOUkfOApVfs_sA88qJRlrOtL6BMO9g",
    "status_code": 200
}
```
**Delete** item from todo list with a *DELETE* request (Authorization header should be updated with new token) and item's *id* passed as argument.
```bash
$ curl -X DELETE http://127.0.0.1:5005/demo/todo-list?id=1 \
-H 'content-type: application/json' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZsYXNrZWxldG9uIiwiZmlyc3RuYW1lIjoiZmxhc2tlbGV0b24iLCJsYXN0bmFtZSI6ImZsYXNrZWxldG9uIiwiaXNfYWRtaW4iOnRydWUsImV4cCI6MTUyNDEyODQ1OX0.H4hXusyj2SpcuTOUkfOApVfs_sA88qJRlrOtL6BMO9g'
```
Response should looks like this:
```bash
{
    "todo_list": [
        {
            "id": "2",
            "what": "make my code clear"
        },
        {
            "id": "3",
            "what": "make my code concise"
        },
        {
            "id": "4",
            "what": "make my code fast"
        }
    ],
    "status_code": 200
}
```

### Authors
    Martin Tovmassian <martin.tovmassian@protonmail.com>
