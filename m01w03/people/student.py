from .person import Person


class Student(Person):
    """
    Student class inherits from Person.
    """

    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        """
        Describe information of a Student object.
        """
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - grade: {self._grade}")
