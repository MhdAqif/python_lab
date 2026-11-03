def factorial(n):
  fact = 1
  for i in range(1,n+1):
    fact = fact * i
  return fact
  
n = int(input("Enter no of terms :"))
sum = 0
for i in range(1,n+1):
  sum = sum +(i**i)/factorial(i)
print("Sum of the series :",sum)  
