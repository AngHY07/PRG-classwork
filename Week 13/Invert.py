
path = "C:\\Text Folders\\"

with open(path + "colors.csv.txt","r") as file: 

    info = file.readlines()
    colors_dict = {}
    new_colors = {}
    for char in info: 

        cleaned_info = char.strip().split(",")
        colors_dict[cleaned_info[0]] = cleaned_info[1]

    for value in colors_dict.values(): 
       new_colors[value] = list()

    for key in colors_dict.keys():

        values = colors_dict[key]
        new_colors[values].append(key)
    
    print(new_colors)


    
         


        

        