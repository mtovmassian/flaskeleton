from flask import request
from flask_restful import Resource
import os
import pickle
import uuid
from api.services.todolist import TodoListService
from api.middlewares import auth
from api.middlewares.rest_response import RESTResponse


class TodoList(Resource):

    tl_service = TodoListService()

    @classmethod
    def set_context(cls, context):
        cls.logger = context["logger"]

    @auth.login_required(request)
    def get(self):
        try:
            todo_list = self.tl_service.get_todo_list()
            args = request.args
            if args and "id" in args:
                todo_id = args["id"]
                data = {
                    "todo_list":
                        [todo for todo in todo_list if todo["id"] == todo_id]
                }
            else:
                data = {"todo_list": todo_list}
            return RESTResponse(data).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()

    @auth.login_required(request)
    def put(self):
        try:
            todos = request.get_json()
            self.tl_service.add_todos(todos)
            return RESTResponse({"todo_list":  self.tl_service.get_todo_list()}).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()

    @auth.login_required(request)
    def post(self):
        try:
            todos = request.get_json()
            self.tl_service.create_todo_list(todos)
            return RESTResponse({"todo_list": self.tl_service.get_todo_list()}).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()

    @auth.admin_only(request)
    def delete(self):
        try:
            todo_id = request.args["id"]
            self.tl_service.delete_todo(todo_id)
            return RESTResponse({"todo_list": ""}).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()
