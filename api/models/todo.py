from typing import List
from sqlalchemy import Column, Integer, String, Boolean
from api.models import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    what = Column(String(255))

    def dictify(self):
        return {"id": self.id, "what": self.what}

    def __repr__(self):
        return "<Todo(id={0}, what={1}>".format(
            self.id, self.what
        )

class TodoRepository:

    def __init__(self, session):
        self.session = session

    def find_by_id(self, todo_id: str) -> Todo:
        return self.session.query(Todo).filter(Todo.id == todo_id).one()
    
    def find_all(self) -> List[Todo]:
        return self.session.query(Todo)

    def save(self, todo: Todo):
        self.session.add(todo)
        self.session.commit()
    
    def save_all(self, todos: List[Todo]):
        self.session.add_all(todos)
        self.session.commit()
    
    def delete(self, todo: Todo):
        self.session.delete(todo)
        self.session.commit()

    def delete_all(self) -> None:
        return self.session.query(Todo).delete()