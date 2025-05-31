
numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]

foundnums = []
count = 0
for num in numbers:
    print(num)
    if num in foundnums:

        numbers.remove(num)
    elif count >= 5:
        break
    elif not num % 2 == 0:
        foundnums.append(num)
        count += 1

print(foundnums)

