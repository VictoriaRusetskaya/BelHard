text = input('Enter phrase: ')
f_word = text.find(' ')
l_word = text.rfind(' ')
text_2 = text[l_word + 1:] + text[f_word: l_word + 1] + text[:f_word]
print(text_2)
