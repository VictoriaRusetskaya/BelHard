# string_numbers = input('Enter three numbers: ')
# negative_count = string_numbers.count('-')
# print('Number of negative: ', negative_count, '\nNumber of positive: ', (3 - negative_count))

negative_count = (int(input('Enter first number: ')) < 0) + \
                 (int(input('Enter second number: ')) < 0) + \
                 (int(input('Enter third number: ')) < 0)
print('Number of negative: ', negative_count, '\nNumber of positive: ', (3 - negative_count))
