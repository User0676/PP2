class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self,x,y):
        self.x = x
        self.y = y

    def dist(self,x,y):
        print("on x:", self.x - x)
        print("on y:", self.y - y)


Cord = Point(5,10)

Cord.show()
Cord.move(2,4)
Cord.show()
Cord.dist(10,10)

