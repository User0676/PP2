class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

        def print_na():
            print(self.name,self.age)
        
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self,name,age)

x = Student("Ali",19)
x.print_na()