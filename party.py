from random import randrange
from statistics import mean
from data import spec_keys, name_list, atr_list
from soldier import Soldier

class Party:
  def __init__(self, name):
    self.name = name
    self.front_line = []
    self.back_line = []
    self.all_soldiers = []
    self.back_protection = 0
    self.has_soldiers = 0
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
    self.all_soldiers.append(soldier)
    self.has_soldiers = len(self.all_soldiers)
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
    self.all_soldiers = []
    self.all_soldiers = self.front_line + self.back_line
    self.has_soldiers = len(self.all_soldiers)
    
  def set_back_protection(self):
    defencer_list = list(filter(lambda soldier: (soldier.protect_back), self.front_line))
    defence_values = list(map(lambda soldier: soldier.defence, defencer_list))
    if len(defence_values) != 0:
      self.back_protection = round(mean(defence_values))
    else:
      self.back_protection = 0

  def back_in_range(self):
    if len(self.front_line) == 0:
      temp = []
      while len(self.back_line) > 0:
        soldier_to_move = self.back_line.pop()
        soldier_to_move.reduce_position(self)
        soldier_to_move.change_pikener_range()
        temp.append(soldier_to_move)
      self.front_line += temp
      print('First line is empty. Position is changed!')
   

  def surrender(self):
    self.want_surrender = True
    print(f'It is enough for {self.name}!')


  def create_soldier(self):
    soldier_name = input("Write soldier's name: ")
    newSoldier = Soldier(soldier_name)

    soldier_spec = input("Choose soldier's specialistion (select a number): 0 - swordsman, 1 - defencer, 2 - archer, 3 - pikener: ")
    while soldier_spec not in ['0', '1', '2', '3']:
      print('choose a number from 0 to 3')
      soldier_spec = input("Choose soldier's specialistion (select a number): 0 - swordsman, 1 - defencer, 2 - archer, 3 - pikener: ")
    
    newSoldier.set_spec(spec_keys[int(soldier_spec)])
    newSoldier.set_party(self.name)
    print('Set attributes.')

    
    while newSoldier.atribute_points > 0:
      print(f'{newSoldier.name} {newSoldier.has_spec()}. Attributes: {newSoldier.attack} attack, {newSoldier.defence} defence, {newSoldier.initiative} initiative')
      print(f"{newSoldier.atribute_points} attribute points left")
      attribute = input("Choose an attribute: (a)ttack, (d)effence, (i)nitiative ")
      while attribute not in atr_list:
        print("Choose one of these letters: a, d, i.")
        attribute = input("Choose an attribute: (a)ttack, (d)effence, (i)nitiative ")
      newSoldier.set_atributes(attribute)

    self.add_soldier(newSoldier)
  


class CPUParty(Party):
  
  def __init__(self):
    super().__init__('The Bots')
    self.is_cpu = True

  def __repr__(self):
    return f'{self.name} - CPU. Soldiers in front-line: {self.list_soldiers(self.front_line)}. Soldiers in back-line: {self.list_soldiers(self.back_line)}.'  

  def random_value(self, array):
    idx = randrange(len(array))
    return array[idx]

  def create_cpu_soldier(self):
    rand_name = self.random_value(name_list)
    newSoldier = Soldier(rand_name)

    rand_spec = self.random_value(spec_keys)
    newSoldier.set_spec(rand_spec)

    while newSoldier.atribute_points > 0:
      rand_atribute = self.random_value(atr_list)
      newSoldier.set_atributes(rand_atribute)
      newSoldier.set_party(self.name)

    self.add_soldier(newSoldier)


  def choose_cpu_oponent(self, enemy_party, soldier): #poprawić fuknkcję, żeby cpu nie strzelał w puste pola
    if soldier.range == 2 and enemy_party.back_protection == 0:
      return self.random_value(enemy_party.back_line)
    return self.random_value(enemy_party.front_line)

