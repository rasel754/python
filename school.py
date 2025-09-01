class Student :
    def __init__(self,name,cls,id):
        self.name=name
        self.cls=cls
        self.id=id
    
    def __repr__(self):
        return f"Student name {self.name} , class {self.cls} and id is : {self.id}"
    

class Teacher :
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id
    
    def __repr__(self):
        return f"Teacher name {self.name} , subject {self.subject} and id is : {self.id}"


class School:
    def __init__(self, name):
        self.name=name
        self.teachers=[]
        self.students=[]

    def add_teacher(self , name , subject):
        id=len(self.teachers)+101
        teacher=Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self , name , fee):
        if fee<6500:
            return "not enough money"
        else:
            id=len(self.students)+1
            student=Student(name,"c",id)
            self.students.append(student)
            return f'{name} is enrolled with id {id} , extra money {fee-6500}'


name=Student("rasel" , 5 , 1143)
teacher=Teacher("milon","css")
print(name)