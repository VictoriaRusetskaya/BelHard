count = int(input('Enter number: '))
data = {i: {'name': input('Enter name: '), 'email': input('Enter email: ')} for i in range(count)}
print(data)
