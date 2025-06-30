
player = ['Hafu', 'Toast', 'Pokimane', 'Pewdiepie', 'Ninja', 'Markiplier'] 

results = [ [98, 107, 87, 121],
              [88, 111],
              [79, 130, 99],
              [86, 100, 121, 66, 98],
              [108, 79, 92],
              [77, 126, 93, 100, 73, 89],
            ]


win_list = []
game_list = []
total_list = []

for x in results:
    game_counter = 0
    win_counter = 0
    total = 0
    for y in x: 
        if y >= 100:
            win_counter += 1
        game_counter += 1
        total += y 
    win_list.append(win_counter)
    game_list.append(game_counter)
    total_list.append(total)




print("{:<10}  {:<5}{:<5} {:<5}".format("Player","Games"," Wins","Total"))

for x in range(len(player)):
    print("{:<10}  {:^5}{:^5} {:^5}".format(player[x],game_list[x],win_list[x],total_list[x]))