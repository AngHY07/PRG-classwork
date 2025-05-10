#Ang Hao Yi 10273989D
marks = float(input("Please enter your marks: "))

if marks < 50:
    print("Grade: F")
    print("See me.")
elif marks < 55:
    print("Grade: D")
elif marks < 60:
    print("Grade: D+")
elif marks <65:
    print("Grade: C")
elif marks < 70:
    print("Grade: C+")
elif marks < 75:
    print("Grade: B")
elif marks < 80:
    print("Grade: B+")
elif marks < 85:
    print("Grade: A")
    print("Well done.")
elif marks >= 85:
    print("Grade: A+")
    print("Excellent!")
