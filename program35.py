def simple_interest(principle,time,rate):
  return principle*rate*time/100

age_group = input("Senior citizen ? (yes/no) ").lower()
rate = 12 if age_group=="yes" else 10
p = float(input("Principle :"))
t = float(input("Time (year)s"))
print("Simple interest",simple_interest(p,t,rate))

