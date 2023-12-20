from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv
from todo import *

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

db_con_string = f"mongodb+srv://jonuonga:{password}@to-do.jvpeeac.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_con_string)


# database creation
todoDatabase = client.todo_db

# collection creation
todo_collection = todoDatabase.tasks



# inserting a task details into a document
def insert_task(task_t, task_d):
    task_document = {
        "task": task_t,
        "date": task_d
    }

    todo_collection.insert_one(task_document)


def remove_task():
    sorted_tasks = todo_collection.find().sort("_id", -1)
    latest_task = sorted_tasks[0]

    todo_collection.delete_one({"_id": latest_task["_id"]})
    





# adding some data (document)

#task_data = {
#    "task": "Linear",
#    "date": "2/25/24"
#}

#task = todo_collection.insert_one(task_data)
#print(task.inserted_id)