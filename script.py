from party import Party, CPUParty
from setup import Setup
  

# Helper function
def create_unit(num, party):
  if party.is_cpu == False:
    for i in range(num):
      print(f"\nCreate soldier number {i + 1}")
      party.create_soldier()

  else:
    for i in range(num):
      party.create_cpu_soldier()
    
  party.back_in_range()
  print(f"\n{party.name} info:")
  print(f'{party}\n')



# Main function
def run_game():
  print('\n***** Welcome to the Battle Game! ***** \n')
  
  # Set the number of soldiers in each unit
  soldiers_num = int(input("Write a number of soldiers in unit (max 6): "))
  while soldiers_num not in range(1, 7):
    print("Write a number from 1 to 6")
    soldiers_num = int(input("Write a number of soldiers in unit (max 6): "))


  # Player 1 settings
  print('\nParty 1 settings!')
  party1_name = input("Write your party's name: ")
  party1 = Party(party1_name)
  party1.create_unit(soldiers_num)

  # Player 2 settings
  opponent = input("Choose your opponent: (h)uman, (c)omputer: ")
  print('\n')
  while opponent not in ['h', 'c']:
    print("Write 'c' or 'h'")
    opponent = input("Choose your opponent: (h)uman, (c)omputer: ")

  print('Party 2 settings! \n')
  
  if opponent == 'h':
    party2_name = input("Write your party's name: ")
    party2 = Party(party2_name)
    party2.create_unit(soldiers_num)
    
  else:
    party2 = CPUParty()
    party2.create_unit(soldiers_num)

  # new Setup instance - creating new board
  board = Setup(party1, party2)
  board.set_initiative_list()

  while board.winner is None:
    board.run_turn()
    board.set_round()
    board.set_turn(True)
    board.set_initiative_list()
  
  play_again = input('Do yo want to play again? (y): ')
  if play_again == 'y':
    run_game()


run_game()
