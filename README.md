# Flaskeleton: Flask-RESTful starter kit
 Flaskeleton is a starter kit for [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) applications. It provides code structure and basic authentication system based on [Json Web Token](https://jwt.io/).

<img src="https://fr.tintin.com/images/tintin/persos/rascar/C1232C3.jpg" alt="Drawing" style="width:100%;"/>

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

You will find a configuration file under `flaskeleton/api/config/conf.cfg`. Three profiles are stored:
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

### Authors
    Martin Tovmassian <martin.tovmassian@protonmail.com>
