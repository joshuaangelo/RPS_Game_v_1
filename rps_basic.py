# Rock Paper Scissors
print('...Rock...\n...Paper...\n...Scissors...')
player_a = input('Player A, your choice: ')
print('.\n.\n' *20)
player_b = input('Player B, your choice: ')


if (player_a == 'rock' and player_b == 'scissors') or (player_a == 'scissors' and player_b == 'paper') or player_a == 'paper' and player_b == 'rock':
      print("player a wins!")
elif (player_b == 'rock' and player_a == 'scissors') or player_b == 'scissors' and player_a == 'paper' or player_b == 'paper' and player_a == 'rock':
      print('player b wins!')
elif player_a == player_b:
      print('Tied')
else:
      print('invalid')
