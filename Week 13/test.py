

try: 
    value = int(input("Enter a value: "))
    assert value < 25
    answer = 10/value
    print("Answer is:",answer)
except ZeroDivisionError: 
    print("Cannot be divided by 0")
except TypeError: 
    print("Your input type is wrong")
except AssertionError: 
    print("Value must be less than 25.")