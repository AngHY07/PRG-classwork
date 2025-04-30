path = 'C:\\Text Folders\\'
studentdata = open(path+'StudentData.txt','r')
fileinfo1 = studentdata.readlines()
specificlines = fileinfo1[0::2]

print(specificlines)
