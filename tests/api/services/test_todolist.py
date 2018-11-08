import sys
import os
from api.config.config import Config
from api.models import DB
from api.services.todolist import TodoListService

config = Config("test")
db = DB("{0}".format(config.get_db_connection_string()))

def test_get_todo_list_should_return_list_of_items_or_empty_list():
    tl_service = TodoListService(db)
    todos = ["foo", "bar"]
    tl_service.create_todo_list(todos)
    assert len(tl_service.get_todo_list()) == 2