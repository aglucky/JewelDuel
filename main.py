from game import *
import itertools as it

#Checks for win in game
def win(game):
  if game.winCheck()==game.players.index(player)+1:
      game.win == True
      print(f'Congratulations {player}, you have won')
      return True
  return False

#Start of Game
print('Welcome to Jewel Duel, a strategic twist on the classic game Bejeweled')

p1 = input('\nPlayer 1 Name:')
p2 = input('\nPlayer 2 Name:')

#Initialize Game Board
game = game(p1,p2)
game.fillBlank()
while game.isMatch(3):
  game.gravDrag
  game.fillBlank()


while not game.win:
  for player in it.cycle(game.players):

    #Shows Board and prompt inputs
    game.show()
    print(f'Your move, {player}')
    gem1 = input('Select the first gem you would like swapped (ex: A2)\n')
    gem2 = input('Select the second gem you would like swapped (ex: B2)\n')
    
    #Ensures move is both valid and in correct format
    while not game.moveCheck(gem1,gem2):
      print('Move Invalid')
      gem1 = input('Please select valid move for gem1 (ex: A2)\n')
      gem2 = input('Please select valid move for gem2 (ex: B2)\n')

    #Converts input strings to coordinates
    y1 = ord(gem1[0])-65
    x1 = int(gem1[1])-1
    y2 = ord(gem2[0])-65
    x2 = int(gem2[1])-1

    #Swaps gems
    game.swap(x1,y1,x2,y2)
    # game.show()
    print('\n')
    
    #Win Check
    if win(game):
        break

    #Checks for 4 in a row
    while game.isMatch(4):
      if win(game):
        break
      game.addSpecialGem(player)
      game.gravDrag()
      game.fillBlank()
      # print('\n')
      # game.show()
      # print('\n')
    #Checks for three in a row
    
    while game.isMatch(3):
      if win(game):
        break
      game.gravDrag
      game.fillBlank()
      # print('\n')
      # game.show()
      # print('\n')