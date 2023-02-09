try:
    n = int(input('Enter N: '))
    m = int(input('Enter M: '))
    k = int(input('Enter K: ')) + 1
except ValueError:
    print('You enter not a number!')
else:
    i = 0
    while i < n:
        if not(k % m):
            print(k)
            i += 1
        k += 1
