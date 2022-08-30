from party import Party, CPUParty
from soldier import Soldier
from setup import Setup


new = Party('GUYS')
sol1 = Soldier('aaa')
sol1.set_spec('archer')
new.add_soldier(sol1)
sol2 = Soldier('bbb')
sol2.set_spec('archer')
new.add_soldier(sol2)
new.back_in_range()

new2 = Party('LOLs')
new2.add_soldier(sol1)
new2.add_soldier(sol2)

board = Setup(new, new2)
board.set_initiative_list()
#print(board.initiative_list)
board.show_board()