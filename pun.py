import numpy as np

class allele:
    def __init__(self, name):
        self.name = name
    
    def __mul__(self, other):
        return allele(self.name + other.name)
    
    def __repr__(self):
        return self.name

A = allele('A')
a = allele('a')
B = allele('B')
b = allele('b')
C = allele('C')
c = allele('c')

father = [[A, a], [B, b], [C, C]]
mother = [[A, A], [b, b], [C, c]]

def solve(f, m):
    res_arr = []
    res = []
    for i, dummy in enumerate(father):
        #TODO: flatten result of np.outer().tolist() first to avoid awkward loops
        res_arr += [np.outer(father[i], mother[i]).tolist()]
    for item in res_arr:
        tmp = [j for i in item for j in i]
        res += [tmp]
    print res
    print np.outer(res[0], res[1])
    #print res
    #print np.kron(res[0], res[1])

solve(father, mother)