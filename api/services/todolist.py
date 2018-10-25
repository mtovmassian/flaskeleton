import uuid
import os
from typing import List
from api.models import DB
from api.models import Todo

class TodoListService:
    
    TODO_LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), "todolist.txt")

    def __init__(self, db: DB):
        self.db = db
        if os.path.isfile(self.TODO_LIST_FILE_PATH) is not True:
            self.create_todo_list(["clean my code", "test my code"])

    def get_todo_list(self):
        todos = self.db.find_all_todos()
        return  [todo.dictify() for todo in todos]

    def create_todo_list(self, todos: List[str]) -> None:
        self.db.delete_all_todos()
        todo_list = [Todo(what=todo) for todo in todos]
        self.db.save_all(todo_list)

    def add_todos(self, todos: List[str]) -> None:
        todo_list = [Todo(what=todo) for todo in todos]
        self.db.save_all(todo_list)
    
    def delete_todo(self, todo_id: str) -> None:
        todo = self.db.find_todo_by_id(todo_id)
        self.db.delete_todo(todo)