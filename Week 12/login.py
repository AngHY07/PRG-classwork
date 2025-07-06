account_list = []
def read_accounts(accounts): 

        for x in range(len(info)): 

            info_filtered = info[x].strip().split(',')
            account_list.append(list())
            account_list[x].append(info_filtered[0])
            account_list[x].append(info_filtered[1])
    
def login(user_name,password): 
    
    for x in range(len(account_list)): 
        if user_name == account_list[x][0]:
            if password == account_list[x][1]: 
                print("Hello {}, you may proceed...".format(user_name.upper()))
                return True
            else: 
                print("Login incorrect. Please try again...")
                return False
     
    print("Login incorrect. Please try again...")
    return False
    


print("Please login to your account before proceeding....")  
path = "C:\\Text Folders\\"

with open(path+ "accounts.txt","r") as file: 

    info = file.readlines()
    read_accounts(info)

    attempt_counter = 1 
    exit = False

    while not(exit): 
         
        if attempt_counter >3: 
              exit = True 
              print("You didnt get it in 3 attempts. Your account is locked.")
              continue     
        
        name =input("Please enter your username: ")
        pwd = input("Please enter your password: ")
        exit = login(name,pwd)
        attempt_counter += 1
        
        

          


