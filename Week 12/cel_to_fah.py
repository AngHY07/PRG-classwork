
temp_degree = int(input("Enter the temperature in degree Celcius: "))


def temp_fah(value):

    f = (value*9/5)+32
    return f 

print("The temperature is equivalent to {:.1f} Fahrenheit.".format(temp_fah(temp_degree)))