from .lecturer import Lecturer

class Session:
    def __init__(self, title, lecturer_id, id = None):
        self.id = id
        self.title = title
        self.lecturer_id = lecturer_id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) and len(value) == 0:
            raise ValueError(
                "Title must be a non-empty string"
            )
        self._title = value

    @property
    def lecturer_id(self):
        return self._lecturer_id
    
    @lecturer_id.setter
    def lecturer_id(self, value):
        if type(value) is int and Lecturer:
            pass