first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = input('Enter your age: ')

# First option
print('Hello! My name is %s %s. I am %s years old.' % (first_name, last_name, age))

# Second option
print('Hello! My name is {} {}. I am {} years old.'.format(first_name, last_name, age))

# Third option
print(f'Hello! My name is {first_name} {last_name}. I am {age} years old.')
