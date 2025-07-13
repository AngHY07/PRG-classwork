prices = {'chicken' : 8.50,\
          'steak' : 13.80,\
          'fish' : 9.80,\
          'pasta' : 9.50,\
          'coffee' : 2.50,\
          'tea' : 1.80,\
          'water' : 0.50}

order_dict = {}

def user_interface(): 
    print('''-------------------
1. Add order
2. Summarize orders
3. Quit
-------------------''')

def first_letter_upper(x): 
        format_first_letter = ""
        word_list = list(x)
        temp_word = word_list[0].upper()
        word_list.pop(0)
        word_list.insert(0,temp_word)
        for letter in word_list: 
            format_first_letter += letter
        return format_first_letter


def menu(): 
    print("{:<8}   {}".format("Item","Price"))
    print("{:<8}   {}".format("----","-----"))
    for x in prices.keys():
        value = prices[x]

        print("{:<8}   ${:.2f}".format(first_letter_upper(x),value))

def summary(): 
    total = 0
    print("{:<8}   {}".format("Item","Quantity"))
    print("{:<8}   {}".format("----","--------"))
    for y in order_dict.keys(): 
        value = order_dict[y]
        print("{:<8}   {:}".format(first_letter_upper(y),value))
        cost = prices[y]*value
        total += cost
    print("Total cost = ${:.2f}".format(total))

exit = False 
while not(exit):
    user_interface()
    user_input = int(input('Your choice? '))

    if user_input == 3: 
        exit = True
        continue

    if user_input == 1: 
        menu()
        order_name = input("Your order? ").lower()

        if order_name in prices:
            sets = int(input("How many sets? "))
            order_dict[order_name] = sets
        else: 
            print("{} is not available.".format(order_name) )
            continue
    
    if user_input == 2: 
        summary()

