''' pun.py

a simple punnett square solver

This program can solve a Punnett square for any number of traits with two
alleles. The output is returned as a list of combinations for each trait.

To use interactively, just try this:
   plot(str2geno('Aa'), str2geno('Aa'))
This can be expanded to any size of genotype, for example:
   father = str2geno('AaBBcc')
   mother = str2geno('AabbCc')
   plot(father, mother)
'''

import numpy as np
import colortable as ct

# this isn't really necessary unless you want to use numpy lin alg routines
class allele:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return allele(self.name + other.name)
    def __mul__(self, other):
        # WARNING: two alleles being multiplied MUST have same length
        # use addition if untrue
        return allele(''.join([self.name[i]+other.name[i] for i, _ in
                               enumerate(self.name)]))
    def __repr__(self):
        return self.name

# a more convenient way of defining a person
# simply converts a string to a genotype, which is a 2d array of alleles
def str2geno(string):
    res = []
    for i in range(0, len(string), 2):
        res += [[allele(string[i]), allele(string[i+1])]]
    return res

father = str2geno('AaBbCc')
mother = str2geno('AAbbCc')

# combines possibility results into full genotypes strings
def combine(arr, depth):
    if depth == len(arr):
        return [allele('')]
    return [i+j for i in arr[depth] for j in combine(arr, depth+1)]

# plots the solution with the colortable.py module
def plot(f, m):
    # takes in the parent arrays
    f_arr, m_arr = combine(f, 0), combine(m, 0)
    sol_arr = np.outer(m_arr, f_arr).tolist()
    square = [[allele('')] + f_arr]
    nrows = len(f_arr) + 1
    for i in range(nrows-1):
        square += [[m_arr[i]] + sol_arr[i]]
    print square
    table = ct.colortbl(square)
    # TODO: come up with a function for coloring (these are just an example)
    table.color(1, 1, c1='#fcaba4')
    table.color(1, 2, c1='#fcaba4', c2='#a4c4fc')
    table.color(2, 1, c1='#fcaba4', c2='#a4c4fc', c3='#ffe987')
    table.color(2, 2, c1='#fcaba4', c2='#a4c4fc', c3='#ffe987', c4='#cdf2c6')
    table.title('a Punnett square')
    table.show()

print 'Plotting results...'
plot(father, mother)
