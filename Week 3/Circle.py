#Ang Hao Yi (10273989D)
import math 

a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))

def area(d,e):
    c = math.sqrt((d**2 + e**2))
    return math.pi*((c/2)**2)

print("The area of the circle is", area(a,b))