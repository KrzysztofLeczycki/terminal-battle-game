from party import Party, CPUParty
from gameplay import Gameplay
  

## Main function
def run_game():
  print('\n***** Welcome to the Battle Game! ***** \n')
  
  # Set the number of soldiers in each unit
  soldiers_num_str = input("Write a number of soldiers in unit (max 6): ")
  # Protect against bad key choice
  while soldiers_num_str not in ['1', '2', '3', '4', '5', '6']: 
    print("Write a number from 1 to 6")
    soldiers_num_str = input("Write a number of soldiers in unit (max 6): ")
  soldiers_num = int(soldiers_num_str)

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

  # Main battle loop. The game ends, when one player has no soldiers in the team.
  # It is possible to surrender and immediately finish game (See gameplay.py). Note: Cpu player fights to its last soldier.
  while board.winner is None:
    # Function triggers displaying board and players actions
    board.run_turn()
    board.set_round()
    # Turns counter resets, when each soldier has done an action if he was alive
    board.set_turn(True)
    # Gameplay method is called again to remove dead soldiers from 'the initiative list' before the next rounds
    # Note: It is possible to eliminate a soldier before his move, so the initiative is important
    board.set_initiative_list()
  
  # Run game once again if you wish
  play_again = input('Do you want to play again? (y): ')
  if play_again == 'y':
    run_game()

# Start game
run_game()
