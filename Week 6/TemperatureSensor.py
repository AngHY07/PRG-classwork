#Ang Hao Yi 10273989D

path = "C:\\Text Folders\\"

with open(path+"temperature.txt","r") as file: 
    data = file.read()
    data_split = data.split(',')
    count_data  = 0
    readings = len(data_split)
    filtered_data_string = []
    filter_data_float = []

    while count_data <= readings - 1: 
        filtered_data_string.append(data_split[count_data].strip())
        count_data += 1 

    count_float = 0
    while count_float <= readings - 1:
        filter_data_float.append(float(filtered_data_string[count_float]))
        count_float = count_float + 1

    print("The temperatures are ")
    total = 0 
    count_print = 0 
    while count_print <= readings - 1: 
        if filter_data_float[count_print] > 29: 
            print (f"   {filter_data_float[count_print]} **higher than 29!!")
            total += filter_data_float[count_print]
            count_print += 1

        else : 
            print (f"   {filter_data_float[count_print]}")
            total += filter_data_float[count_print]
            count_print += 1

        
    print("\nNumber of readings: {:d}".format(readings))
    print("Average temperature: {:.2f}".format(total/readings))




    



    
