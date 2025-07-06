def asterisk_print(x,y):

    for row in range(x):
        for column in range(y):
            print("*",end=" ")
        print("")

side = int(input("Enter the number of side: "))
char = int(input("Enter the number of char: "))
asterisk_print(side,char)