import random

def play():
    user=input("What is your chiocie?'r' for rock 'p' for paper 's' for sissor")
    computer = random.choice({'r', 'p', 's'})

    if user == computer:
        return ' its a tie'

    if user_won (user, computer):
        return 'player won! '
    
    return 'player lost! '

def user_won(player,opponent):

    if (player =='r'  and opponent =='s'  or player == 's' and opponent == 'r' or player == 'r' and opponent =='s'):
        
        return True
    
