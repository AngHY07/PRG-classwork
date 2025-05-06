#Ang Hao Yi 10273989D
path = "C:\\Text Folders\\"
studentdata = open(path+"StudentData.txt",'r')
studentinfo = studentdata.readlines()
firstline = studentinfo[0]
secondline = studentinfo[1]
filterfirstline = firstline.replace('\n','')
split1 = filterfirstline.split(',')
filtersecondline = secondline.replace('\n','')
split2 = filtersecondline.split(',')


print('{:<10s}     {:<14s}'.format("Name","Mobile Contact"))
print('{:<10s}     {:<14s}'.format(split1[0],split1[1]))
print('{:<10s}     {:<14s}'.format(split2[0],split2[1]))

studentdata.close()