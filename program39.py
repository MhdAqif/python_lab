def add(*args):
 """This is a function adds any number of integers arguments"""
 total = 0
 for i in args:
     total +=i
 return total
print("Sum =",add(10,20,30,40))
print("Documentation :",add.__doc__)
