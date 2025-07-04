

path = "C:\\Text Folders\\"

file = input("Please enter the name of the data file: ")
total = 0
with open(path+file,"r") as info: 
    title = info.readline()
    date_total = []
    information = info.readlines()
    
    for y in range(len(information)):
        data = information[y].strip().split(",")
        date_total.append(list())
        date_total[y].append(data[0])
        
        for x in range(1,len(data)):
            total += int(data[x])
        date_total[y].append(total)
        total = 0
    
    print(title.strip())
    print(f"{"Month":<9}       {"Sales":<5}")
    for x in range(len(date_total)):
        print("{:<9}       {:>5d}".format(date_total[x][0],date_total[x][1]))

    
    




    
