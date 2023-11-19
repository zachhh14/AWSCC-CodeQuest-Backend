limit = int(input('Limit: '))
counter = 1

def fizzBuzz(number):
    if not number:
        return None
    
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz!'
    
    if  number % 3 == 0:
        return 'Fizz'
    
    if  number % 5 == 0:
        return 'Buzz'
    
    return number

while (counter <= limit):
    print(fizzBuzz(counter))
    counter+=1
