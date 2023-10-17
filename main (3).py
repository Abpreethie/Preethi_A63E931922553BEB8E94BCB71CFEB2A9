def sort_students(student_list):
    # Sort the list of student objects based on the 'cgpa' attribute in descending order
    student_list.sort(key=lambda x: x.cgpa, reverse=True)

# Define a Student class for creating student objects
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of student objects
students = [
    Student("Alice", "A001", 3.9),
    Student("Bob", "B002", 3.7),
    Student("Charlie", "C003", 4.0),
    Student("David", "D004", 3.5)
]

sort_students(students)

# Print the sorted list
for student in students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

