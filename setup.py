from random import randrange
class Setup:
  def __init__(self, party1, party2):
    self.player_1 = party1
    self.player_2 = party2
    self.initiative_list = []
    self.round_num = 1
    self.winner = None
  

  def __repr__(self):
    return f'{self.player_1} fought against {self.player_2}. The winner is {self.winner}.'


  def set_initiative_list(self):
    soldiers_list = []
    soldiers_list += self.player_1.front_line + self.player_1.back_line + self.player_2.front_line + self.player_2.back_line
    print(soldiers_list)
    
    def quick_sort(list, start, end):
      if start >= end:
        return
      
      pivot_idx = randrange(start, end + 1)
      pivot_element = list[pivot_idx]
      list[end], list[pivot_idx] = list[pivot_idx], list[end]
     
      less_than_pointer = start
      for i in range(start, end):
        if list[i].initiative > pivot_element.initiative:
          list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
          less_than_pointer += 1

      list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
     
      quick_sort(list, start, less_than_pointer - 1)
      quick_sort(list, less_than_pointer + 1, end)

    quick_sort(soldiers_list, 0, len(soldiers_list)-1)
    self.initiative_list = soldiers_list
 

  def choose_soldier(self, input):
    idx = int(input) - 1
    return self.initiative_list[idx]


  def show_board(self):
    self.set_initiative_list()
    character_string = list(map(lambda soldier: f'{self.initiative_list.index(soldier) + 1}: {soldier.party} - {soldier.name}', self.initiative_list))
    inititive_string = ' * '.join(character_string)
    
    def joining_fun(arr):
      representation = list(map(lambda soldier: f'{soldier.name} - {soldier.specialization} {soldier.health}/10 HP', arr))
      return ' | '.join(representation)
    
    print(
      f'''
      xxxxx Round {self.round_num} xxxxx
      *** Initiative ***
      ** {inititive_string} **

      -- {self.player_1.name} --
      - back-line -
      {joining_fun(self.player_1.back_line)}
      - front-line -
      {joining_fun(self.player_1.front_line)}
      - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
      {joining_fun(self.player_2.front_line)}
      - front-line -
      {joining_fun(self.player_2.back_line)}
      - back-line -
      -- {self.player_2.name} --
      ''')

  def player_actions(self, soldier):
    print(f'Current soldier {soldier}')
    choose_action = input('Choose your action: 1 - attack the enemy, 2 - get information about any soldier, 3 - surrender.: ')

    if choose_action == '1':
      target = int(input("Choose an enemy's number from the initiative list.: "))
      enemy = self.initiative_list[target - 1]
      if enemy.party == self.player_1.name:
        enemy_party = self.player_1
      else:
        enemy_party = self.player_2
      enemy.be_attacked(soldier, enemy_party)
    elif choose_action == '2':
      target = int(input("Choose an soldier's number from the initiative list.: "))
      print(self.initiative_list[target - 1])
      self.player_actions(soldier)
    elif choose_action == '3':
      if soldier.party == self.player_1.name:
        self.player_1.surrender()
      elif soldier.party == self.player_2.name:
        self.player_2.surrender()
      self.set_winner()
      return 'finish'
    else:
      print('Choose proper action')
      self.player_actions(soldier)

  def run_turn(self):
    self.set_initiative_list()
    for soldier in self.initiative_list:
      self.show_board()
      # Check if player_2 is cpu
      if soldier in self.player_2.all_soldiers and self.player_2.is_cpu:
        print(f'{self.player_2.name} never surrender!')
        target = self.player_2.choose_cpu_oponent(self.player_1, soldier)
        print(target.name)
        #target.be_attacked(self.player_1, soldier)
      else:
        do_or_finish = self.player_actions(soldier)
        if do_or_finish == 'finish': return
      self.party_destroyed()

  def set_round(self):
    self.round_num += 1

  def set_winner(self):
    if (self.player_1.want_surrender):
      self.winner = self.player_2.name
    elif (self.player_2.want_surrender): 
      self.winner = self.player_1.name
    print(f'{self.winner } won the game!')
    return

  def party_destroyed(self):
    if (self.player_1.has_soldiers == 0):
      self.winner = self.player_2.name
    elif (self.player_2.has_soldiers == 0): 
      self.winner = self.player_1.name
    else:
      return
    print(f'{self.winner } won the game!')
    return
  

