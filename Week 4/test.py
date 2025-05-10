
gender = input("Kindly enter your gender")
age = int(input("Kindly enter your age"))


if (gender == "Female" and age < 18) or (gender != "Female" and age > 18):
    print('You are either a female or older than 18 but not both')
else :
    print("You are either a male  younger than 18 or a female older than 18")
