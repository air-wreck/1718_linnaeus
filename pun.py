''' pun.py

a simple punnett square solver

This program can solve a Punnett square for any number of traits with two
alleles. The output is returned as a list of combinations for each trait.
'''

import numpy as np

# this isn't really necessary unless you want to use numpy lin alg routines
class allele:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return allele(self.name + other.name)
    def __mul__(self, other):
        return allele(self.name + other.name)
    def __repr__(self):
        return self.name

# a more convenient way of defining a person
# simply converts a string to a genotype, which is a 2d array of alleles
def str2geno(string):
    res = []
    for i in range(0, len(string), 2):
        res += [[allele(string[i]), allele(string[i+1])]]
    return res

''' this is the long way to do it:
# bind variables to allele objects
A = allele('A')
a = allele('a')
B = allele('B')
b = allele('b')

# set up the father and mother with any number of traits
father = [[A, a], [B, b]]
mother = [[A, A], [b, b]]
'''

# this is the short way:
father = str2geno('AaBb')
mother = str2geno('AAbb')

# find all possibilities
# this is ovecomplicated, but I really wanted to use a linear algebra function
def solve(f, m):
    res = []
    for i, dummy in enumerate(father):
        res += [np.outer(father[i], mother[i]).flatten().tolist()]
    return res

# combines possibility results into full genotypes strings
def combine(arr, depth):
    if depth == len(arr):
        return [allele('')]
    return [i+j for i in arr[depth] for j in combine(arr, depth+1)]

sol = solve(father, mother)
print 'The possible traits are:'
print sol
print ''
print 'The overall combinations are:'
print combine(sol, 0)
print ''
print 'The possibilities for the father are:'
print combine(father, 0)
print ''
print 'The possibilities for the mother are:'
print combine(mother, 0)
