def fibonnaci(n):
  if n<=1:
    return n 
  return fibonnaci(n-1)+fibonnaci(n-2)
terms = int(input("How many terms"))
for i in range(terms):
  print(fibonnaci(i),end="")
