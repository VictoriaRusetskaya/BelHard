try:
    num1 = int(input('Enter first number: '))
    action = input('Enter action: ')
    num2 = int(input('Enter second number: '))
except ValueError:
    print('You enter not a number!')
else:
    match action:
        case '+':
            print('Result: ', num1 + num2)
        case '-':
            print('Result: ', num1 - num2)
        case '*':
            print('Result: ', num1 * num2)
        case '/':
            print('Result: ', num1 / num2)
        case _:
            print('Unknown action!')
