options = {
    1 : 'Add item to the shopping list',
    2 : 'View shopping list',
    3 : 'Remove item from the shopping list',
    4 : 'Quit',
}
exit = False
cart = []

while not exit:
    print('Options:')
    for option in options.items():
        print(f"{option[0]}. {option[1]}")

    choice = input('Enter the number of you choice: ')
    match choice:
        case '1':
            item = input('Enter the item you want to add: ')
            cart.append(item)
            print(f'{item} has been added to your shopping list.')
        case '2':
            print('Your shopping list:')
            for cart_item in cart:
               print(cart_item)
        case '3':
            item_to_remove = input('Enter the item you want to remove: ')
            cart.remove(item_to_remove)
            print(f'{item_to_remove} has been removed from your shopping list.')
        case '4':
            exit = True
            print('Goodbye!')
        case __:
            print('Invalid input')

    print()

    