# app.py

from models import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        try:
            self.tasks[index].mark_completed()
        except IndexError:
            raise ValueError("Invalid task index")

    def remove_task(self, index):
        try:
            del self.tasks[index]
        except IndexError:
            raise ValueError("Invalid task index")
