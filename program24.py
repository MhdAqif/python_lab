d1 = {}
d2 = {}
n1 = int(input("Enter number of items in first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d1[key] = value
n2 = int(input("Enter number of items in second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d2[key] = value
d1.update(d2)
print("Merged dictionary:", d1)
