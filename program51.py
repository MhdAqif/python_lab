class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


l1 = float(input("Enter length of Rectangle 1: "))
b1 = float(input("Enter breadth of Rectangle 1: "))

l2 = float(input("Enter length of Rectangle 2: "))
b2 = float(input("Enter breadth of Rectangle 2: "))

r1 = Rectangle(l1, b1)
r2 = Rectangle(l2, b2)

print("\nArea of Rectangle 1:", r1.area())
print("Perimeter of Rectangle 1:", r1.perimeter())
print("Area of Rectangle 2:", r2.area())
print("Perimeter of Rectangle 2:", r2.perimeter())

if r1.area() > r2.area():
    print("Rectangle 1 has a greater area.")
elif r1.area() < r2.area():
    print("Rectangle 2 has a larger area.")
else:
    print("Both rectangles have equal area.")

