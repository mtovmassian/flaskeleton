import pickle

db = None

with open("./api/resources/demo/todolistdb", 'rb') as todolistdb:
    db = pickle.load(todolistdb)

print(db)
