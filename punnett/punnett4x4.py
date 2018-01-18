import matplotlib.pyplot as plt
import re

def makeSquare4():
    while True:
        p1 = raw_input("Please enter the alleles of the father: ").strip()
        p2 = raw_input("Please enter the alleles of the mother: ").strip()
        go = test(p1, p2)
        if go == '':
            break
        else:
            print go
    
    gametes1 = []
    gametes2 = []
    for i in range(2):
        for j in range(2,4):
            gametes1.append(p1[i]+p1[j])
            gametes2.append(p2[i]+p2[j])
            
    data = [[],[],[],[]]
    count = 0
    for g1 in gametes2:
        data[count].append(g1)
        for g2 in gametes1:
            data[count].append(formatS(g1[0]+g2[0])+formatS(g1[1]+g2[1]))
        count+=1
        
    phenprobs = prob(p1, p2)
    colors = setColors(data)
    #text = analyzeData(data)
    
    table = plt.table(
        cellText=data,
        cellColours=colors,
        cellLoc='center',
        colWidths=[0.2]*5,
        rowLabels=['']*4,
        colLabels=['']+gametes1,
        colColours= ['0.45']*5,
        colLoc='center',
        loc='center',bbox=None)
    table.scale(1, 4)
    plt.axis('off')
    plt.show()
    #plt.savefig('image.png',dpi=750)
    
    return phenprobs
        
def prob(g1,g2):
    g1a = g1[0:2]
    g1b = g1[2:4]
    g2a = g2[0:2]
    g2b = g2[2:4]
    probsa = probOne(g1a,g2a)
    probsb = probOne(g1b,g2b)
    phenprobs = {}
    plist = ('0','2')
    for a in plist:
        for b in plist:
            tag = a+b
            phenprobs[tag] = probsa[a]*probsb[b]
    return phenprobs

def probOne(g1, g2):
    phenprobs = {}
    pdom1 = sum(1 for c in g1 if c.isupper())/2.0
    pdom2 = sum(1 for c in g2 if c.isupper())/2.0
    phenprobs['2']=pdom1*pdom2 +pdom1*(1-pdom2) + pdom2*(1-pdom1)
    phenprobs['0']=(1-pdom1)*(1-pdom2)
    return phenprobs

def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data):
    colors = [[],[],[],[]]
    i = 0
    for row in data:
        for box in row:
            if len(box) == 2:
                colors[i].append('0.45')
            elif box.isupper():
                colors[i].append('m')
            elif (box[0].upper() in box) and (box[2].upper() in box):
                colors[i].append('m')
            elif box[0].upper() in box:
                colors[i].append((1,.35,.65))
            elif box[2].upper() in box:
                colors[i].append('c')
            else:
                colors[i].append('w')
        i+=1
    return colors

def analyzeData(data):
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

def test(p1, p2):
    p1 = p1.upper()
    p2 = p2.upper()
    if re.sub('[^A-Za-x]','',p1) != p1 or re.sub('[^A-Za-x]','',p2) != p2:
        return '\nPlease input letters for alleles. Try again.'
    if len(p1)!=4 or len(p2) !=4:
        return '\nPlease input exactly four alleles for each parent. Try again.'
    letters = []
    for p in (p1, p2):
        letters2 = []
        for letter in p:
            if letter not in letters2:
                letters2.append(letter)
            if letter not in letters:
                letters.append(letter)
        if len(letters2) != 2:
            return '\nPlease use two different letters in each parent genotype.Try again.'
    if len(letters) != 2:
        return '\nPlease use the same two letters for both parent genotypes. Try again.'
    if len(p1.strip(p1[0])) !=2 or len(p2.strip(p2[0])) !=2:
        return '\nPlease provide two alleles for each gene. Try again.'
    if p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper():
        return '\nPlease group the alleles by gene. Try again.'
    return ''