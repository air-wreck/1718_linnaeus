''' ped_draw_example.py

an example for the ped_draw.py module
'''

# import required stuff
import ped_draw as pd
import ped_solve as ps

# define people
# this example uses pre-defined disease probabilities, but the actual program
# will calculate these by defining relationships and recursively traversing
# the linked graph
dad = ps.Person('dad', ps.Sex.m, 0.5)
mom = ps.Person('mom', ps.Sex.f, 0)
son1 = ps.Person('son1', ps.Sex.m, 0.25)
son2 = ps.Person('son2', ps.Sex.m, 0.45)
son3 = ps.Person('son3', ps.Sex.m, 0.75)
son4 = ps.Person('son4', ps.Sex.m, 0.99)
dau1 = ps.Person('dau1', ps.Sex.f, 0.82)
dau2 = ps.Person('dau2', ps.Sex.f, 0.04)
gda1 = ps.Person('gda1', ps.Sex.f, 0.32)
gso1 = ps.Person('gso1', ps.Sex.m, 0.39)
gso2 = ps.Person('gso2', ps.Sex.m, 0.00)
gso3 = ps.Person('gso3', ps.Sex.m, 1.00)
gda2 = ps.Person('gda2', ps.Sex.f, 0.88)

# make a Draw object
test = pd.Draw('test')

# draw the marriage with the given children
test.draw_marriage(dad, mom, [son1, son2, dau1])

# another family!
d2 = ps.Person('d2', ps.Sex.m, 0.09)
m2 = ps.Person('m2', ps.Sex.f, 0.67)
hus = ps.Person('hus', ps.Sex.m, 0.8)
chi = ps.Person('chi', ps.Sex.f, 0.76)
nese = ps.Person('nese', ps.Sex.f, 0.45)
test.draw_marriage(d2, m2, [hus, chi, nese])
# it currently can't draw multiple generations very well
test.draw_marriage(dau1, hus, [gda1, gso1, gda2])

# Draw.show() shows the pdf and returns the *.dot description generated
print test.show()
