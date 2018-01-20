''' MODULE: allele.py

provides some basic definitions and routines for solving punnett squares

This is not really the main Punnett square solver. Karena's main.py script is
the general solver. This is just a quick solver for proof-of-concept for the
website.
'''
import numpy as np
import colortable as ct

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

def str2geno(string):
    res = []
    for i in range(0, len(string), 2):
        res += [[allele(string[i]), allele(string[i+1])]]
    return res

def combine(arr, depth):
    if depth == len(arr):
        return [allele('')]
    return [i+j for i in arr[depth] for j in combine(arr, depth+1)]

def solve(f, m):
    f_arr, m_arr = combine(str2geno(f), 0), combine(str2geno(m), 0)
    sol_arr = np.outer(m_arr, f_arr).tolist()
    square = [[allele('')] + f_arr]
    nrows = len(f_arr) + 1
    for i in range(nrows-1):
        square += [[m_arr[i]] + sol_arr[i]]
    return square

def plot(f, m, title=''):
    square = solve(f, m)
    table = ct.colortbl(square)
    table.title(title)
    return table
