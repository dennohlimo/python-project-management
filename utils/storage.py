import json
from models.user import User
from models.project import Project
from models.task import Task

def save_data():
    data = {
        "users": {
            user_id: user.to_dict()
            for user_id, user in User._users.items()
        },
        "projects": {
            project_id: project.to_dict()
            for project_id, project in Project._projects.items()
        },
        "tasks": {
            task_id: task.to_dict()
            for task_id, task in Task._tasks.items()
        }
    }

    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

        print("Data saved successfully")


def load_data():
    try:
        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("No saved data found. Starting a new project.")
        return
    except json.JSONDecodeError:
       print("Saved data is damaged. Starting a new project.")
       return

    for user_id, user_data in data.get("users", {}).items():
        User.from_dict(user_data)

    for project_id, project_data in data.get("projects", {}).items():
        Project.from_dict(project_data)

    for task_id, task_data in data.get("tasks", {}).items():
        Task.from_dict(task_data)

    print("Data loaded successfully.")
