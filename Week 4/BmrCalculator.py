#Ang Hao Yi 10273989D
path = "C:\\Text Folders\\data.txt"

datafile = open(path,'r')
bmi_info = datafile.readline()
infosplit = bmi_info.split(',')

weight = float(infosplit[0])
height = float(infosplit[1])
gender = infosplit[2]
age = int(infosplit[3])

if gender == 'male':
    bmr = 10*weight + 6.25*(height*100)-5 *age+5
else:
    bmr = 10*weight+6.25*(height*100)-5* age-161

print(f'''
Weight: {weight}kg
Height: {height:.1f}m
Age: {age}
Gender: {gender}
BMR: {bmr:.1f} kcal/day

''')

datafile.close()
