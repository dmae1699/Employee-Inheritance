class Person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print("My name is", self.name, "and my id number is", self.id_number)
        print("My salary is", self.salary,"and my post is",self.post)
class Employee(Person):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,id_number)
e=Employee("Avleen",1234,150000,"doctor")
e.display()
