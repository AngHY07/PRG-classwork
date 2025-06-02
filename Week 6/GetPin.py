#Ang Hao Yi 10273989D

attempts = 3

while attempts > 0:
    pin = int(input("Enter pin: "))
    if pin == 12345:
        print("Correct pin entered.")
        break
    else : 
        attempts = attempts - 1
        if attempts > 0 :
            print("Invalid pin. Please try again.")
            print(f"You have {attempts} tries left.")
        else:
            print("Invalid pin. You have no more tries.")
            print("Your account is locked.")  
        continue

    