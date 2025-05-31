#Ang Hao Yi 10273989D

flag = False
odd=[]
even= []
total = 0
while not(flag): 

    number = int(input("Please enter a number (0 to end): "))

    if number == 0: 
        flag = True
        continue 

    if (number % 2) == 0:
        even.append(number)
        total += number
    else: 
        odd.append(number) 
        total += number

odd.sort()
even.sort()

print(f"Odd numbers: {odd}")
print(f"Even numbers: {even}")
print(f"Average = {total/(len(odd)+len(even)):.2f}")

