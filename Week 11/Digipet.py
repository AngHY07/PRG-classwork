menu = ['Feed','Play','Rest','Status']
status = [3,3,3]
title = ['hungry','happiness','energy']
msg = ['Nom nom nom','XD','Zzzzz']
value = [[0,1,2],[1,0,2],[2,1,0]]
choice = [1,2,3]

print("Digipet")
stop = False
while not(stop):

    user_input = int(input('''(1) Feed
(2) Play
(3) Rest 
(4) Status 
(5) Quit (Game Over)
Please select an option: '''))
    if user_input == 5: 
        stop = True 
        continue

    if user_input == 1 or user_input == 2 or user_input==3:
        for x in choice:
            if user_input == choice[x-1]:
                value_1 = value[x-1][0]
                value_2 = value[x-1][1]
                value_3 = value[x-1][2]

        if status[value_1] == 5:
            print(f"Your {title[value_1]} is at full bar")
        else: 
            status[value_1] += 1

        if status[value_2] == 0:
            print(f"Your {title[value_2]} is at 0")
        else: 
            status[value_2] -= 1
            
        if  status[value_3] == 0:
            print(f"Your {title[value_3]} is at 0")
        else: 
            status[value_3] -= 1
        
        print(msg[value_1])
    
    
    if user_input == 4:
 
        for x in range(3):
            print(f"{title[x]:10}",end="   ")
            dot = 5-status[x]
            for x in range(status[x]):
                print("*",end="")
            for x in range(dot):
                print(".",end="")
            print()
        








    


