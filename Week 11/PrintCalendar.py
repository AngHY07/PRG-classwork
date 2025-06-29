
days = int(input("Enter number of days: "))
first_day = str(input("When is the first day of the week: "))

counter_days = 1
print(" {} {} {} {} {} {} {}".format('Sun',"Mon",'Tue','Wed','Thu','Fri','Sat'))
day_list = [["Sun",0,7,8],["Mon",4,6,7],["Tue",8,5,6],["Wed",12,4,5],["Thu",16,3,4],["Fri",20,2,3],["Sat",24,1,2]]

i = 0

while i < len(day_list):
     if first_day == day_list[i][0]:
          value = day_list[i][1]
          value_2 = day_list[i][2]
          value_3 = day_list[i][3]
          break
     else:
            i += 1


for z in range(value):
        print(" ",end="")
    
for y in range(1,value_2+1):
    for f in range(3):
        print(" ",end="")
    print(y, end="")

print()
    
for y in range(value_3,10):
        for f in range(3):
            print(" ",end="")
        print(y, end="")
        counter_days += 1
        if counter_days == 8:
            print()
            counter_days = 1

for y in range(10,days+1):
        for f in range(2):
            print(" ",end="")
        print(y, end="")
        counter_days += 1
        if counter_days == 8:
            print()
            counter_days = 1




    



