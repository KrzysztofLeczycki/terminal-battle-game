import array
from party import Party, CPUParty
from soldier import Soldier
from setup import Setup
from random import randrange

new = CPUParty()
#new = Party('GUYS')
sol1 = Soldier('aaa')
sol1.set_spec('archer')
new.add_soldier(sol1)
sol2 = Soldier('bbb')
sol2.set_spec('pikener')
new.add_soldier(sol2)
#new.back_in_range()
sol3 = Soldier('ccc')
sol3.set_spec('defencer')
sol4 = Soldier('ddd')
sol4.set_spec('pikener')
sol5 = Soldier('eee')
sol5.set_spec('swordsman')
sol6 = Soldier('fff')
sol6.set_spec('defencer')

new2 = Party('LOLs')
new2.add_soldier(sol3)
new2.add_soldier(sol4)
new2.add_soldier(sol5)
#new.add_soldier(sol6)

board = Setup(new2, new)

while board.winner is None:
    new2.back_in_range()
    new.back_in_range()
    board.run_turn()
    board.set_round()
    board.set_turn(True)
