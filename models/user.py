
import re

from models.person import Person


class User(Person):
    _users = {}
    _next_id = 1000

    def __init__(self, user_id, name, email):
        super().__init__(name)
        self.user_id = user_id
        self.email = email
        self.project_ids = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not isinstance(new_email, str):
            raise TypeError("Email must be a string.")

        new_email = new_email.strip()

        if not re.fullmatch(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}", new_email):
            raise ValueError("Please enter a valid email.")
        self._email = new_email

    @classmethod
    def _generate_id(cls):
        while True:
            cls._next_id += 1
            user_id = f"USR{cls._next_id}"

            if user_id not in cls._users:
                return user_id

    @classmethod
    def create(cls, name, email):
        user_id = cls._generate_id()
        user = cls(user_id, name, email)
        cls._users[user_id] = user
        return user

    @classmethod
    def get(cls, user_id):
        return cls._users.get(user_id)

    @classmethod
    def all(cls):
        return list(cls._users.values())

    def add_project(self, project):
        if project.user_id not in (None, self.user_id):
            raise ValueError("This project already belongs to another user.")

        if project.project_id not in self.project_ids:
            self.project_ids.append(project.project_id)

        project.user_id = self.user_id
        
    

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "project_ids": list(self.project_ids)
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["user_id"], data["name"], data["email"])
        user.project_ids = list(data.get("project_ids", []))
        cls._users[user.user_id] = user
        return user
    
    def __repr__(self):
        return (
            f"User(user_id={self.user_id!r}, "
            f"name={self.name!r}, email={self.email!r})"
        )
