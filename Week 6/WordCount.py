# Ang Hao Yi 10273989D
num_enter = 5
wordlist=[]
num_letters =0
while num_enter > 0:
    
    word = str(input("Enter word (x to exit): "))

    if word == 'x':
        break 

    flag = False
    for char in wordlist:
        if word == char:
            flag = True
        else :
            continue
    
    if flag == True: 
        print(f"{word} has already been entered.")
        continue
    else : 
        wordlist.append(word)
        num_enter = num_enter -1
        num_letters = len(word) + num_letters


print(f"Your words are {wordlist}")
print(f"The number of letters in these words is {num_letters}")