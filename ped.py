''' ped.py

a basic pedigree thing

A linked tree representation of a pedigree. Person objects form nodes, and
edges are direction toward parents.
'''

class Person:
    father = None  # we use a linked representation for now, although we likely
    mother = None  # want to switch to something easier to modify later
    name = 'Bob'
    sex = 0  # for now, 0 = male and 1 = female
    infected = 0.0  # probability that this person is infected
                    # a negative number indicates 'unknown'

    def __init__(self, name, sex, infected):
        self.name = name
        self.sex = sex
        self.infected = infected

    def add_parents(self, f, m):
        #TODO: ensure that the graph is acyclic
        self.father = f
        self.mother = m

# construct a basic pedigree tree
grandpa = Person('grandpa', 0, 1)
grandma = Person('grandma', 1, 0)
dad = Person('dad', 0, -1)
mom = Person('mom', 1, 0)
son = Person('son', 0, -1)
daughter = Person('daughter', 1, -1)

# define relationships
dad.add_parents(grandpa, grandma)
son.add_parents(dad, mom)
daughter.add_parents(dad, mom)

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

print find_prob(son)
print find_prob(daughter)
