from party import Party, CPUParty
from gameplay import Gameplay
  

## Main function
def run_game():
  print('\n***** Welcome to the Battle Game! ***** \n')
  
  # Set the number of soldiers in each unit
  soldiers_num = int(input("Write a number of soldiers in unit (max 6): "))
  # Protect against bad key choice
  while soldiers_num not in range(1, 7): 
    print("Write a number from 1 to 6")
    soldiers_num = int(input("Write a number of soldiers in unit (max 6): "))

  # Player 1 settings
  print('\nParty 1 settings!')
  party1_name = input("Write your party's name: ")
  # New Party class instance
  party1 = Party(party1_name)
  party1.create_unit(soldiers_num)

  # Player 2 settings
  # Choose live or cpu player
  opponent = input("Choose your opponent: (h)uman, (c)omputer: ")
  print('\n')
  # Protect against bad key choice
  while opponent not in ['h', 'c']:
    print("Write 'c' or 'h'")
    opponent = input("Choose your opponent: (h)uman, (c)omputer: ")

  print('Party 2 settings! \n')
  
  # Set human player
  if opponent == 'h':
    party2_name = input("Write your party's name: ")
    party2 = Party(party2_name)
    party2.create_unit(soldiers_num)

  #Set cpu player  
  else:
    party2 = CPUParty()
    party2.create_unit(soldiers_num)

  # New Gameplay instance - creating new board
  board = Gameplay(party1, party2)
  # In this list each soldier is placed according to his initiative
  board.set_initiative_list()

  # Main battle loop. Game ends, when one player has no soldiers in team.
  # It is possible to surrender and immediatly finish game (See gameplay.py). Note: Cpu player figths to its last soldier.
  while board.winner is None:
    # Function triggers displaying board and players actions
    board.run_turn()
    board.set_round()
    # Turns counter resets, when each soldier has done an action if he was alive
    board.set_turn(True)
    # Gameplay method is calleed again to remove dead soldiers from 'initiative list' before next rounds
    # Note: It is possible to eleminate soldier before his move, so initiative is important
    board.set_initiative_list()
  
  # Run game once again if you wish
  play_again = input('Do yo want to play again? (y): ')
  if play_again == 'y':
    run_game()

# Start game
run_game()
