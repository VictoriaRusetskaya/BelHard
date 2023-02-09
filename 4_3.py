try:
    n = int(input('Enter N: '))
except ValueError:
    print('You enter not a number!')
else:
    num = 2
    line = []
    while num <= n:
        while len(line) < 5:
            if not(num % 2):
                line.append(num)
            num += 1
        print(line)
        line = []
