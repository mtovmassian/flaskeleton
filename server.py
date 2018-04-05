import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import argparse
from app.config.config import Config
from app.dao.dao import Dao


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", type=str,
        help="Config profile DEV|PROD|TEST (default: DEV)", default="DEV"
    )
    args = parser.parse_args()
    config_profile = args.config
    return config_profile


class Server:

    def __init__(self, config_profile: str):
        self.config = Config(config_profile)
        self.HOST = self.config.get("server.host")
        self.PORT = int(self.config.get("server.port"))
        self.DEBUG_MODE = bool(int(self.config.get("server.debug_mode")))
        self.DAO = Dao(self.config)
        self.context = {
            "config": self.config,
            "dao": self.DAO
        }

    def start(self):
        app = Flask(__name__)
        CORS(app)
        api = Api(app)

        from app.resources.version import Version
        Version.set_context(self.context)
        api.add_resource(Version, "/version")

        #
        # from smartexchangetool.resources.semantic.sentence_similarity import SentenceSimilarity
        # api.add_resource(SentenceSimilarity, self.endpoint("/semantic/sentence-similarity"))

        app.run(
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
