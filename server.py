import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import argparse
from api.middlewares.logger import Logger
from api.config.config import Config
from api.models import DB


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", type=str,
        help="Config profile dev|prod|test (default: dev)", default="dev"
    )
    args = parser.parse_args()
    config_profile = args.config
    return config_profile

class Server:

    CONTEXT = {} # Use context to share singletons through your application

    def __init__(self, config_profile: str):
        os.environ.setdefault("config_profile", config_profile)
        self.config: Config = Config(config_profile)
        self.db = DB("sqlite:///{0}".format(self.config.get_db_name()))
        self.HOST: str = self.config.get_app_host()
        self.PORT: int = self.config.get_app_port()
        self.DEBUG_MODE: int = bool(self.config.get_app_debug_mode())
        self.app = Flask(__name__)
        CORS(self.app)
        api = Api(self.app)
        self.CONTEXT["logger"] = Logger()
        self.CONTEXT["db"] = self.db

        from api.resources.version import Version
        api.add_resource(Version, "/version", resource_class_kwargs=self.CONTEXT)

        from api.resources.login import Login
        api.add_resource(Login, "/login", resource_class_kwargs=self.CONTEXT)

        from api.resources.todolist import TodoList
        api.add_resource(TodoList, "/demo/todo-list", resource_class_kwargs=self.CONTEXT)

    def start(self):
        self.app.run(
            host=self.HOST,
            port=self.PORT,
            debug=self.DEBUG_MODE,
            threaded=True
        )


if __name__ == '__main__':
    config_profile = parse_args()
    server = Server(config_profile)
    server.start()
