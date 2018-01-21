import matplotlib.pyplot as plt
import re

def makeSquare8():#Creates a 8x8 punnett square and plots it; autosomal only
    while True:
        p1 = raw_input("Please enter the alleles of the father: ").strip() #enter raw input and gets rid of excess whitespace
        p2 = raw_input("Please enter the alleles of the mother: ").strip() #enter raw input and gets rid of excess whitespace
        go = test(p1, p2) #tests for proper input
        if go == '':
            break
        else:
            print go
            
    gametes1 = [] #stores gametes for father
    gametes2 = [] #stores gametes for mother
    for i in range(2):
        for j in range(2,4):
            for k in range(4,6):
                gametes1.append(p1[i]+p1[j]+p1[k])
                gametes2.append(p2[i]+p2[j]+p2[k])
                
    data = [[],[],[],[],[],[],[],[]] 
    count = 0
    for g1 in gametes2:#appends everything together to create genotypes of possible offspring
        data[count].append(g1)
        for g2 in gametes1:
            data[count].append(formatS(g1[0]+g2[0])+formatS(g1[1]+g2[1])+formatS(g1[2]+g2[2]))
        count+=1
        
    phenprobs = prob(p1,p2)
    colors = setColors(data)
    #text = analyzeData(data)
    
    table = plt.table( #initialize table
        cellText=data,
        cellColours=colors,
        cellLoc='center',
        colWidths=[0.1]*9,
        rowLabels=['']*8,
        colLabels=['']+gametes1,
        colColours= ['0.45']*9,
        colLoc='center',
        loc='center',bbox=None)
    table.scale(1, 2)
    plt.axis('off')
    plt.show() #output the image of the table
    #plt.savefig('image.png',dpi=750)
    return phenprobs

def prob(g1,g2):#calculates probability of each theoretical phenotype
    g1a = g1[0:2]
    g1b = g1[2:4]
    g1c = g1[4:6]
    g2a = g2[0:2]
    g2b = g2[2:4]
    g2c = g2[4:6]
    probsa = probOne(g1a,g2a)#calls the individual 2x2 probability generator
    probsb = probOne(g1b,g2b)#calls the individual 2x2 probability generator
    probsc = probOne(g1c,g2c)#calls the individual 2x2 probability generator
    phenprobs = {} #stores in dictionary
    plist = ('0','2')
    for a in plist: #figure out probabilities with indepdendent probability
        for b in plist:
            for c in plist:
                tag = a+b+c
                phenprobs[tag] = probsa[a]*probsb[b]*probsc[c]
    return phenprobs
    
def probOne(g1, g2):#2x2 individual probability calculation based on each genotype
    phenprobs = {}
    pdom1 = sum(1 for c in g1 if c.isupper())/2.0
    pdom2 = sum(1 for c in g2 if c.isupper())/2.0
    phenprobs['2']=pdom1*pdom2 + pdom1*(1-pdom2) + pdom2*(1-pdom1)
    phenprobs['0']=(1-pdom1)*(1-pdom2)
    return phenprobs

def formatS(string): #formats the genotypes
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data): #gives each individual cell a color
    colors = [[],[],[],[],[],[],[],[]]
    j = 0
    c= [0,0,0]
    for row in data:
        for box in row:
            if len(box) == 3:
                colors[j].append('0.45')
            else:
                for i in range(0,3):
                    if box[0+2*i:2+2*i].isupper():
                        c[i] = 0.5
                    elif box[0+2*i:2+2*i].islower():
                        c[i] = 1
                    else: 
                        c[i] = 0.5
                if c[0]==0.5 and c[1]==0.5 and c[2]==0.5:
                    colors[j].append((.6,.6,.6))
                else:
                    colors[j].append(tuple(c))
        j+=1
    return colors

def analyzeData(data): #analyzes data to determine what phenotypes will be exhibited
    text = [['']*8]*8
    for i in range(0,8):
        for j in range(1,9):
            for k in range(0,3):
                if data[i][j][(0+2*k):(2+2*k)].isupper():
                    text[i][j-1]+="Trait " + str(k+1) + ": Homozygous dominant.\n" 
                elif data[i][j][(0+2*k):(2+2*k)].islower():
                    text[i][j-1]+="Trait " + str(k+1) + ": Homozygous recessive.\n"
                else:
                    text[i][j-1]+="Trait " + str(k+1) + ": Heterozygous.\n"
    return text

def test(p1, p2): #tests for proper input
    p1 = p1.upper()
    p2 = p2.upper()
    if re.sub('[^A-Za-x]','',p1) != p1 or re.sub('[^A-Za-x]','',p2) != p2: #Tests if only letters are used via regex
        return '\nPlease input letters for alleles. Try again.'
    if len(p1)!=6 or len(p2) !=6: #checks for proper size of input
        return '\nPlease input exactly six alleles for each parent. Try again.'
    letters = {}
    for p in (p1, p2): #checks if there aren't 3 letters being used
        letters2 = {}
        for letter in p:
            if letter not in letters2:
                letters2[letter]=1
            else:
                letters2[letter]+=1
            if letter not in letters:
                letters[letter]=1
            else:
                letters[letter]+=1
        if len(letters2) != 3:
            return '\nPlease use three different letters in each parent genotype.Try again.'
    if len(letters) != 3: #checks if different letters are used by both parents
        return '\nPlease use the same three letters for both parent genotypes. Try again.'
    for letter in letters: #checks if each gene has 2 letters
        if letters[letter] != 4 or letters2[letter] != 2:
            return '\nPlease provide two alleles for each gene. Try again.'
    if p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper(): #checks if not grouped by letter/gene
        return '\nPlease group the alleles by gene. Try again.'
    if p1[2].upper() != p1[3].upper() or p2[2].upper() != p2[3].upper():
        return '\nPlease group the alleles by gene. Try again.'
    return ''