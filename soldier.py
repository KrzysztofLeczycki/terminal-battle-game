from data import spec_list, spec_keys

## The Soldier class controls abilities and behaviour 
class Soldier:
  #The constructor function
  def __init__(self, name):
    self.name = name
    self.party = None
    # Each soldier has an equal number of attributes points
    self.atribute_points = 4
    # Each soldier has an equal number of health points
    self.health = 10
    self.alive = True
    # Thera are 4 specializations: swordsman, defender, archer and pikeman. See more details in data.py
    self.specialization = None
    # Attack, defence and initiative are depended on specialization. 
    # They can be improved by spending attribute points
    self.attack = 1
    self.defence = 1
    self.initiative = 1 # Places soldier in 'initiative list'
    #
    # These attributes are dependent only on specialization
    self.position = None # Soldiers stand on one from two lines: front and back
    self.range = 1 # Range value equal 1 means that a soldier is able to hit an enemy only in front-line, value means the attack is possible to back-line too
    self.protect_back = False # Value 'True' is reserved only for defenders who increase the defence value of soldiers in back-line
    

  # Representation of Soldier object
  def __repr__(self):

    # Helper function that back-line is protected by a defender
    def can_protect():
      if self.protect_back:
        return f'{self.name} protects back-line against arrows'
      else: 
        return ''    

    return f'''{self.name}, the {self.specialization} has {self.health}/10 HP. 
                Attributes: {self.attack} attack, {self.defence} defence, {self.initiative} initiative, {self.range} range. {can_protect()}'''


  # The method that sets all attributes depended on the specialization. See data.py to see specializations' specification
  def set_spec(self, spec):
    spec_index = spec_keys.index(spec)
    self.specialization = spec_keys[spec_index]
    self.attack += spec_list[spec]['attack']
    self.defence += spec_list[spec]['defence']
    self.initiative += spec_list[spec]['initiative']
    self.position = spec_list[spec]['position']
    self.range = spec_list[spec]['range']
    self.protect_back = spec_list[spec]['protect_back']


  # The method sets attributes accordingly to the player's choice
  def set_atributes(self, key):
    if key == 'a':
      self.attack += 1
    elif key == 'd':
      self.defence += 1
    elif key == 'i':
      self.initiative += 1
    self.atribute_points -= 1


  # The method sets the soldier's party
  def set_party(self, my_party):
    self.party = my_party


  # self.alive setter function
  def is_dead(self):
    if self.health <= 0:
      self.alive = False
      print(f'{self.name} bytes the dust.')


  # The method checks if the enemy is able to reach the soldier. The only case that attack can't be performed is when the attacker has range '1' and the defender stands on back-line
  # Example: the current soldier Mark wants to hit the enemy soldier John. Methot should be called like this:
  # John.can_be_attacked(Mark)
  # Note: The pikeman who stands on the front-line (when there are no attackers or defenders in a party) can reach back-line
  def can_be_attacked(self, enemy):
    return not (enemy.range == 1 and self.position == 2) 


  # The method changes pikemen's and archers' position from '2' to '1' when there are no soldiers in front-line
  def reduce_position(self, my_party):
    if self.position == 2 and len(my_party.front_line) == 0:
      self.position = 1
      print(f'{my_party.name} lost all soldiers in front-line. {self.name} is within direct range now.')
      

  # The method changes pikeman's range to '2' when there are no soldiers on the front-line
  def change_pikener_range(self):
    if self.specialization == 'pikeman':
      self.range = 2


  # The method controls attacks. 
  # Example: the current soldier Mark wants to hit the enemy soldier John. Methot should be called like this:
  # John.be_attacked(Mark, Johns_party)
  def be_attacked(self, enemy, my_party):
    if self.can_be_attacked(enemy):
      # These part of the code checks if soldiers standing on the back-line have additional protection ensured by defender
      if self.position == 2 and enemy.specialization == 'archer':
        damage = enemy.attack - (self.defence + my_party.back_protection) // 2
      else:
        damage = enemy.attack - self.defence // 2
      # In some cases damage value could be equal to 0 or less than 0 (that means attacked soldier would gain additional health points)
      # Just to avoid pat situations on the battlefield or miraculous healings any soldier loses at least 1 health point
      if damage <= 0: damage = 1
      print(f'{self.name} had {self.health} HP and lost {damage} HP. \n')
      self.health -= damage
      self.is_dead()
      # When a soldier dies he is removed from his party object. See party.py
      my_party.delete_soldier(self)
    else:
      print(f'{enemy.name} out of range!')