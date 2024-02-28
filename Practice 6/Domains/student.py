from .init import Init
import numpy

class Student(Init):
    def __init__(self, id, name, dob): 
        super().__init__(id, name)
        self._dob = dob
        self._mark = numpy.array([])
        self._gpa = None
    def __str__(self):
        return f'{super().__str__()} - DoB: {self._dob}'.rstrip()