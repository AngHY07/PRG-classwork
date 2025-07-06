import random

def is_even(n):

    if (n % 2) == 0:
        print("{} is even".format(n))
    else: 
        print("{} is odd".format(n))


for x in range(5):

    value = random.randint(1,100)
    is_even(value)

