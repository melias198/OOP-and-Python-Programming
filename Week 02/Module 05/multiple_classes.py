class Student:
    def __init__(self,Name,Class,Id):
        self.Name = Name
        self.Class = Class
        self.ID = Id

    def __repr__(self) -> str:
        return f"Student Name is {self.Name},He Studied in Class {self.Class},His ID NO. is {self.ID}."


class Teacher:
    def __init__(self,Name,Department,Id):
        self.Name = Name
        self.Department = Department
        self.ID = Id

    def __repr__(self) -> str:
        return f"Teacher Name is {self.Name},He will Give a Lecture in {self.Department},His ID NO is {self.ID}."
    

class School:
    def __init__(self,Name):
        self.Name = Name
        self.Teachers = []
        self.Students = []
    
    def add_teacher(self,Name,Department):
        ID = len(self.Teachers) + 101
        teacher = Teacher(Name,Department,ID)
        self.Teachers.append(teacher)

    def enroll(self,Name,Class):
        ID = len(self.Students) + 1001
        student = Student(Name,Class,ID)
        self.Students.append(student)

    def __repr__(self) -> str:
        print("Welcome to Our",self.Name)
        print("<---Our Dedicated Teachers Panel--->")
        for teacher in self.Teachers:
            print(teacher)
        print("<---------------------------------->")
        print("<>---Our Beloved Students---<>")
        for student in self.Students:
            print(student)
        print("<>--------------------------<>")
        return "Thank You For Believing Us."
    
Amar_School = School("Amar_School")

Amar_School.add_teacher("Morshedur Rahman","Math")
Amar_School.add_teacher("Sahedur Rahman","Bangla")
Amar_School.add_teacher("Ruhul Kader","English")

Amar_School.enroll("Rahi","Nine")
Amar_School.enroll("Kafi","Nine")
Amar_School.enroll("Sahi","Nine")

print(Amar_School)


