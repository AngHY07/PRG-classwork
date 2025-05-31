#Ang Hao Yi 10273989D


numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]
odd = []

for char in numbers: 
    if ((char%2) != 0): 
        odd.append(char)
    else :
        continue 

odd.reverse()
for char in odd: 
    repeat_counter = 0
    for index in range(0,len(odd)):
        if char == odd[index]:
            repeat_counter += 1
        else:
            continue 
    
    if repeat_counter == 1: 
        continue
    else :
        odd.remove(char)

odd.reverse()

print(odd[0:5])


