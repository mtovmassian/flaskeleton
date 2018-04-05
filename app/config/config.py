import os
from configparser import ConfigParser


class Config:

    def __init__(self, profile):
        self.profile = profile
        self.config = ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.cfg')
        self.config.read(config_file)

    def get(self, parameter: str) -> str:
        return self.config.get(self.profile, parameter)
