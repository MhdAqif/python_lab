import graphics.rectangle
import graphics.circle

print("Rectangle")
print("Area :",graphics.rectangle.area(10,5))
print("Perimeter :",graphics.rectangle.perimeter(10,5))

print("\nCircle")
print("Area :",graphics.circle.area(7))
print("Perimeter :",graphics.circle.perimeter(7))

from graphics.threeD_graphics.cuboid import area,perimeter

print("\nCuboid")
print("Surface area :",area(5,4,3))
print("Total Edge length :",perimeter(5,4,3))

from graphics.threeD_graphics.sphere import *
print("\nSphere")
print("Surface Area :",area(7))
print("Circumference :",perimeter(7))


