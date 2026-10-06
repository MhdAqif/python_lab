names=input("Enter first name seperated by space:").split()
count = 0
for name in names:
  count+=name.lower().count('a')
print("Numbers of occurence of 'a':",count)

