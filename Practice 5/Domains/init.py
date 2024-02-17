class Init():
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def __str__(self):
        return f'ID: {self._id} - Name: {self._name}'