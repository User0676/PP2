class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Default area of a shape is 0")


class Rectangle(Shape):   
    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        print(self.length*self.width)

sh = Shape(10,5)
rec = Rectangle(10,5)
sh.area()
rec.area()

