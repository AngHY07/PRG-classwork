def asterisk_print(x,y):

    for row in range(x):
        for column in range(x):
            print(char,end=" ")
        print("")

side = int(input("Enter the number of side: "))
char = input("Enter the char: ")
asterisk_print(side,char)