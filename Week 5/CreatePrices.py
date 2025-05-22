# Ang Hao Yi 10273989D

path = "C:\\Text Folders\\"
prices = [ ["kopi", 0.4], 
           ["teh", 0.4], 
           ["milo", 0.5], 
           ["soft drinks", 1.20] ]


with open(path+"prices.txt","w") as file:
    file.write(f'''{prices[0][0]}: ${prices[0][1]:.2f}
{prices[1][0]}: ${prices[1][1]:.2f}
{prices[2][0]}: ${prices[2][1]:.2f}
{prices[3][0]}: ${prices[3][1]:.2f}''')


