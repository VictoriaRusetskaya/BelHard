text = input('Enter text: ')
count_repeats = {text[i]: text.count(text[i]) for i in range(len(text))}
print(count_repeats)
