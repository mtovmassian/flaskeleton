from flask import request
from flask_restful import Resource
import os
import pickle
import uuid
from api.services.todolist import TodoListService
from api.middlewares import auth
from api.middlewares.rest_response import RESTResponse


class TodoList(Resource):

    def __init__(self, logger, db):
        self.logger = logger
        self.todo_list_service = TodoListService(db)

    @auth.login_required(request)
    def get(self):
        try:
            todo_list = self.todo_list_service.get_todo_list()
            return RESTResponse({"todo_list": todo_list}).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()

    @auth.login_required(request)
    def put(self):
        try:
            todos = request.get_json()
            self.todo_list_service.add_todos(todos)
            return RESTResponse({"todo_list": self.todo_list_service.get_todo_list()}).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()

    @auth.login_required(request)
    def post(self):
        try:
            todos = request.get_json()
            self.todo_list_service.create_todo_list(todos)
            return RESTResponse({"todo_list": self.todo_list_service.get_todo_list()}).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()

    @auth.admin_only(request)
    def delete(self):
        try:
            todo_id = request.args["id"]
            self.todo_list_service.delete_todo(todo_id)
            return RESTResponse({"todo_list": []}).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()
