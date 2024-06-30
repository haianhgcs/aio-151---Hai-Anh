from .person import Person


class Doctor(Person):
    """
    Doctor class inherits from Person.
    """

    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        """
        Describe information of a Doctor object.
        """
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - specialist: {self._specialist}")
