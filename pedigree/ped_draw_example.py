''' ped_draw_example.py

an example for the ped_draw.py module
'''

# import required stuff
import ped_draw as pd
import ped as ped
from defs import *

# define people
# this example uses pre-defined disease probabilities, but the actual program
# will calculate these by defining relationships and recursively traversing
# the linked graph
dad = Person('dad', Sex.m, 0.5)
mom = Person('mom', Sex.f, 0)
son1 = Person('son1', Sex.m, 0.25)
son2 = Person('son2', Sex.m, 0.45)
son3 = Person('son3', Sex.m, 0.75)
son4 = Person('son4', Sex.m, 0.99)
dau1 = Person('dau1', Sex.f, 0.82)
dau2 = Person('dau2', Sex.f, 0.04)
hus = Person('hus', Sex.m, 0)
gdau = Person('gdau', Sex.f, 0.32)

# make a Draw object
test = pd.Draw('test')

# draw the marriage with the given children
test.draw_marriage(dad, mom, [son1, son2, son3, son4, dau1, dau2])

# it currently can't draw multiple generations very well
# test.draw_marriage(dau1, hus, [gdau])

# Draw.show() shows the pdf and returns the *.dot description generated
print test.show()
