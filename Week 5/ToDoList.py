# Ang Hao Yi (10273989D)

path = "C:\\Text Folders\\"

with open(path + "todolist.txt","r") as file:
    for line in file:
        print(line.strip())