def yourResponse(choice):
    if not choice:
        return print('error input')
    if choice == 'yes':
        return input('Police arrived & Asked whether thief is inside (yes or no) ')
    if choice == 'no':
        return input('He Attacked on you. Will you knock him down (yes or no) ')
    
def determineEnding(choice):
    if not choice:
        return 'error input'
    if choice == 'yes':
        return 'WIN'
    if choice == 'no':
        return 'Game Over'


print('Narrator: One day, there is a strange guy who is asking for a shelter')
your_response = input('Can i seek for a shelter? (yes or no) ')
what_happen = yourResponse(your_response)
print(determineEnding(what_happen))





