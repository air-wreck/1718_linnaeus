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
gda1 = Person('gda1', Sex.f, 0.32)
gso1 = Person('gso1', Sex.m, 0.39)
gso2 = Person('gso2', Sex.m, 0.00)
gso3 = Person('gso3', Sex.m, 1.00)
gda2 = Person('gda2', Sex.f, 0.88)

# make a Draw object
test = pd.Draw('test')

# draw the marriage with the given children
test.draw_marriage(dad, mom, [son1, son2, dau1])

# another family!
d2 = Person('d2', Sex.m, 0.09)
m2 = Person('m2', Sex.f, 0.67)
hus = Person('hus', Sex.m, 0.8)
chi = Person('chi', Sex.f, 0.76)
nese = Person('nese', Sex.f, 0.45)
test.draw_marriage(d2, m2, [hus, chi, nese])
# it currently can't draw multiple generations very well
test.draw_marriage(dau1, hus, [gda1, gso1, gda2])

# Draw.show() shows the pdf and returns the *.dot description generated
print test.show()
