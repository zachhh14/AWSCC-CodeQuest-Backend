input_number = int(input('Enter a number: '))


def evaluateNumber(number):
    if not number:
        return 'That number is a Zero!'
    
    if number < 0:
        return f'{number} is a Negative number!'
    
    if number > 0:
        return f'{number} is a Positive number!'

print(evaluateNumber(input_number))