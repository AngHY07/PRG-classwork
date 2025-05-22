#Ang Hao Yi 10273989D
filename =str(input("Please enter the filename: "))

path = "C:\\Text Folders\\"
with open(path+filename,'r') as file:
    words  = 0
    for line in file:
        line_split = line.split(" ")
        words = words + len(line_split)

print(f"Number of words in {filename}: {words}")

with open(path+"output.txt","w") as output: 
    output.write(f"There are {words:d} words in the document.")

print("Number of words successfully written to output.txt")

