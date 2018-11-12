from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from typing import List
from .user import User
from .user import UserRepository
from .todo import Todo
from .todo import TodoRepository


class DB:

    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        Session = sessionmaker(bind=self.engine)
        Session.configure(bind=self.engine)
        self.session: Session = Session()
        
        self.user = UserRepository(self.session)
        self.todo = TodoRepository(self.session)
    
    def create_table(self, table_class) -> None:
        table_class.__table__.create(self.engine)
    
    def drop_table_if_exists(self, table_name, table_class) -> None:
        if (self.engine.dialect.has_table(self.engine, table_name)):
            table_class.__table__.drop(self.engine)

    def create_db(self):
        self.drop_table_if_exists("users", User)
        self.create_table(User)
        self.drop_table_if_exists("todos", Todo)
        self.create_table(Todo)
        flaskeleton_user = User(
            username="flaskeleton",
            first_name="Flask",
            last_name="Eleton",
            password="3a9eb269c59de0d8e0a878acf5195a1ea1ac8bc97e8a3966a692b5328dd3b2c803141a234ff0fedbea0400fd9cd09416477f1fe14ea3b44df496dd841f9c0dbf",
            is_admin=False
        )
        admin_user = User(
            username="admin",
            first_name="Admin",
            last_name="Admin",
            password="c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec",
            is_admin=True
        )
        todo1 = Todo(what="clean my code")
        todo2 = Todo(what="test my code")
        self.session.add_all([flaskeleton_user, admin_user, todo1, todo2])
        self.session.commit()
        self.session.close()