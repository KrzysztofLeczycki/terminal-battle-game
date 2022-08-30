from soldier import Soldier
from party import Party, CPUParty
from setup import Setup
  

def run_game():
  print('Welcome to the Battle Game! \n')
  
  # Set the number of soldiers in each unit
  soldiers_num = int(input("Write a number of soldiers in unit (max 6): "))
  while soldiers_num not in range(1, 7):
    print("Write a number from 1 to 6")
    soldiers_num = int(input("Write a number of soldiers in unit (max 6): "))


  # Helper function witch reapets adding new soldier
  def create_unit(num, function):
    for i in range(num):
      print(i)
      function

  # Player 1 settings
  print('Party 1 settings!')
  party1_name = input("Write your party's name: ")
  party1 = Party(party1_name)
  #create_unit(soldiers_num, party1.create_soldier())
  for i in range(soldiers_num):
    party1.create_soldier()

  print("Party's 1 info:")
  print(f'{party1}\n')

  # Player 2 settings
  opponent = input("Choose your opponent: (h)uman, (c)omputer: ")
  while opponent not in ['h', 'c']:
    print("Write 'c' or 'h'")
    opponent = input("Choose your opponent: (h)uman, (c)omputer: ")

  print('Party 2 settings!')
  if opponent == 'h':
    party2_name = input("Write your party's name: ")
    party2 = Party(party2_name)
    create_unit(soldiers_num, party2.create_soldier())
    print("Party's 2 info:")
    print(f'{party2}\n')
    
  else:
    party2 = CPUParty()
    create_unit(soldiers_num, party2.create_cpu_soldier())
    print(f'{party2}\n')

  # new Setup instance - creating new board
  board = Setup(party1, party2)
  print(board)
  

run_game()