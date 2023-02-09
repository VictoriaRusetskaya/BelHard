# try:
#     n = int(input('Enter N: '))
# except ValueError:
#     print('You enter not a number!')
# else:
#     num = 2
#     line = []
#     while num <= n:
#         while len(line) < 5:
#             if not(num % 2):
#                 line.append(num)
#             num += 2
#         print(line)
#         line = []

n = int(input('Enter N: '))
count = 0
for num in range(2, n+1, 2):
    count += 1
    if count % 5:
        print(num, end=' ')
    else:
        print(num)
