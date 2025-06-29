#Ang Hao Yi 10273989D

character = input("Enter a character: ")
number = int(input("Enter a number: "))



value = number*2
for i in range(1,number+1):
    for l in range(number-i):
        print(" ",end="")  
    for y in range(i):
        print(character,end=" ")
    print()

print("Merry Christmas!")

    
