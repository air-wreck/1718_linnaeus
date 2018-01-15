''' defs.py

contains common definitions that need to exist across multiple files
'''

def enum(**enums):
    return type('Enum', (), enums)
Sex = enum(m='male', f='female')

class Person:
    father = None  # we use a linked representation for now, although we likely
    mother = None  # want to switch to something easier to modify later
    name = 'Bob'
    sex = Sex.m
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
