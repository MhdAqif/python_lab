n = int(input("Enter number:"))
temp = n
sum = 0
while temp>0:
 d = temp%10
 sum+=d**len(str(n))
 temp //=10
if sum == n:
 print("Armstrong")
else:
 print("Not Armstrong")
