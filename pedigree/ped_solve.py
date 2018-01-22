''' ped_solve.py

contains defintions needed for solving pedigrees
'''

# enumerated Sex type with possibilities 'male' and 'female'
def enum(**enums):
    return type('Enum', (), enums)
Sex = enum(m='male', f='female')

# the Person class represents an individual and serves as a node for the DAG
class Person:
    father = None  # we use a linked representation for now, although we likely
    mother = None  # want to switch to something easier to modify later
    name = 'Bob'
    sex = Sex.m
    infected = -1.0  # probability that this person is infected
                     # a negative number indicates 'unknown'

    def __init__(self, name, sex, infected=-1.0):
        self.name = name
        self.sex = sex
        self.infected = infected

    def add_parents(self, f, m):
        #TODO: ensure that the graph is acyclic
        self.father = f
        self.mother = m

    def get(self):
        return (self.name, self.sex, self.infected)

def infect(f, m):
    # this is a proof of concept
    # for now, we will use the rule that prob = 0.5*f_prob + 0.5*m_prob
    # in actuality, the rule depends on what type of disease, sex, etc.
    return 0.5 * (f + m)

# recursively determine the probability for a given person
def find_prob(person, silent=False):
    # silent allows no stdout printing for CGI script
    if person.infected >= 0:
        # this person has an independent probability
        return person.infected
    if person.father == None or person.mother == None:
        # this person does not have a mother or father but has no probability
        if not silent:
            print 'error@%s' % person.name
            print ('  error: all founder individuals must have independent '
                   'probabilities')
        return -1
    f = find_prob(person.father)
    m = find_prob(person.mother)
    person.infected = infect(f, m)
    return person.infected
