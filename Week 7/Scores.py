# Ang Hao Yi 10273989D

path = "C:\\Text Folders\\"
average_score = 0
name_highest = ""

with open(path+"scores.txt","r") as file: 
    firstline = file.readline()
    firstline_split = firstline.strip().split(",")

    print(f"{firstline_split[0]:<9}  {firstline_split[1]:<7}  {firstline_split[2]:6}  {firstline_split[3]:6}  {"Average":7}")

    for line in file:

        line_split = line.strip().split(",")
        average = (int(line_split[2])+int(line_split[3]))/2

        if average > average_score:
            average_score = average 
            name_highest = line_split[1]

        print(f"{line_split[0]:<9}  {line_split[1]:<7}  {line_split[2]:^6}  {line_split[3]:^6}  {average:>7.2f}")

print(f"{name_highest} has the highest average score of {average_score:.1f}")