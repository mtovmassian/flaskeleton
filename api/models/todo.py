from sqlalchemy import Column, Integer, String, Boolean
from api.models import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    what = Column(String)

    def dictify(self):
        return {"id": self.id, "what": self.what}

    def __repr__(self):
        return "<Todo(id={0}, what={1}>".format(
            self.id, self.what
        )