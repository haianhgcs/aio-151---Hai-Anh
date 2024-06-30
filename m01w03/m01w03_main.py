import torch
import torch.nn as nn
from calc.softmax import Softmax
from calc.softmax_stable import SoftmaxStable
from people.student import Student
from people.teacher import Teacher
from people.doctor import Doctor
from ward import Ward
from container.stack import MyStack
from container.queue import MyQueue
from util.utilities import float_equals

print("1. Write class and implement `softmax` method.")
softmax = Softmax()
data = torch.Tensor([1, 2, 3])
output = softmax(data)

print(f"Input: {data}")
print(f"Output (Softmax): {output}")

softmax_stable = SoftmaxStable()
data = torch.tensor([1, 2, 3])
output = softmax_stable(data)

print(f"Input: {data}")
print(f"Output (Softmax): {output}")

print("2. Class ")
# Using defined classes
student1 = Student("studentA", 2010, "7")
teacher1 = Teacher("teacherA", 1969, "Math")
teacher2 = Teacher("teacherB", 1995, "History")
doctor1 = Doctor("doctorA", 1945, "Endocrinologists")
doctor2 = Doctor("doctorB", 1975, "Cardiologists")
ward1 = Ward("Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

# Print information off all people in Ward
student1.describe()
teacher1.describe()
doctor1.describe()
ward1.describe()

# Count number of Doctor in Ward
print(f"\nNumber of doctors : {ward1.count_doctor()}")

# Order people by age and reprint information
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers):{ward1.compute_average()}")

print("Using my Stack")
stack = MyStack(5)
stack.push(1)
stack.push(2)

print("Stack is full:", stack.is_full())

print("Top element:", stack.top())
print("Popped element:", stack.pop())
print("Top element after pop:", stack.top())
print("Popped element:", stack.pop())

print("Stack is full:", stack.is_full())
print("Stack is empty:", stack.is_empty())


print("Using my Queue")
queue = MyQueue(5)
queue.enqueue(1)
queue.enqueue(2)

print("Queue is full:", queue.is_full())

print("Front element:", queue.front())
print("Dequeued element:", queue.dequeue())
print("Front element after dequeue:", queue.front())
print("Dequeued element:", queue.dequeue())

print("Queue is full:", queue.is_full())
print("Queue is empty:", queue.is_empty())


print("Question #1: ")
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(), 2) == round(0.09, 2)
print(output)

print("Question #2: ")
softmax = Softmax()
data = torch.Tensor([5, 2, 4])
output = softmax(data)
assert round(output[-1].item(), 2) == round(0.26,2)
print(output)


print("Question #3: ")
softmax = Softmax()
data = torch.Tensor([1, 2, 300000000])
output = softmax(data)
assert round(output[0].item(), 2) == round(0.00,2)
print(output)

print("Question #4: ")
softmax_stable = SoftmaxStable()
data = torch.tensor([1, 2, 3])
output = softmax_stable(data)
assert round(output[-1].item(), 2) == round(0.67,2)
print(output)

print("Question #5: ")
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1._yob == 2011
student1.describe()

print("Question #6: ")
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1._yob == 1991
teacher1.describe()

print("Question #7: ")
doctor1 = Doctor(name="doctorZ2023", yob=1981,  specialist="Endocrinologists")
assert doctor1._yob == 1981
doctor1.describe()

print("Question #8: ")
student1 = Student("studentA", 2010, "7")
teacher1 = Teacher("teacherA", 1969, "Math")
teacher2 = Teacher("teacherB", 1995, "History")
doctor1 = Doctor("doctorA", 1945, "Endocrinologists")
doctor2 = Doctor("doctorB", 1975, "Cardiologists")
ward1 = Ward("Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
assert ward1.count_doctor() == 1
ward1.add_person(doctor2)
print(ward1.count_doctor())

print("Question #9: ")
stack = MyStack(5)
stack.push(1)
assert stack.is_full() == False
stack.push(2)
print(stack.is_full())

print("Question #10: ")
stack = MyStack(5)
stack.push(1)
assert stack.is_full() == False
stack.push(2)
print(stack.top())

print("Question #11: ")
queue = MyQueue(5)
queue.enqueue(1)
assert queue.is_full() == False
queue.enqueue(2)
print(queue.is_full())

print("Question #12: ")
queue = MyQueue(5)
queue.enqueue(1)
assert queue.is_full() == False
queue.enqueue(2)
print(queue.front())
