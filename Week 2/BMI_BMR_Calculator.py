#Ang Hao Yi 10273989D

# BMI_BMR_Calculator.py
# This program calculates the body mass index and basal metabolic rate

# Calculate BMI
weight = float(input('Enter weight(kg): '))
height = float(input('Enter height(m): '))

bmi = weight / height**2 

print('BMI: ', bmi)

# Calculate BMR
age = float(input('Enter age(years): '))
gender = str(input('Are you male or female? '))

if gender == "male":
    bmr = 10*weight + 6.25 * height - 5 *age + 5
else :
    bmr = 10*weight + 6.25 * height -5 * age - 161


print('BMR: ', bmr)


