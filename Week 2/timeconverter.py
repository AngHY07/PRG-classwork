#Ang Hao Yi 10273989D


time =int(input('Enter time in seconds '))
hour = time // 3600
min = (time%3600)//60
sec =  (time%3600)%60

print("Time:",hour,"hr",min,"min",sec,"sec")


