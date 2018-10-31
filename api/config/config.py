import os
import yaml
from typing import Dict

class Config:

    def __init__(self, profile):
        self.profile = profile
        config_file_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        with open(config_file_path, 'r') as config_file:
            self.config = yaml.load(config_file)

    def get_app(self) -> Dict[str, any]:
        return self.config[self.profile]["app"]
    
    def get_app_name(self) -> str:
        return self.get_app()["name"]
    
    def get_app_version(self) -> str:
        return self.get_app()["version"]
    
    def get_app_host(self) -> str:
        return self.get_app()["host"]

    def get_app_port(self) -> int:
        return self.get_app()["port"]

    def get_app_debug_mode(self) -> int:
        return self.get_app()["debug_mode"]

    def get_db(self) -> Dict[str, any]:
        return self.config[self.profile]["db"]
    
    def get_db_name(self) -> str:
        return self.get_db()["name"]

    def get_db_host(self) -> str:
        return self.get_db()["host"]

    def get_db_port(self) -> int:
        return self.get_db()["port"]

    def get_db_connection_string(self) -> str:
        return self.get_db()["connection_string"]