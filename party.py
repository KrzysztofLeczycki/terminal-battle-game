from random import randrange
from statistics import mean


class Party:
  def __init__(self, name):
    self.name = name
    self.front_line = []
    self.back_line = []
    self.back_protection = 0
    self.has_soldiers = len(self.front_line + self.back_line)
    self.want_surrender = False
    self.is_cpu = False
  
  def list_soldiers(self, line):
    string = ''
    if len(line) != 0:
      for soldier in line:
        string += f'{soldier.name}, the {soldier.specialization}; '
    return string

  def __repr__(self):
    return f'The {self.name}. Soldiers in front-line: {self.list_soldiers(self.front_line)}. Soldiers in back-line: {self.list_soldiers(self.back_line)}.'

  def add_soldier(self, soldier):
    soldier.set_party(self.name)
    if soldier.position == 1:
      self.front_line.append(soldier)
      if soldier.protect_back:
        self.set_back_protection()
    else:
      self.back_line.append(soldier)

  def delete_soldier(self, soldier):
    if not soldier.alive and soldier in self.front_line:
      index = self.front_line.index(soldier)
      self.front_line.pop(index)
      self.set_back_protection()
    elif not soldier.alive and soldier in self.back_line:
      index = self.back_line.index(soldier)
      self.back_line.pop(index)
    
  def set_back_protection(self):
    defencer_list = list(filter(lambda soldier: (soldier.protect_back), self.front_line))
    defence_values = list(map(lambda soldier: soldier.defence, defencer_list))
    if len(defence_values) != 0:
      self.back_protection = round(mean(defence_values))
    else:
      self.back_protection = 0

  def back_in_range(self):
    if len(self.front_line) == 0:
      for i in range(len(self.back_line)):
        self.front_line.append(self.back_line.pop(i))
      print('Changed position!')

  def surrender(self):
    self.want_surrender = True
    print(f'It is enough for {self.name}!')
  
class CPUParty(Party):
  
  def __init__(self, name):
    super().__init__('The Bots')
    self.is_cpu = True

  def __repr__(self):
    return f'{self.name} - CPU. Soldiers in front-line: {self.list_soldiers(self.front_line)}. Soldiers in back-line: {self.list_soldiers(self.back_line)}.'  

  def random_value(self, array):
    idx = randrange(len(array))
    return array[idx]

  def choose_cpu_oponent(self, enemy_party, soldier):
    if soldier.range == 2 and enemy_party.back_protection == 0:
      return self.random_value(enemy_party.back_line)
    return self.random_value(enemy_party.front_line)

