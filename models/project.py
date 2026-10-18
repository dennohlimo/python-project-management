from datetime import datetime

class Project:
    _projects = {}
    _next_id = 1000


    def __init__(self, project_id,title,description,due_date):
        self.project_id = project_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_id = None
        self.task_ids = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise ValueError("Title must be a string")
        if new_title.strip() == "":
            raise ValueError("Title cannot be empty")
        self._title = new_title.strip()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        if not isinstance(new_description, str):
            raise ValueError("Description must be a string")
        if new_description.strip() == "":
            raise ValueError("Description cannot be empty")
        self._description =new_description.strip()

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, new_due_date):
        if not isinstance(new_due_date, str):
            raise ValueError("Due date must be a string.")
        new_due_date = new_due_date.strip()
        try:
            datetime.strptime(new_due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Please use YYYY-MM-DD format")

        self._due_date = new_due_date.strip()
    @classmethod
    def _generate_id(cls):
        while True:
            cls._next_id += 1
            project_id = f"PROJ{cls._next_id}"

            if project_id not in cls._projects:
                return project_id

    @classmethod
    def create(cls, title, description, due_date):
        project_id = cls._generate_id()
        project = cls(project_id, title, description, due_date)
        cls._projects[project_id] = project

        return project

    @classmethod
    def get(cls, project_id):
        return cls._projects.get(project_id)

    @classmethod
    def all(cls):
        return list(cls._projects.values())
    
    def add_task(self, task):
        if task.project_id not in (None, self.project_id):
            raise ValueError("This task already belongs to another project.")
        if task.task_id not in self.task_ids:
            self.task_ids.append(task.task_id)

        task.project_id = self.project_id
        

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_id": self.user_id,
            "task_ids": list(self.task_ids)
        }
    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["project_id"],
            data["title"],
            data["description"],
            data["due_date"],
        )
        project.user_id = data.get("user_id")
        project.task_ids = list(data.get("task_ids", []))
        cls._projects[project.project_id] = project
        return project

    def __repr__(self):
        return (
            f"Project(project_id={self.project_id!r}, "
            f"title={self.title!r})"
        )

        
    