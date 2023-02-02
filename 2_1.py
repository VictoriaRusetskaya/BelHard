# First option
text = input('Enter your phrase: ')
print(text.replace(' ', '-'))

# Second option
words = text.split(' ')
print('-'.join(words))
