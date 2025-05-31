#Ang Hao Yi 10273989D


days = int(input("Enter number of days: "))
count_days = 0
print("Day | Task(s)")

while count_days < days:
    
    count_week = 1 
    for index in range(1,days+1):
        if count_week < 8:
            print(f'{index:>3} |')
            count_week += 1
            count_days += 1
        else: 
            print("Day | Task(s)")
            print(f'{index:>3} |')
            count_week = 2
            count_days += 1
            continue
        




        
