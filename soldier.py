from data import spec_list, spec_keys

## Soldier class controls abbilities and behaviour 
class Soldier:
  def __init__(self, name):
    self.name = name
    self.party = None
    # Each soldier has equal number of atributes points
    self.atribute_points = 4
    # Each soldier has equal number of health points
    self.health = 10
    self.alive = True
    # Thera are 4 specializations: swordsman, defencer, archer and pikiner. See more details in data.py
    self.specialization = None
    # Attack, defence and initiative are depended on specialization. 
    # They can be improved by spending atribute points
    self.attack = 1
    self.defence = 1
    self.initiative = 1 # Places soldier in 'initiative list'
    #
    # These attributes are dependent only on specialization
    self.position = None # Soldiers stands on one from two lines: front and back
    self.range = 1 # 
    self.protect_back = False
    

  def __repr__(self):

    def can_protect():
      if self.protect_back:
        return f'{self.name} protects back-line against arrows'
      else: 
        return ''    

    return f'''{self.name}, the {self.specialization} has {self.health}/10 HP. 
                Attributes: {self.attack} attack, {self.defence} defence, {self.initiative} initiative, {self.range} range. {can_protect()}'''


  def set_spec(self, spec):
    spec_index = spec_keys.index(spec)
    self.specialization = spec_keys[spec_index]
    self.attack += spec_list[spec]['attack']
    self.defence += spec_list[spec]['defence']
    self.initiative += spec_list[spec]['initiative']
    self.position = spec_list[spec]['position']
    self.range = spec_list[spec]['range']
    self.protect_back = spec_list[spec]['protect_back']


  def set_atributes(self, key):
    if key == 'a':
      self.attack += 1
    elif key == 'd':
      self.defence += 1
    elif key == 'i':
      self.initiative += 1
    self.atribute_points -= 1


  def set_party(self, my_party):
    self.party = my_party


  def is_dead(self):
    if self.health <= 0:
      self.alive = False
      print(f'{self.name} bytes the dust.')


  def can_be_attacked(self, enemy):
    return not (enemy.range == 1 and self.position == 2) 


  def reduce_position(self, my_party):
    if self.position == 2 and len(my_party.front_line) == 0:
      self.position = 1
      print(f'{my_party.name} lost all soldiers in front-line. {self.name} is within direct range now.')
      

  def change_pikener_range(self):
    if self.specialization == 'pikener':
      self.range = 2


  def be_attacked(self, enemy, my_party):
    self.reduce_position(my_party)
    my_party.back_in_range()
    if self.can_be_attacked(enemy):
      if self.position == 2 and enemy.specialization == 'archer':
        damage = enemy.attack - (self.defence + my_party.back_protection) // 2
      else:
        damage = enemy.attack - self.defence // 2
      if damage <= 0: damage = 1
      print(f'{self.name} had {self.health} HP and lost {damage} HP. \n')
      self.health -= damage
      self.is_dead()
      my_party.delete_soldier(self)
    else:
      print(f'{enemy.name} out of range!')

