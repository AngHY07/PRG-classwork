#Ang Hao Yi 10273989D
map = [ [' ', 'T', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
      		]


for i in range(5):
    print("+",end="")
    for v in range(3):
        print("-",end="")
print("+")

for char in map:
    for i in range(len(char)):
        print("|",end="")
        print(" ",end="")
        print(char[i],end="")
        print(" ",end="") 
    print("|")

    for i in range(5):
        print("+",end="")
        for v in range(3):
            print("-",end="")
    print("+")


    
