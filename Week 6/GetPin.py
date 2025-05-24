#Ang Hao Yi 10273989D

attempts = 3

while attempts >= 0:
    pin = int(input("Enter pin: "))
    if pin == 12345:
        break
    else : 
        if attempts == 3 or attempts == 2 :
            print("Invalid pin. Please try again.")
            attempts = attempts - 1
            print(f"You have {attempts} tries left.")
        elif attempts == 1:
            attempts = attempts - 1
            break    
        continue

if attempts == 0: 
    print("Invalid pin. You have no more tries.")
    print("Your account is locked.")
else: 
    print("Correct pin entered.")
    