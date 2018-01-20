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

import allele

father = 'Aa'
mother = 'Aa'

print 'Plotting results...'
psquare = allele.plot(father, mother, title='example')
psquare.color(1, 1, c1='#a4c4fc')
psquare.color(2, 2, c1='#fcaba4')
psquare.color(1, 2, c1='#fcaba4', c2='#a4c4fc')
psquare.color(2, 1, c1='#fcaba4', c2='#a4c4fc')
psquare.show()
