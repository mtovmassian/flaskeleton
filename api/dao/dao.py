from api.config.config import Config
"""
    IMPLEMENT YOUR OWN DATA ACCESS OBJECTS HERE
"""


class Dao:

    def __init__(self, config: Config):
        self.db_host: str = config.get_db_host()
        self.db_port: int = config.get_db_port()
        self.db_name = config.get_db_name()
