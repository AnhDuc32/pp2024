from .init import Init

class Course(Init):
    def __init__(self, id, name, credit):
        super().__init__(id, name)
        self._credit = credit
    def __str__(self):
        return f'{super().__str__()} - Credit: {self._credit}'