#!/usr/bin/env python

import sys, os, cgitb
# ideally, the paths will be changed for the final project so that this is not
# necessary to do
sys.path.insert(1, os.path.join(sys.path[0], '../punnett'))
import allele

# these will be retrieved from HTTP POST once this is working okay
father = 'Aa'
mother = 'Aa'

# plot the punnett square
psquare = allele.plot(father, mother, title='example')
psquare.color(1, 1, c1='#a4c4fc')
psquare.color(2, 2, c1='#fcaba4')
psquare.color(1, 2, c1='#fcaba4', c2='#a4c4fc')
psquare.color(2, 1, c1='#fcaba4', c2='#a4c4fc')

# print the image to stdout
print 'Content-Type: image/png'
print ''
print psquare.to_png()
