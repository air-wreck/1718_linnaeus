''' punnett4x4.py

a simple punnett square solver for the 4x4 size

This program can solve a Punnett square for any number of traits with four
alleles. The output is returned as a punnett square drawn using matplotlib and the chance of inheriting certain traits.

To use interactively, just type makeSquare4().
'''

import matplotlib.pyplot as plt
import re
import os

def makeSquare4():#Creates a 4x4 punnett square and plots it; autosomal only
    title = raw_input('Please enter the title of your Punnett Square: ')
    father = raw_input("Please enter the father's name: ")
    mother = raw_input("Please enter the mother's name: ")
    while True: #loops until valid user input
        p1 = raw_input("Please enter the alleles of the father: ").strip() #enter raw input and gets rid of excess whitespace
        if p1=='help': #opens help documentation
            os.system('notepad.exe help.txt')
            print '\n'
        else:
            p2 = raw_input("Please enter the alleles of the mother: ").strip() #enter raw input and gets rid of excess whitespace
            if p2=='help': #opens help documentation
                os.system('notepad.exe help.txt')
                print '\n'
            else:
                go = test(p1, p2) #tests for proper input
                if go == '':
                    break
                else:
                    print go
    #edits genotypes to have uppercase allele always precede lowercase 
    p1 = sorted(p1[:2])+sorted(p1[2:4])
    p2 = sorted(p2[:2])+sorted(p2[2:4])
    gametes1 = [] #stores gametes for father
    gametes2 = []  #stores gametes for mother
    for i in range(2):
        for j in range(2,4):
            gametes1.append(p1[i]+p1[j])
            gametes2.append(p2[i]+p2[j])
            
    data = [[],[],[],[]]
    count = 0
    for g1 in gametes2: #appends everything together to create genotypes of possible offspring
        data[count].append(g1)
        for g2 in gametes1:
            data[count].append(formatS(g1[0]+g2[0])+formatS(g1[1]+g2[1])) 
        count+=1
        
    phenprobs = prob(p1, p2)
    colors = setColors(data)
    #text = analyzeData(data)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    table = plt.table( #initializes table
        cellText=data,
        cellColours=colors,
        cellLoc='center',
        colWidths=[0.2]*5,
        rowLabels=['']*4,
        colLabels=['']+gametes1,
        colColours= ['0.45']*5,
        colLoc='center',
        loc='center',bbox=None)
    table.scale(1, 3.65)
    plt.xticks([], [])
    plt.yticks([], [])
    plt.text(0.5, 1.15, title, horizontalalignment = 'center', fontsize = 14, transform = ax.transAxes)
    ax.set_xlabel(father)
    ax.xaxis.set_label_position('top')
    ax.set_ylabel(mother)
    plt.show() #show table
    #plt.savefig('image.png',dpi=750)
    
    return phenprobs
        
def prob(g1,g2): #calculates probability of each theoretical phenotype
    #splits parent genotypes up by trait
    g1a = g1[0:2]
    g1b = g1[2:4]
    g2a = g2[0:2]
    g2b = g2[2:4]
    probsa = probOne(g1a,g2a) #calls the individual 2x2 probability generator
    probsb = probOne(g1b,g2b)
    phenprobs = {} #stores in dictionary
    plist = ('0','2')
    for a in plist:
        for b in plist:
            tag = a+b
            phenprobs[tag] = probsa[a]*probsb[b]
    return phenprobs

def probOne(g1, g2): #calculates 2x2 probability 
    phenprobs = {}
    #determines frequency of dominant allele 
    pdom1 = sum(1 for c in g1 if c.isupper())/2.0
    pdom2 = sum(1 for c in g2 if c.isupper())/2.0
    #'2' represents dominant phenotype in offspring, '0' recessive
    phenprobs['2']=pdom1*pdom2 +pdom1*(1-pdom2) + pdom2*(1-pdom1)
    phenprobs['0']=(1-pdom1)*(1-pdom2)
    return phenprobs

def formatS(string): #formats genotypes properly in each individual cell
    #uppercase letter should precede lowercase letter
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data): #colors each cell depending on phenotype
    colors = [[],[],[],[]]
    i = 0
    for row in data:
        for box in row:
            if len(box) == 2: #parent alleles - gray
                colors[i].append('0.45')
            elif box.isupper(): #both dominant - magenta
                colors[i].append('m')
            elif (box[0].upper() in box) and (box[2].upper() in box):
                colors[i].append('m')
            elif box[0].upper() in box: #first trait dominant - pink
                colors[i].append((1,.35,.65)) 
            elif box[2].upper() in box: #second trait dominant - blue
                colors[i].append('c')
            else: #both recessive - white
                colors[i].append('w')
        i+=1
    return colors

def analyzeData(data): #Displays the trait/phenotype of each cell
    text = [['']*4]*4
    for i in range(0,4):
        for j in range(1,5):
            if data[i][j][:2].isupper():
                text[i][j-1]+="Trait 1: Homozygous dominant."
            elif data[i][j][:2].islower():
                text[i][j-1]+="Trait 1: Homozygous recessive."
            else:
                text[i][j-1]+="Trait 1: Heterozygous."
            if data[i][j][2:4].isupper():
                text[i][j-1]+="\nTrait 2: Homozygous dominant."
            elif data[i][j][2:4].islower():
                text[i][j-1]+="\nTrait 2: Homozygous recessive."
            else:
                text[i][j-1]+="\nTrait 2: Heterozygous."
    return text

def test(p1, p2): #Checks if the input is correct 
    p1 = p1.upper()
    p2 = p2.upper()
    if re.sub('[^A-Z]','',p1) != p1 or re.sub('[^A-Z]','',p2) != p2: #checks if input has only letters
        return '\nPlease input letters for alleles. Try again.'
    if len(p1)!=4 or len(p2) !=4: #checks if input is the right size
        return '\nPlease input exactly four alleles for each parent. Try again.'
    letters = []
    for p in (p1, p2): #checks if genotypes use the same letter
        letters2 = []
        for letter in p:
            if letter not in letters2:
                letters2.append(letter)
            if letter not in letters:
                letters.append(letter)
        if len(letters2) != 2:
            return '\nPlease use two different letters in each parent genotype.Try again.'
    if len(letters) != 2: #checks if different alleles are used for each trait
        return '\nPlease use the same two letters for both parent genotypes. Try again.'
    if len(p1.strip(p1[0])) !=2 or len(p2.strip(p2[0])) !=2: #checks if not enough alleles are present
        return '\nPlease provide two alleles for each gene. Try again.'
    if p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper(): #checks if alleles aren't grouped
        return '\nPlease group the alleles by gene. Try again.'
    return ''