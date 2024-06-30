from people.doctor import Doctor
from people.teacher import Teacher


class Ward:
    """
    Ward class.
    """

    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        """
        Add a person into people list of Ward.
        """
        self.people.append(person)

    def describe(self):
        """
        Print Ward name and information of all people in Ward.
        """
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        """
        Count number of Doctor in Ward.
        """
        return sum(isinstance(person, Doctor) for person in self.people)

    def sort_age(self):
        """
        Order people in Ward by age of people (ascending).
        """
        self.people.sort(key=lambda person: person.get_yob(), reverse=True)

    def compute_average(self):
        """
        Calculate average age of birth of all Teachers in Ward.
        """
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return None
        return sum(teacher.get_yob() for teacher in teachers) / len(teachers)
