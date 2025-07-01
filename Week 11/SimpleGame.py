
exit = False 

map = [ [' ', ' ', ' ', ' ', ' '],
        [' ', 'T', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
      		]

while not(exit):
    invalid = False

    for i in range(5):
        print("+",end="")
        for v in range(3):
            print("-",end="")
    print("+")

    for char in map:
        for i in range(len(char)):
            print("|",end="")
            print(" ",end="")
            print(char[i],end="")
            print(" ",end="") 
        print("|")

        for i in range(5):
            print("+",end="")
            for v in range(3):
                print("-",end="")
        print("+")

    steps = input("Enter your direction or Q to quit: ")

    if steps.upper() == "Q":
        exit = True 
        continue 
    
    if steps.upper() == "W" or steps.upper() == "S":
        if steps.upper() == "W":
            value_1 = 0
            value_2 = -1
            up_or_down = "up"
        elif steps.upper() == "S":
            value_1 = -1 
            value_2 = 1
            up_or_down = "down"
        
        while not(invalid): 
            for x in map[value_1]:  
                    if x == "T":
                        print(f"Sorry, you are not allowed to move {up_or_down}")
                        invalid = True
                        break
            if invalid == True:
                continue
            
            list_counter = 0 
            t_in_list = 0 
            letter = "T"
            for x in range(len(map)):
                if "T" in map[x]: 
                    list_counter = x
                    break 
            t_in_list = map[list_counter].index("T")
            map[list_counter].remove("T")
            map[list_counter].insert(t_in_list," ")
            map[list_counter + value_2].pop()
            map[list_counter + value_2].insert(t_in_list,"T")
            break
     
    invalid_2 = False
        
    if steps.upper() == "A" or steps.upper()=="D":       
        while not(invalid_2): 

            if steps.upper()=="A":
                value_1 = 0
                value_2 = -1
                left_or_right = "left"
            else:
                value_1 = -1
                value_2 = 1
                left_or_right = "right"

            for x in map:
                    if x[value_1] == "T":
                        print(f"You can't move to the {left_or_right}")
                        invalid_2 = True 
                        break 
            if invalid_2 == True:
                continue 
        
            list_counter = 0 
            t_in_list = 0 
            letter = "T"
            for x in range(len(map)):
                if "T" in map[x]: 
                    list_counter = x
                    break 
            
            t_in_list = map[list_counter].index("T")
            map[list_counter].remove("T")
            map[list_counter].insert(t_in_list+value_2 ,"T")
            break 

            



            
                





