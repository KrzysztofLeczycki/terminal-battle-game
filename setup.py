from random import randrange
class Setup:
  def __init__(self, party1, party2):
    self.player_1 = party1
    self.player_2 = party2
    self.initiative_list = []
    self.round_num = 1
    self.turn_num = 1
    self.winner = None
  

  def __repr__(self):
    return f'{self.player_1} fought against {self.player_2}. The winner is {self.winner}.'


  def set_initiative_list(self):
    soldiers_list = []
    soldiers_list += self.player_1.front_line + self.player_1.back_line + self.player_2.front_line + self.player_2.back_line
    
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
 

  def initiative_stringify(self, enemy_only=False, current_soldier=None):
    if not enemy_only:
      character_list = list(map(lambda soldier: f'{self.initiative_list.index(soldier) + 1}: {soldier.party} - {soldier.name}', self.initiative_list))
      return '   * '.join(character_list)
    else:
      filtered_list = []
      for soldier in self.initiative_list:
        if soldier.party != current_soldier.party and soldier.alive:
          key = self.initiative_list.index(soldier) + 1
          filtered_list.append(f'{key}: {soldier.name} ({soldier.specialization})')
      return '   * '.join(filtered_list)


  def choose_soldier(self, input):
    idx = int(input) - 1
    return self.initiative_list[idx]


  def show_board(self): 
    def joining_fun(arr):
      representation = list(map(lambda soldier: f'{soldier.name} - {soldier.specialization} {soldier.health}/10 HP', arr))
      return '   |   '.join(representation)
    
    print(
      f'''

      xxxxxxxx Round {self.round_num} xxxxxxxx
         xxxxx Turn {self.turn_num} xxxxx

      *** Initiative ***
      ** {self.initiative_stringify()} **

      -- {self.player_1.name} --
      
      back:   {joining_fun(self.player_1.back_line)}
    
      front:  {joining_fun(self.player_1.front_line)}
      - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
      front:  {joining_fun(self.player_2.front_line)}
      
      back:   {joining_fun(self.player_2.back_line)}
      
      -- {self.player_2.name} --

      ''')


  def reset_front_line(self):
    self.player_1.back_in_range()
    self.player_2.back_in_range()


  def player_actions(self, soldier):
    
    choose_action = input('Choose your action: 1 - attack the enemy, 2 - get information about any soldier, 3 - surrender.: ')
    print('\n')

    def reset_choice():
      if self.initiative_list.index(soldier) == target -1:
        print('You are an idiot! Your are trying to hit yourself! Do something different.')
        return True
      elif not enemy.alive:
        print(f"{enemy.name} is dead enough, so let him rest in piece. Do something different.")
        return True
      elif not enemy.can_be_attacked(soldier):
        print(f'You are more likely to hit your head, than reach {enemy.name}! Do something different.')
        return True


    if choose_action == '1':
      print(f'Initiative list (watch out on friendly fire): {self.initiative_stringify(enemy_only=True, current_soldier=soldier)}')
      target = int(input("Choose an enemy's number from the initiative list.: "))
      enemy = self.initiative_list[target - 1]
      
      if reset_choice(): self.player_actions(soldier)
     
      if enemy.party == self.player_1.name:
        enemy_party = self.player_1
      else:
        enemy_party = self.player_2
      enemy.be_attacked(soldier, enemy_party)
      
    elif choose_action == '2':
      print(f'Initiative list: {self.initiative_stringify()}')
      target = int(input("Choose an soldier's number from the initiative list.: "))
      print(self.initiative_list[target - 1])
      print('\n')
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
    for soldier in self.initiative_list:
      self.reset_front_line()
      self.show_board()
      
      # Check if player_2 is cpu
      if soldier.health < 1:
        continue
      print(f'Current soldier {soldier}')
      
      if soldier in self.player_2.all_soldiers and self.player_2.is_cpu:
        print(f'{self.player_2.name} never surrender!')
        target = self.player_2.choose_cpu_oponent(self.player_1, soldier)
        target.be_attacked(soldier, self.player_1)
      
      else:
        do_or_finish = self.player_actions(soldier)
        if do_or_finish == 'finish': return
      
      is_finished = self.party_destroyed()
      if is_finished: break
      self.set_turn()


  def set_round(self):
    self.round_num += 1


  def set_turn(self, new_round=False):
    if new_round: 
      self.turn_num = 1
    else:
      self.turn_num += 1


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
    print("The last enemy's soldier is down!")
    print(f'{self.winner } won the game!')
    return True
  

