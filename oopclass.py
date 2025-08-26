# OOP
#1.Preciseness and clarity in code
#2.eusability through inheritance
#3.Encapsulation to protect data
#4.Polymorphism to use a single interface for different data types
#5.Abstraction to hide complex implementation details
#school management system
#three classes: Student, Teacher, Course
#objects: student1, student2, teacher1, course1
#methods: display_info, add_student
#attributes: name, age, student_id, subject, teacher_id, course_name, course_code
#relationships: A Course has one Teacher and multiple Students
#Example code:
class Student: 
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        return f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}"
class Teacher:
    def __init__(self, name, subject, teacher_id):
        self.name = name
        self.subject = subject
        self.teacher_id = teacher_id

    def display_info(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}, ID: {self.teacher_id}"
class Course:
    def __init__(self, course_name, course_code, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_info(self):
        student_names = ', '.join([student.name for student in self.students])
        return (f"Course Name: {self.course_name}, Code: {self.course_code}, "
                f"Teacher: {self.teacher.name}, Students: [{student_names}]")
    