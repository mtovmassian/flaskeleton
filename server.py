import os
import sys
from typing import Tuple
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import argparse
from api.middlewares.logger import Logger
from api.config.config import Config
from api.models import DB


def parse_args() -> Tuple[any]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--profile", type=str,
        help="Config profile dev|prod|test (default: dev)", default="dev"
    )
    parser.add_argument(
        "-d", "--db-init", action="store_true",
        help="Initialize database"
    )
    args = parser.parse_args()
    return (args.profile, args.db_init)

class Server:

    CONTEXT = {} # Use context to share singletons through your application

    def __init__(self, config_profile: str, db_init: bool):
        os.environ.setdefault("config_profile", config_profile)
        self.config: Config = Config(config_profile)
        self.db = DB(self.config.get_db_connection_string())
        if db_init: self.db.create_db()
        self.HOST: str = self.config.get_app_host()
        self.PORT: int = self.config.get_app_port()
        self.DEBUG_MODE: int = bool(self.config.get_app_debug_mode())
        self.CONTEXT["logger"] = Logger()
        self.CONTEXT["db"] = self.db

        self.app = Flask(__name__)
        CORS(self.app)
        api = Api(self.app)

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
    config_profile, db_init = parse_args()
    server = Server(config_profile, db_init)
    server.start()
