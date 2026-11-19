from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def getdata(self):
        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))
        
    def area(self):
        print("Area of the rectangle:", self.length * self.breadth)

class Triangle(Polygon):
    def getdata(self):
        self.base = float(input("Enter base: "))
        self.height = float(input("Enter height: "))
        
    def area(self):
        print("Area of the triangle:", 0.5 * self.base * self.height)

r = Rectangle()
r.getdata()
r.area()

t = Triangle()
t.getdata()
t.area()

