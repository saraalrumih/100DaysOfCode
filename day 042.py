# classes 2
class Student:
    def __init__(self, id, name, level):
        self.id=id
        self.name=name
        self.level=level

    def get_student_info(self):
        print(self.name," is a student with id: ",self.id," in "," level.")

student1=Student(11111,"Sara","9")
student2=Student(22221,"Asma","3")

student1.get_student_info()
student2.get_student_info()

# change object property
student1.name="Noura"
student1.get_student_info()

# delete object property
del student1.id

# delete object
del student1
