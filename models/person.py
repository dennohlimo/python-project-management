class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name (self):
        return self._name

    @name.setter
    def name(self,new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string ")
        self._name = new_name.strip()