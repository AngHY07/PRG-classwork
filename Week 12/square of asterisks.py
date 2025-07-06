def asterisk_print(value):

    for row in range(value):
        for column in range(value):
            print("*",end=" ")
        print("")
    
number_side = int(input("Enter the number of asterisks: "))
asterisk_print(number_side)