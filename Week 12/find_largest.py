

def largest_num(value):
    if value > large_list[0]:
        large_list[0] = value
        

first_int = int(input("Enter the first integer number: "))
large_list = [first_int]

second_int = int(input("Enter the second integer number: "))

third_int = int(input("Enter the third integer numeber: "))

forth_int = int(input("Enter the forth integer number: "))


largest_num(second_int)
largest_num(third_int)
largest_num(forth_int)

print("The largest integer is",large_list[0])