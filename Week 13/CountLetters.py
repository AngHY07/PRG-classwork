import string

sentence = input("Enter a sentence: ")

filtered_sentence = sentence.strip(string.punctuation).replace(" ","").lower()
letter_dict = {}

for x in filtered_sentence: 
    letter_dict[x] = 0

for y in filtered_sentence: 
    letter_dict[y] += 1

for key in letter_dict.keys(): 
    value = letter_dict[key]
    print("{} : {}".format(key,value))