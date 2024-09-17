import math

print("QUADRATIC EQUATION SOLVER")
print("---------------------------------")
print("general term : ax^2 + bx + c = 0")
a = float(input("enter the value of (a) : "))
b = float(input("enter the value of (b) : "))
c = float(input("enter the value of (c) : "))
x = (b**2 - 4*a*c)

if x >= 0:
    root1 = (-b + math.sqrt(x)) / (2*a)
    root2 = (-b - math.sqrt(x)) / (2*a)
    print(f"Root(s) of the equation: {root1}, {root2}")

else:
    print("the equation has no real root")

print("------------------------------")
print("thanks for using our service !!!")
print("this is programmed by : Aninda Sadhukhan")
