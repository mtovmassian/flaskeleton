import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from api.services.todolist import TodoListService

def test_create_todo_list_should_write_data_in_text_file():
    pass

def test_get_todo_list_should_return_list_of_items_or_empty_list():
    tl_service = TodoListService()
    todos = ["foo", "bar"]
    tl_service.create_todo_list(todos)
    assert len(tl_service.get_todo_list()) == 2