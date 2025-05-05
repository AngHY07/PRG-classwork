# Ang Hao Yi (10273989D)
friendlist =["Izzat","Bryan","Dalton","Ethan","Isaac"]

newname = str(input('What is the name of your new friend? '))
friendlist.append(newname)
print("My friends are now ",friendlist)

friendzone = str(input("Who do you want to be friendzoned? "))
position = friendlist.index(friendzone)
friendlist.remove(friendzone)

print('{} was in position {}. He will be friendzoned'.format(friendzone,position))
print("My eligible friends are now: ",friendlist)



