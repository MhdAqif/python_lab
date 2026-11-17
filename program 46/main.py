import armstrong

lower=int(input("Enter the lower limit :"))
upper=int(input("Enter the upper limit :"))
print("Armstrong number b/w",lower,"and",upper,"are :")
for num in range(lower,upper+1):
  if armstrong.is_armstrong(num):
    print(num,end=" ")
