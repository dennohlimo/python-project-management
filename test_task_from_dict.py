
from models.task import Task

task_data = {
    "task_id": "TASK1001",
    "title": "Create homepage",
    "status": "completed",
    "assigned_to": "USR1001",
    "project_id": "PROJ1001"
}

task = Task.from_dict(task_data)

print(task)
print(task.to_dict())
print(Task.get("TASK1001"))
