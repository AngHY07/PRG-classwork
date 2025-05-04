
Path = 'C:\\Text Folders\\'
messageinformation = open (Path+'message.txt','r')
messagecontent = messageinformation.read()

print(messagecontent)
print("The length of the message is {}".format(len(messagecontent)))
print("The number of words in the message is {}".format(len(messagecontent.split())))
