#Ang Hao Yi 10273989D

path = "C:\\Text Folders\\"
with open(path+"prices.txt",'a') as file:
    file.write('\n{}: ${}'.format("teh peng", "1.20"))
    file.write('\n{}: ${}'.format("milo peng", "1.40"))