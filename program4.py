basic_pay=float(input("Enter the basic pay"))
hra = basic_pay * 10/100
ta = basic_pay * 5/100
total_salary = basic_pay + hra + ta
print("basic pay :",basic_pay)
print("HRA:",hra)
print("TA :",ta)
print("Total :",total_salary)
