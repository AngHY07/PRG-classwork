

def fah_to_cel(x):

    cel = (5.0/9.0) *(x-32)
    print(f"The temperature in celsius is {cel:.1f} degrees\n")

def cel_to_fah(x): 

    fah = (9.0/5.0)*x + 32
    print(f"The temperature in fahrenheit is {fah:.1f} degrees\n",)


exit = False

while not(exit): 
    
    input_value =int(input('''Temperature Conversion 
[1]Fahrenheit to Celsius
[2]Celsius to Fahrenheit 
[3]Exit
Please enter your option:'''))
    

    if input_value < 1 or input_value >3:
        print("Invalid option, please try again\n")
        continue

    if input_value == 3: 
        exit = True 
        print("Thank you")
        continue

    if input_value == 1:
        fahrenheit = float(input("Please enter the temperature in farenheit:"))
        fah_to_cel(fahrenheit)
        continue

    if input_value == 2: 
        celsius = float(input("Please enter the temperature in celsius:"))
        cel_to_fah(celsius)
        continue
    

