from ntpath import join
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


  def set_round(self):
    self.round_num += 1

  def set_winner(self):
    if self.player_1.has_soldiers == 0 or self.player_1.want_surrender:
      self.winner = self.player_2.name
    elif self.player_2.has_soldiers == 0 or self.player_2.want_surrender: 
      self.winner = self.player_1.name
    print(f'{self.winner } won the game!')
