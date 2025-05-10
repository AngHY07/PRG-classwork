#Ang Hao Yi 10273989D

import re
password = input("Kindly enter your password: ")

digit = re.search(r"\d",password)
upper_case = re.search(r"[A-Z]",password)
lower_case = re.search(r"[a-z]",password)

if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif digit == None:
    print("Password must contain at least one digit.")
elif upper_case == None:
    print("Password must contain at least one uppercase letter.")
elif lower_case == None:
    print("Password must contain at least one lower case letter.")
else:
    print("Password is valid.")



