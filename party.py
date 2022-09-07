from random import randrange
from statistics import mean
from data import spec_keys, name_list, atr_list
from soldier import Soldier


# The Party class controls soldiers' flow in units - adding, deleting and changing position
class Party:
  # The constructor function
  def __init__(self, name):
    self.name = name
    # Each soldier with the position attribute equal to 1 fights in the close combat
    self.front_line = []
    # Each soldier with the position attribute equal to 2 fights in the ranged combat
    self.back_line = []
    self.all_soldiers = []
    # The additional protection against arrows ensured by defenders if there are any
    self.back_protection = 0
    self.has_soldiers = 0
    # Human players have possibility to leave the combat
    self.want_surrender = False
    # Second party can be controlled by cpu
    self.is_cpu = False
  

  # The representation function
  def __repr__(self):

    # The helper function checking if there are any soldiers in one of the lines
    def list_soldiers(line, line_name):
      string = f'Soldiers in {line_name}: '
      if len(line) != 0:
        for soldier in line:
          if line.index(soldier) == len(line) -1:
            string += f'{soldier.name}, the {soldier.specialization}.'
            break
          string += f'{soldier.name}, the {soldier.specialization}; '
        
        return string

    # The helper function delivering information about cpu player
    def cpu_info():
      if self.is_cpu:
        return ' - CPU'
      return ''

    string1 = 'front-line'
    string2 = 'back-line'
    return f'The {self.name}{cpu_info()}. {list_soldiers(self.front_line, string1)} {list_soldiers(self.back_line, string2)}'


  # The party assignment method 
  def add_soldier(self, soldier):
    # The soldier's party setter method
    soldier.set_party(self.name)
    self.all_soldiers.append(soldier)
    self.has_soldiers = len(self.all_soldiers)
    
    # The correct line assignment accordingly to the soldier's position attribute
    if soldier.position == 1:
      self.front_line.append(soldier)
      # Set the back-line protection if there are any defenders in the first-line
      if soldier.protect_back:
        self.set_back_protection()
    
    else:
      self.back_line.append(soldier)


  # Remove the soldier when is dead
  def delete_soldier(self, soldier):
    # The Front-line soldier case
    if not soldier.alive and soldier in self.front_line:
      index = self.front_line.index(soldier)
      self.front_line.pop(index)
      # Reset the protection if a defender is dead
      self.set_back_protection()

    # The back-line soldier case
    elif not soldier.alive and soldier in self.back_line:
      index = self.back_line.index(soldier)
      self.back_line.pop(index)
    
    # Reset the list of all soldiers
    self.all_soldiers = []
    self.all_soldiers = self.front_line + self.back_line
    self.has_soldiers = len(self.all_soldiers)


  # Create soldier methond
  def create_soldier(self):
    soldier_name = input("Write soldier's name: ")
    newSoldier = Soldier(soldier_name)

    soldier_spec = input("\nChoose soldier's specialistion (select a number): 0 - swordsman, 1 - defender, 2 - archer, 3 - pikeman: ")
    while soldier_spec not in ['0', '1', '2', '3']:
      print('choose a number from 0 to 3')
      soldier_spec = input("Choose soldier's specialistion (select a number): 0 - swordsman, 1 - defender, 2 - archer, 3 - pikeman: ")
    
    newSoldier.set_spec(spec_keys[int(soldier_spec)])
    newSoldier.set_party(self.name)
    print('\nSet attributes.')

    while newSoldier.atribute_points > 0:
      print(f'{newSoldier.name} {newSoldier.specialization}. Attributes: {newSoldier.attack} attack, {newSoldier.defence} defence, {newSoldier.initiative} initiative')
      print(f"{newSoldier.atribute_points} attribute points left")
      attribute = input("\nChoose an attribute: (a)ttack, (d)effence, (i)nitiative: ")
      
      while attribute not in atr_list:
        print("\nChoose one of these letters: a, d, i.")
        attribute = input("Choose an attribute: (a)ttack, (d)effence, (i)nitiative: ")
      newSoldier.set_atributes(attribute)

    self.add_soldier(newSoldier)


  def create_unit(self, num):
    if self.is_cpu == False:
      for i in range(num):
        print(f"\nCreate soldier number {i + 1}")
        self.create_soldier()

    else:
      for i in range(num):
        self.create_cpu_soldier()
    
    self.back_in_range()
    print(f"\n{self.name} info:")
    print(f'{self}\n')
  
    
  def set_back_protection(self):
    defender_list = list(filter(lambda soldier: (soldier.protect_back), self.front_line))
    defence_values = list(map(lambda soldier: soldier.defence, defender_list))
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
        soldier_to_move.change_pikeman_range()
        temp.append(soldier_to_move)
      self.front_line += temp
      print('First line is empty. Position is changed!')
   

  def surrender(self):
    self.want_surrender = True
    print(f'It is enough for {self.name}!')



  


class CPUParty(Party):
  
  def __init__(self):
    super().__init__('The Bots')
    self.is_cpu = True


  def random_value(self, array):
    idx = randrange(len(array))
    return array[idx]


  def create_cpu_soldier(self):
    # Choose random name from name_list
    rand_name = name_list.pop(randrange(len(name_list)))
    newSoldier = Soldier(rand_name)

    rand_spec = self.random_value(spec_keys)
    newSoldier.set_spec(rand_spec)

    while newSoldier.atribute_points > 0:
      rand_atribute = self.random_value(atr_list)
      newSoldier.set_atributes(rand_atribute)
      newSoldier.set_party(self.name)

    self.add_soldier(newSoldier)


  def choose_cpu_oponent(self, enemy_party, soldier):
    if soldier.range == 2 and enemy_party.back_protection == 0 and len(enemy_party.back_line) != 0:
      return self.random_value(enemy_party.back_line)
    return self.random_value(enemy_party.front_line)

