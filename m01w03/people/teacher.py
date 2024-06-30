from .person import Person


class Teacher(Person):
    """
    Teacher class inherits from Person.
    """

    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        """
        Describe information of a Teacher object.
        """
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - subject: {self._subject}")
