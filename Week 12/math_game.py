
import random

correct_list = ["Very good!","Excellent!","Nice work!","Keep up the good work!"]

incorrect_list = ["No. Please try again.","Wrong. Try once more.","Don’t give up!","No. Keep trying."]

def menu(): 
    print('''\n[1] Addition
[2] Subtraction 
[3] Multiplication 
[4] Division
[5] Random 
[6] Quite program''')
    
def print_incorrect_msg(): 

    value = random.randint(0,3)
    print(incorrect_list[value])

def print_correct_msg(): 
    
    value = random.randint(0,3)
    print(correct_list[value])


def addition():

    a = random.randint(1,10)
    b = random.randint(2,10)
    correct = a + b 
    answer_status = False
    
    while not(answer_status): 
        answer = float(input("How much is {} + {}? ".format(a,b)))
        if answer == correct: 
            print_correct_msg()
            answer_status = True 
            continue
        else: 
            print_incorrect_msg()

def subtraction():

    a = random.randint(1,10)
    b = random.randint(2,10)
    correct = a - b 
    answer_status = False 
    
    while not(answer_status):
        answer = float(input("How much is {} - {}? ".format(a,b)))
        if answer == correct: 
            print_correct_msg()
            answer_status = True 
            continue
        else: 
            print_incorrect_msg()

def multiplication(): 
    
    a = random.randint(1,10)
    b = random.randint(2,10)
    correct = a * b
    answer_status = False 
    
    while not(answer_status):

        answer = float(input("How much is {} x {}? ".format(a,b)))
        if answer == correct: 
            print_correct_msg()
            answer_status = True 
            continue
        else: 
            print_incorrect_msg()

def division(): 
    
    a = random.randint(1,10)
    b = random.randint(2,10)
    correct = round(a/b,2)
    answer_status = False 
    
    while not(answer_status):

        answer = float(input("How much is {} / {} (Round to nearest 2.d.p)? ".format(a,b)))
        if answer == correct: 
            print_correct_msg()
            answer_status = True
            continue 
        else: 
            print_incorrect_msg()

def input_choice(x):

    if x ==1: 
        addition()
    elif x==2: 
        subtraction()
    elif x ==3: 
        multiplication()
    elif x ==4: 
        division()

stop = False
while not(stop):
    
    menu()
    user_input = int(input("Please enter your choice: "))

    if user_input == 6: 
        stop = True 
        continue
    elif user_input ==5: 
        input_choice(random.randint(1,4))
    else: 
        input_choice(user_input)
