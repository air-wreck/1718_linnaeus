''' ped_draw_example.py

an example for the ped_draw.py and ped_solve.py modules
'''

# import required stuff
import ped_draw as pd
import ped_solve as ps


###############
# DEFINE PEOPLE
###############

# the J clan
john = ps.Person('John', ps.Sex.m, 1.00)
jane = ps.Person('Jane', ps.Sex.f, 0.65)
jim = ps.Person('Jim', ps.Sex.m)
joe = ps.Person('Joe', ps.Sex.m)
joan = ps.Person('Joan', ps.Sex.f)
jim.add_parents(john, jane)
joe.add_parents(john, jane)
joan.add_parents(john, jane)

# the M clan
mark = ps.Person('Mark', ps.Sex.m, 0.35)
mary = ps.Person('Mary', ps.Sex.f, 0.00)
Max = ps.Person('Max', ps.Sex.m)
mercy = ps.Person('Mercy', ps.Sex.f)
marie = ps.Person('Marie', ps.Sex.f)
Max.add_parents(mark, mary)
mercy.add_parents(mark, mary)
marie.add_parents(mark, mary)

# the union of the J and M clans
anne = ps.Person('Anna', ps.Sex.f)
alex = ps.Person('Alex', ps.Sex.m)
amy = ps.Person('Amy', ps.Sex.f)
anne.add_parents(Max, joan)
alex.add_parents(Max, joan)
amy.add_parents(Max, joan)


###################
# DRAW THE PEDIGREE
###################

# make a Draw object
test = pd.Draw('example')

# draw the marriages with the given children
# pd.Draw.draw_marriage() automatically calls ps.find_prob() on all people
test.draw_marriage(john, jane, [jim, joe, joan])
test.draw_marriage(mark, mary, [Max, mercy, marie])
test.draw_marriage(joan, Max, [anne, alex, amy])

# pd.Draw.show() shows the pdf and returns the *.dot description generated
print test.show()
