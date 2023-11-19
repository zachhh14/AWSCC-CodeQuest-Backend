import random 

computer_choices = ['rock', 'paper', 'scissor']
player_one_hand = input('Player1: ').lower()
computer_hand = random.choice(computer_choices)

def gameStart(hand_one, hand_two):
    if not hand_one or not hand_two:
        return 'invalid input'
    
    if player_one_hand == computer_hand:
        return 'its a tie'
    
    if (player_one_hand == 'rock' and computer_hand == 'scissor' ) or \
        (player_one_hand == 'scissor' and computer_hand == 'paper' ) or \
        (player_one_hand == 'paper' and computer_hand == 'rock' ):

        return 'Player1 Wins!'
    
    # if all the condition did not meet, the player 2 wins
    return 'Computer Wins!' 

print(f"computer: {computer_hand}") # printing what computer's hand
print(gameStart(player_one_hand, computer_hand))

    