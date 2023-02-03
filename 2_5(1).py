text = input('Enter phrase: ')
print("Word count: ", len(text.split()))

# Second option
phrase = text.strip()
print('Word count: ', phrase.count(' ') + 1)

# Third option
phrase = ' '.join(text.split())
print('Word count: ', phrase.count(' ') + 1)
