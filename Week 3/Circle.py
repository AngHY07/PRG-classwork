import math 

a = float(input("enter the value of a, "))
b = float(input("enter the value of b, "))

def area(d,e):
    c = math.sqrt((d**2 + e**2))
    return math.pi*((c/2)**2)

print("The area of the circle is ", area(a,b))