
# Ang Hao Yi 10273989D

path = "C:\\Text Folders\\"

with open(path+"Marks.txt","r") as file: 
    student_info = file.readlines()
    student_filtered = []

    for char in student_info: 
        filter = char.replace("\n","")
        student_filtered.append(filter.split(";"))

    count = 1
    position_count = 0
    total = 0
    print(f"{"Name":<10}    {"Mark"}")
    print(f"{"----":<10}    {"----"}")
    while count <= len(student_filtered):
        print(f"{student_filtered[position_count][0]:<10}    {int(student_filtered[position_count][1]):.1f}")
        total = total + int(student_filtered[position_count][1])
        position_count += 1
        count += 1


print(f"\nAverage Mark: {total/len(student_filtered):.2f}")