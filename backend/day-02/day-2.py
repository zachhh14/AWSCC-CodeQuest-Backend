numbers = ['first number', 'second number', 'third number']
sum = 0
for number in numbers:
    input_number = input(f"Enter the {number}: ")
    sum = sum + int(input_number)

print(f"\nSum: {sum}")
