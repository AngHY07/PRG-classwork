#Ang Hao Yi 10273989D

path = "C:\\Text Folders\\"

with open(path+"cars.txt",'r') as carfile:
    carinfo = carfile.readlines()
    carinfo_filtered =[]
    for char in carinfo:
        filter = char.replace("\n","")
        carinfo_filtered.append(filter)
    carinfo_filtered.remove("Fesla Corp")
    carinfo_filtered.remove("***Price List***")
    print(f"1. {carinfo_filtered[0]}")
    print(f"2. {carinfo_filtered[1]}")
    print(f"3. {carinfo_filtered[2]}")
    print(f"4. {carinfo_filtered[3]}\n")

    car_list = []
    price_list = []

    for char in carinfo_filtered:
        char_split = char.split(":")
        car_list.append(char_split[0])
        price_list.append(char_split[1])

    order_number = str(input("Enter the order number: "))
    customer_name = str(input("Customer Name: "))
    carchoice = int(input("Enter car choice: "))

with open(path+order_number+".txt","w") as output: 
    output.write(f"{customer_name} ordered the {car_list[carchoice-1]} at the price of {price_list[carchoice-1]}")

print("Car has been successfully ordered.")




    