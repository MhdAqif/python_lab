list1= list(map(int,input("Enter first list:").split()))
list2= list(map(int,input("Enter second list:").split()))
print("Same length",len(list1)==len(list2))
print("Same sum",sum(list1)==sum(list2))
if set(list1) and set(list2):
 print("Common values exists")
else:
 print("No common value")

