# Ang Hao Yi 10273989D
seeplayer = str(input("Does the guard see the player (y/n)? "))

if seeplayer == 'y':
    far = int(input("How far is the player? "))
    if far <= 1:
        print("The guard attacks!")
    elif far >= 2 and far <= 4:
        print("The guard advances.")
    elif far >= 5:
        print("The guard waits.")
else: 
    print("The guard waits.")


  