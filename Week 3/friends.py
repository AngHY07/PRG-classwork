friendlist =["Izzat","Bryan","Dalton","Ethan","Isaac"]

newname = str(input('What is the name of your new friend? '))
print("My friends are now ",friendlist)
friendzone = str(input("Who do you want to be friendazoned? "))
position = friendlist.index(friendzone)

friendlist.remove(friendzone)
friendlist.append(newname)

print('{} was in position {}. He will be friendzoned'.format(friendzone,position))
print("My eligible friends are now: ",friendlist)



