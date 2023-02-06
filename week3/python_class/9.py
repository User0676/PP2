class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(avs):
        print(avs.name)

p1=person("Ali",19)
print(p1.age)

p1.age=20
print(p1.age)