
def obtain_grade(mark):

    if mark < 49.5:
        return "F"
    elif mark < 54.5:
        return "D"
    elif mark < 59.5:
        return "D+"
    elif mark < 64.5:
        return "C"
    elif mark < 69.5:
        return "C+"
    elif mark < 74.5:
        return "B"
    elif mark < 79.5:
        return "B+"
    elif mark < 84.5:
        return "A"
    else: 
        return 'A+'


mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]

print("{:<12}   {:<5}   {:<5}".format('Student Name',"Marks","Grade"))
for x in range(len(mark_list)): 
    print("{:<12}   {:<5}   {:<5}".format(mark_list[x][0],mark_list[x][1],obtain_grade(mark_list[x][1])))




