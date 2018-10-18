import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import argparse
from api.config.config import Config
from api.dao.dao import Dao


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

    def __init__(self, config_profile: str):
        self.config: Config = Config(config_profile)
        self.HOST: str = self.config.get_app_host()
        self.PORT: int = self.config.get_app_port()
        self.DEBUG_MODE: int = bool(self.config.get_app_debug_mode())
        self.app = Flask(__name__)
        CORS(self.app)
        api = Api(self.app)

        CONTEXT = {
            # Use context to share singletons through your application
            "config": self.config,
            "dao": Dao(self.config),
            "logger": self.app.logger
        }

        from api.resources.version import Version
        Version.set_context(CONTEXT)
        api.add_resource(Version, "/version")

        from api.resources.login import Login
        Login.set_context(CONTEXT)
        api.add_resource(Login, "/login")

        from api.resources.demo.todolist import TodoList
        TodoList.set_context(CONTEXT)
        TodoList.init_db()
        api.add_resource(TodoList, "/demo/todo-list")

    def start(self):
        self.app.run(
            host=self.HOST,
            port=self.PORT,
            debug=self.DEBUG_MODE,
            threaded=True
        )


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    config_profile = parse_args()
    server = Server(config_profile)
    server.start()
