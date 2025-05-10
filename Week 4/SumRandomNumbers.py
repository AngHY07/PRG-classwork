# Ang Hao Yi 10273989D
import random

num1 = random.randint(0,100)
num2 = random.randint(0,100)

answer = int(input(f'Enter the sum of {num1} and {num2}: '))

if answer == num1+num2:
    print("Your answer is correct")
else: 
    print("Your answer is wrong")
    print("The correct answer is", num1+num2)