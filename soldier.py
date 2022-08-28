from data import spec_list, spec_keys

class Soldier:
  def __init__(self, name):
    self.name = name
    self.specialization = None
    self.atribute_points = 4
    self.health = 10
    self.attack = 1
    self.defence = 1
    self.initiative = 1
    self.position = None
    self.range = 1
    self.protect_back = False
    self.alive = True
    self.party = None

 ############# 
 # __repr__ helper functions
  def has_spec(self):
    if self.specialization:
      return f', the {self.specialization}'

  def can_protect(self):
    if self.protect_back:
      return f'{self.name} protects back-line against arrows'
    elif self.position == 1:
      return f'{self.name} does not protect back-line against arrows'
   
  
  ############# 

  def __repr__(self):
    return f'{self.name}{self.has_spec()} has {self.health}/10 HP. Attributes: {self.attack} attack, {self.defence} defence, {self.initiative} initiative, {self.range} range. {self.can_protect()}'

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

  def can_attack(self, enemy):
    return enemy.range >= self.position

  def reduce_position(self, my_party):
    if self.position == 2 and len(my_party.front_line) == 0:
      self.position = 1
      print(f'{my_party.name} lost all soldiers in front-line. Back-line is within direct range')

  def be_attacked(self, enemy, my_party):
    self.reduce_position(my_party)
    my_party.back_in_range()
    if self.can_attack(enemy):
      if self.position == 2 and enemy.specialization == 'archer':
        damage = enemy.attack - (self.defence + my_party.back_protection) // 2
      else:
        damage = enemy.attack - self.defence // 2
      print(f'{self.name} had {self.health} HP and lost {damage} HP.')
      self.health -= damage
      self.is_dead()
      my_party.delete_soldier(self)
    else:
      print(f'{enemy.name} out of range!')

