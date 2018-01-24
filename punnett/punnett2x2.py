''' punnett2x2.py

a simple punnett square solver for the 2x2 size

This program can solve a Punnett square for any number of traits with two
alleles. The output is returned as a punnett square drawn using matplotlib along 
with a matrix of probabilities of offspring phenotypes

To use interactively, just type makeSquare2().
'''

import matplotlib.pyplot as plt
import colortable as ct
import re
import os

#value of global variables reflect current mode of inheritance
inc = False
cod = False
xl = False

def makeSquare2(): #Creates 2x2 Punnett Square;
    global inc
    global cod
    global xl
    inc, cod, xl = False, False, False
    global inherit
    inherit = inheritlist(raw_input('Please enter \'aut\' for autosomal,'
        '\'inc\' for incomplete dominance, \'cod\' for codominance, and \'xl\' for x-linked.\n')) #User inputs inheritance format
    if inherit == "invalid" or inherit == "help":#error checking if user doesn't enter according to rules
        while inherit == "invalid" or inherit == 'help': #loops until user input is valid
            if inherit == 'help': #opens help documentation 
                os.system('notepad.exe help.txt')
            print "Please try again."
            inherit = inheritlist(raw_input('Please enter \'aut\' for autosomal,'
        '\'inc\' for incomplete dominance, \'cod\' for codominance, and xl for x-linked:\n')) #User inputs inheritance format
    title = raw_input('Please enter the title of your Punnett Square: ')
    father = raw_input("Please enter the father's name: ")
    mother = raw_input("Please enter the mother's name: ")
    while True: #loops until user input is valid
        p1 = raw_input("Please enter the alleles of the father: ")#enter father alleles
        if p1=='help':
            os.system('notepad.exe help.txt')
            print '\n'
        else:
            p2 = raw_input("Please enter the alleles of the mother: ")#enter mother alleles
            if p2=='help': #opens help documentation
                os.system('notepad.exe help.txt')
                print '\n'
            else:
                if xl:
                    go = xltest(p1, p2) #test for appropriate alleles
                else:
                    go = test(p1,p2)#test for appropriate alleles
                if go == '':
                    break #proceeds if input is valid
                else:
                    print go #prints error message if input is invalid
    
    p1 = formatS(p1)
    p2 = formatS(p2)        
    data=[[],[]] #create list of genotypes
    count = 0
    for i in p2:
        data[count].append(i)#add one gamete from mother
        for j in p1:
            data[count].append(formatS(j+i)) #add one gamete from father
        count+=1
    
    if cod: #prints two colors in one cell if codominant in nature
        data.insert(0,['',p1[0],p1[1]])
        table = ct.colortbl(data)
        letters = letterlist(p1, p2)
        for i in (1,2): #parses through offspring cells
            for j in (1,2):
                if str(data[i][j])[0] != str(data[i][j])[1]: #if both alleles
                    table.color(i, j, c1='#ffffff', c2='#ff4059')
                elif data[i][j][0] == letters[0]: #if phenotype 1
                    table.color(i, j, '#ff4059')
                else: #if phenotype 2
                    table.color(i, j, '#ffffff')
        phenprobs = prob(p1,p2)
        table.title(inherit + ' of ' + title)
        table.x_label(father)
        table.y_label(mother)
        table.show()
        
    else: #prints one color per cell based on phenotype
        phenprobs = prob(p1,p2)
        colors = setColors(data)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        table = plt.table( #initialize table
            cellText=data,
            cellColours=colors,
            cellLoc='center',
            colWidths=[0.25,0.25,0.25],
            rowLabels=['',''],
            colLabels=['',p1[0],p1[1]],
            colColours= ['0.45','0.45','0.45'],
            colLoc='center',
            loc='center',bbox=None)
        table.scale(1, 6)
        plt.xticks([], [])
        plt.yticks([], [])
        plt.text(0.5, 1.1, inherit + ' of ' + title, horizontalalignment = 'center', fontsize = 14, transform = ax.transAxes)
        ax.set_xlabel(father)
        ax.xaxis.set_label_position('top')
        ax.set_ylabel(mother)
        plt.show()
    #plt.savefig('image.png',dpi=750)
    return phenprobs, xl, cod
        
def letterlist(p1, p2): #creates list of alleles contained in codominant genotypes
    letters = []
    for p in (p1, p2): #parses through letters in genotypes
        for letter in p:
            if letter not in letters:
                letters.append(letter)
    return sorted(letters) #returns list sorted in alphabetical order

def prob(g1, g2): #calculate probability of inheriting specific traits
    phenprobs = {}
    if xl: #if mode of inheritance is x-linked
        #determine frequency of dominant allele in parent genotypes
        pdom1 = sum(1 for c in g1 if c=='X')/1.0
        pdom2 = sum(1 for c in g2 if c.isupper())/2.0
        #'F' represents female offspring, 'M' represents male 
        phenprobs['F2'] = pdom1*pdom2
        phenprobs['F1'] = pdom1*(1-pdom2) + (1-pdom1)*pdom2
        phenprobs['F0'] = (1-pdom2)*(1-pdom1)
        phenprobs['M2'] = pdom2
        phenprobs['M0'] = (1-pdom2)
    else:
        if cod:
            letters = letterlist(g1, g2)
            #determine frequency of first allele in parent genotypes
            pdom1 = sum(1 for c in g1 if c==letters[0])/2.0
            pdom2 = sum(1 for c in g2 if c==letters[0])/2.0
        else:
            #determine frequency of dominant allele in parent genotypes
            pdom1 = sum(1 for c in g1 if c.isupper())/2.0
            pdom2 = sum(1 for c in g2 if c.isupper())/2.0
        
        #for offspring, '2' represents dominant phenotype, '1' intermediate, '0' recessive
        phenprobs['2']=pdom1*pdom2
        if inc or cod:
            phenprobs['1']=pdom1*(1-pdom2) + pdom2*(1-pdom1)
        else:
            phenprobs['2']+= pdom1*(1-pdom2) + pdom2*(1-pdom1)
        phenprobs['0']=(1-pdom1)*(1-pdom2)
    return phenprobs
        
def inheritlist(x): #dictionary storing names of each type of inheritance
    global inc
    global cod
    global xl
    #updates global variable statuses
    if x == 'inc':
        inc = True
    elif x == 'cod':
        cod = True
    elif x == 'xl':
        xl = True
    else:
        inc, cod, xl = False, False, False
    #returns appropriate name based on user input
    return {
        'aut': "Autosomal Dominance",
        'inc': "Incomplete Dominance",
        'cod': "Codominance",
        'xl': 'X-Linked Inheritance',
        'help': 'help',
        }.get(x, "invalid")

def formatS(string): #edits genotype so that capital allele always precedes lowercase
    if (not xl) or 'Y' not in string:
        if string[0]<=string[1]:
            return string[0]+string[1]
        else:
            return string[1]+string[0]
    else:
        #exception - if x-linked, X allele should precede Y allele
        if string[0]=='Y':
            return string[1]+string[0]
        else: 
            return string[0]+string[1]

def setColors(data): #determines the color of each box based on offspring phenotype
    colors = [[],[]]
    i = 0
    for row in data:
        for box in row:
            if len(box) == 1: #parent alleles - gray
                colors[i].append('0.45')
            elif box.isupper(): #dominant phenotype - red
                colors[i].append((1,.25,.35))
            elif box[0].upper() in box:
                if inc: #intermediate phenotype - pink
                    colors[i].append((1,.35,.65))
                elif xl:
                    if box[0].isupper(): 
                        colors[i].append((1,.25,.35))
                    else:
                        colors[i].append('w')
                else: 
                    colors[i].append((1,.25,.35))
            else: #recessive phenotype - white
                colors[i].append('w')
        i+=1
    return colors 

def analyzeData(data): #displays text for the specific phenotype of each cell
    text = [[],[]]
    for i in range(0,2):
        for j in range(1,3):
            if data[i][j].isupper():
                text[i].append("Homozygous dominant. Dominant phenotype.")
            elif data[i][j].islower():
                text[i].append("Homozygous recessive. Recessive phenotype")
            else:
                if inc:
                    text[i].append("Heterozygous. Intermediate phenotype.")
                else:
                    text[i].append("Heterozygous. Dominant phenotype.")
    return text
    
def test(p1, p2): #Tests for the proper input of 2x2 inputs
    if re.sub('[^A-Za-x]','',p1) != p1 or re.sub('[^A-Za-x]','',p2) != p2: #if the alleles aren't some form of letters, then error
        return '\nPlease input letters for alleles. Try again.'
    if len(p1)!=2 or len(p2) !=2:
        return '\nPlease input exactly two alleles for each parent. Try again.' #checks if there aren an appropriate number of alleles
    if cod:
        if p1 != p1.upper() or p2 != p2.upper():
            return '\nPlease use capital letters for alleles in codominance.'
        letters = letterlist(p1, p2)
        if len(letters) > 2:
            return '\nPlease use two different letters for alleles.'
    else:
        if p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper():
            return '\nPlease use the same letter in each parent genotype.Try again.' #checks if one parent has 2 different letters for one gene
        if p1.upper() != p2.upper():
            return '\nPlease use the same letter for both parent genotypes. Try again.' #checks if there are different alleles in each parent
    return ''
    
def xltest(p1,p2):
    if re.sub('[X,x]','',p1) != 'Y' or re.sub('[X,x]','',p2) != '': #if alleles aren't X/x/Y for male or X/x for female, then error
        return "\nPlease enter appropriate alleles for each parent (Father: X, x, Y; Mother: X, x)."
    if len(p1)!=2 or len(p2) !=2:
        return '\nPlease input exactly two alleles for each parent. Try again.'
    return ''
    