''' ped.py

a basic pedigree thing that defines two functions infect() and find_prob()
should probably be bundled with defs.py, but that can be done later

A linked tree representation of a pedigree. Person objects form nodes, and
edges are directed toward parents.
'''

import ped_draw as pd
from defs import *

# determine probability that a given individual is infected
def infect(f, m):
    # for now, we will use the rule that prob = 0.5*f_prob + 0.5*m_prob
    # in actuality, the rule depends on what type of disease, sex, etc.
    return 0.5 * (f + m)

# recursively determine the probability for a given person
def find_prob(person):
    if person.infected >= 0:
        # this person has an independent probability
        return person.infected
    if person.father == None or person.mother == None:
        # this person does not have a mother or father but has no probability
        print 'error@%s' % person.name
        print ('  error: all founder individuals must have independent '
              'probabilities')
        return -1
    f = find_prob(person.father)
    m = find_prob(person.mother)
    person.infected = infect(f, m)
    return person.infected

if __name__ == '__main__':
    # construct a basic pedigree tree
    grandpa = Person('grandpa', Sex.m, 1)
    grandma = Person('grandma', Sex.f, 0)
    dad = Person('dad', Sex.m, -1)
    mom = Person('mom', Sex.f, 0)
    son = Person('son', Sex.m, -1)
    daughter = Person('daughter', Sex.f, -1)

    # define relationships
    dad.add_parents(grandpa, grandma)
    son.add_parents(dad, mom)
    daughter.add_parents(dad, mom)

    print find_prob(son)
    print find_prob(daughter)
