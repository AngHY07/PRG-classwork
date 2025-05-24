#Ang Hao Yi 10273989D

path = "C:\\Text Folders\\"

with open(path+"temperature.txt","r") as file: 
    list_temp = file.readlines()
    list_temp_filtered =[]

    for char in list_temp:
        filter = char.strip().replace("\n","")
        list_temp_filtered.append(float(filter))
    

reading = len(list_temp_filtered)

count = 0
total = 0

print("The temperatures are ")
while count <= reading-1: 

    if list_temp_filtered[count] > 29:
        print(f"  {list_temp_filtered[count]} ** higher than 29!!!")
    else : 
        print(f'  {list_temp_filtered[count]}')
    
    total = total + list_temp_filtered[count]
    count = count + 1 
    
average = total/reading
print(f"\nNumber of readings: {reading}")
print(f"Average temperature: {average:.2f}")



    
