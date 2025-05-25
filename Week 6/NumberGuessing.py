# Ang Hao Yi 10273989D
import random

randomvalue = random.randint(0,100)

attempts = 1 
print("Welcome to Number Guessing Game")
while attempts <= 5 : 
    guess_num = int(input(f"Try {attempts}: Enter a number between 1 and 100 (or -1 to end): "))

    if guess_num is -1:
        break
    elif guess_num == randomvalue:
        print("Bingo, you've got it right!")
        break
    elif guess_num < randomvalue:
        print(f"{guess_num} is too low")
        attempts = attempts + 1
        continue
    elif guess_num > randomvalue: 
        print(f"{guess_num} is too high")
        attempts = attempts + 1
        continue

print("Bye-bye!")
