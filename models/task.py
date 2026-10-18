class Task:
    _tasks = {}
    _next_id = 1000

    def __init__(self, task_id, title, assigned_to):
        self.title = title
        self.task_id = task_id
        self.assigned_to =assigned_to
        self.status = "pending" #all tasks start automatically as pending
        self.project_id = None

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
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if not isinstance(new_status, str):
            raise ValueError("Status must be a string.")
        new_status = new_status.lower().strip()

        if new_status not in ["pending", "completed"]:
            raise ValueError("Status must be pending or completed.")

        self._status = new_status

    def mark_complete(self):
        self.status = "completed"
    

    @classmethod
    def _generate_id(cls):
        while True:
            cls._next_id +=1
            task_id = f"TASK{cls._next_id}"

            if task_id not in cls._tasks:
                return task_id

    @classmethod
    def create(cls, title, assigned_to):
        task_id = cls._generate_id()

        task = cls(task_id, title, assigned_to)
        cls._tasks[task_id] = task

        return task
    
    @classmethod
    def get(cls, task_id):
        return cls._tasks.get(task_id)

    @classmethod
    def all(cls):
        return list(cls._tasks.values())

    def to_dict(self):
        return{
            "task_id": self.task_id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_id": self.project_id
        }
    @classmethod
    def from_dict(cls, data):
        task = cls(data["task_id"], data["title"], data["assigned_to"])
        task.status = data.get("status", "pending")
        task.project_id = data.get("project_id")
        cls._tasks[task.task_id] = task
        return task

    def __repr__(self):
        return (
            f"Task(task_id={self.task_id!r}, "
            f"title={self.title!r}, "
            f"status={self.status!r})"
        )
    
