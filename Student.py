class Student:

    # class varaibles
    class_year = 2025
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Spongebob", 23)
student2 = Student("Patrick", 20)
student3 = Student("Squid", 55)
student4 = Student("Sandy", 27)


print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

