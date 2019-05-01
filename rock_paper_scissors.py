from random import choice
# If you get a "Not valid" Response be sure that you are using Lowercase 
 
rules = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
previous = ['rock', 'paper', 'scissors']
 
while True:
    player = input('\nRock, Paper or Scissors? : ')
    ai = rules[choice(previous)]  
 
    if player in ('quit', 'exit'): break
 
    elif player in rules:
        previous.append(player)
        print('the computer played', ai, end='; ')
 
        if rules[ai] == player:  
            print('Winner!')
        elif rules[player] == ai:  
            print('You Lose! :(')
        else: print("A Tie!")
 
    else: print("Not valid")
