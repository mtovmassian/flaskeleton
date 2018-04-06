"""
    IMPLEMENT YOUR OWN DATA ACCESS OBJECTS HERE
"""


class Dao:

    def __init__(self, config):
        self.db_host = config.get("db.host")
        self.db_port = int(config.get("db.port"))
        self.db_name = config.get("db.name")
