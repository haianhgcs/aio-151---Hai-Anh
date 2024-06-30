from abc import ABC, abstractclassmethod


class Person(ABC):
    """
    Basic class for Student, Teacher và Doctor.
    """

    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractclassmethod
    def describe(self):
        """
        Describe basic information of a person object.
        """
        pass
