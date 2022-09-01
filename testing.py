from party import Party, CPUParty
from soldier import Soldier
from setup import Setup
from random import randrange

#new = Party('GUYS')
new = CPUParty()
sol1 = Soldier('aaa')
sol1.set_spec('archer')
new.add_soldier(sol1)
sol2 = Soldier('bbb')
sol2.set_spec('swordsman')
new.add_soldier(sol2)
new.back_in_range()
sol3 = Soldier('ccc')
sol3.set_spec('swordsman')
sol4 = Soldier('ddd')
sol4.set_spec('pikener')

new2 = Party('LOLs')
new2.add_soldier(sol3)
new2.add_soldier(sol4)

board = Setup(new2, new)
board.set_initiative_list()

while board.winner is None:
  board.run_turn()
  board.set_round()
  board.set_turn(True)
