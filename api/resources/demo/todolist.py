from flask import request
from flask_restful import Resource
import pickle
import uuid
from api.middlewares import auth
from api.middlewares import response as res


class TodoList(Resource):

    DB_PATH = "./api/resources/demo/todolist"

    @classmethod
    def set_context(cls, context):
        cls.logger = context["logger"]

    @classmethod
    def init_db(cls):
        cls.write_db([])

    @auth.login_required(request)
    def get(self):
        try:
            todo_list = self.read_db()
            args = request.args
            if args and "id" in args:
                todo_id = args["id"]
                data = {
                    "todo_list":
                        [todo for todo in todo_list if todo["id"] == todo_id]
                }
            else:
                data = {"todo_list": todo_list}
            return res.send_200(data=data)
        except Exception as error:
            self.logger.error(error)
            return res.send_500(error)

    @auth.login_required(request)
    def post(self):
        try:
            todo_list = self.read_db()
            new_todos = request.json
            for new_todo in new_todos:
                todo_list.append({"id": self.gen_uuid(), "what": new_todo})
            self.write_db(todo_list)
            return res.send_200(data={"todo_list": todo_list})
        except Exception as error:
            self.logger.error(error)
            return res.send_500(error)

    @auth.login_required(request)
    def put(self):
        try:
            todo_list = []
            self.write_db(todo_list)
            return res.send_200(data={"todo_list": todo_list})
        except Exception as error:
            self.logger.error(error)
            return res.send_500(error)

    @auth.login_required(request)
    def delete(self):
        try:
            todo_list = self.read_db()
            todo_id = request.args["id"]
            todo_list = [todo for todo in todo_list if todo["id"] != todo_id]
            self.write_db(todo_list)
            return res.send_200(data={"todo_list": todo_list})
        except Exception as error:
            self.logger.error(error)
            return res.send_500(error)

    @classmethod
    def gen_uuid(self):
        return str(uuid.uuid4())

    @classmethod
    def write_db(cls, data):
        with open(cls.DB_PATH, "wb") as todolist_file:
            pickle.dump(data, todolist_file)

    @classmethod
    def read_db(cls):
        with open(cls.DB_PATH, "rb") as todolistdb:
            return pickle.load(todolistdb)