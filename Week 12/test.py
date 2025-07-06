def function1(i):

    if (i % 3 != 0):

        print(i, ' ')

    i -= 1

    while( i >= 1):

        if (i % 3 != 0):

            print(i, ' ')

        i -= 1

 

i = 0

while(i <= 4):

    function1(i)

    i += 1

print('i is', i)