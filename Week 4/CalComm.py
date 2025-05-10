#Ang Hao Yi 10273989D
sales = float(input("Enter monthly sales of sales agent: "))

if sales >= 10000: 
    print("Commission rate is : 10%")
    print(f"Comimission paid is : ${sales*0.1:.2f}")
else : 
    print("Comission rate is : 5%")
    print(f"Comission paid is : ${sales*0.05:.2f}")

