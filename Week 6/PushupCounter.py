#Ang Hao Yi 10273989D

target = int(input("Enter target number of pushups: "))
total = 0
counter = 1
while total < target:
    daily_num = int(input(f"Day{counter}: How many pushups did you do today? "))
    total += daily_num
    counter = counter + 1

print(f"You did a total of {total} pushups!")
print(f"You hit your terget in {counter-1} days!")