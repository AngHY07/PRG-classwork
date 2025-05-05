#Ang Hao Yi (10273989D)
Path = 'C:\\Text Folders\\'
messageinformation = open (Path+'message.txt','r')
messagecontent = messageinformation.read()
messagesplit = messagecontent.split()
print(messagecontent)
print("The num of char of the message is {}".format(len(messagecontent)))
print("The number of words in the message is {}".format(len(messagecontent.split())))
print ('The number of times \'and\' appear in the message',messagecontent.count('and'))

print ("The first word is ",messagesplit[0])
print("Last word is",messagesplit[-1])

