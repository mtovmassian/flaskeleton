import uuid
import os
from typing import List

class TodoListService:
    
    TODO_LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), "todolist.txt")

    def __init__(self):
        if os.path.isfile(self.TODO_LIST_FILE_PATH) is not True:
            self.create_todo_list(["clean my code", "test my code"])

    def get_todo_list(self):
        lines = self.read_todo_list().split("\n")
        if len(lines) == 1 and lines[0] == '':
            return []
        else:
            return [{"id": line.split(",")[0], "what": line.split(",")[1]} for line in lines]

    def create_todo_list(self, todos: List[str]) -> None:
        todo_list = "\n".join(["{0},{1}".format(self.gen_uuid(), todo) for todo in todos])
        self.write_todo_list(todo_list)

    def add_todos(self, todos: List[str]) -> None:
        todos = "\n".join(["{0},{1}".format(self.gen_uuid(), todo) for todo in todos])
        todo_list = self.read_todo_list()
        todo_list_updated = todo_list + "\n" + todos
        self.write_todo_list(todo_list_updated)
    
    def delete_todo(self, todo_id: str) -> None:
        todo_list = self.read_todo_list()
        todo_list_updated = "\n".join([line for line in todo_list.split("\n") if line.split(",")[0] != todo_id])
        self.write_todo_list(todo_list_updated)

    @classmethod
    def gen_uuid(self) -> str:
        return str(uuid.uuid4())

    @classmethod
    def write_todo_list(cls, data: str) -> None:
        with open(cls.TODO_LIST_FILE_PATH, "w") as todolist_file:
            todolist_file.write(data)

    @classmethod
    def read_todo_list(cls) -> None:
        with open(cls.TODO_LIST_FILE_PATH, "r") as todolistdb:
            return todolistdb.read()