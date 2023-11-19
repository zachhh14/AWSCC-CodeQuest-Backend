player_one_hand = input('Player1: ').upper()
player_two_hand = input('Player2: ').upper()

def gameStart(hand_one, hand_two):
    if not hand_one or not hand_two:
        return 'invalid input'
    
    if player_one_hand == player_two_hand:
        return 'its a tie'
    
    if (player_one_hand == 'ROCK' and player_two_hand == 'SCISSOR' ) or \
        (player_one_hand == 'SCISSOR' and player_two_hand == 'PAPER' ) or \
        (player_one_hand == 'PAPER' and player_two_hand == 'ROCK' ):

        return 'Player1 Wins!'
    
    return 'Player2 Wins!' # if all the condition did not meet, the player 2 wins

print(gameStart(player_one_hand, player_two_hand))

    