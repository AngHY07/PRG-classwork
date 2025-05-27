# Ang Hao Yi 10273989D

number = int(input("Please enter a number: "))

count = 1 

while count <= 10: 
    print(f"{number:>5} x {count:<3} = {number*count}")
    count = count + 1

print("The End")