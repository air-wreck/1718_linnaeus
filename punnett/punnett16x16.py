import matplotlib.pyplot as plt
import re

def makeSquare16():
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
            for k in range(4,6):
                for l in range(6,8):
                    gametes1.append(p1[i]+p1[j]+p1[k]+p1[l])
                    gametes2.append(p2[i]+p2[j]+p2[k]+p2[l])
                    
    data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    count = 0
    for g1 in gametes2:
        data[count].append(g1)
        for g2 in gametes1:
            data[count].append(formatS(g1[0]+g2[0])+formatS(g1[1]+g2[1])+formatS(g1[2]+g2[2])+formatS(g1[3]+g2[3]))
        count+=1
        
    phenprobs = prob(p1,p2)
    colors = setColors(data)
    
    table = plt.table(
        cellText=data,
        cellColours=colors,
        cellLoc='center',
        colWidths=[0.055]*17,
        rowLabels=['']*16,
        colLabels=['']+gametes1,
        colColours= ['0.45']*17,
        colLoc='center',
        loc='center',bbox=None)
    plt.axis('off')
    plt.show()
    #plt.savefig('image.png',dpi=750)
    return phenprobs

def prob(g1,g2):
    g1a = g1[0:2]
    g1b = g1[2:4]
    g1c = g1[4:6]
    g1d = g1[6:8]
    g2a = g2[0:2]
    g2b = g2[2:4]
    g2c = g2[4:6]
    g2d = g2[6:8]
    probsa = probOne(g1a,g2a)
    probsb = probOne(g1b,g2b)
    probsc = probOne(g1c,g2c)
    probsd = probOne(g1d,g2d)
    phenprobs = {}
    plist = ('0','2')
    for a in plist:
        for b in plist:
            for c in plist:
                for d in plist:
                    tag = a+b+c+d
                    phenprobs[tag] = probsa[a]*probsb[b]*probsc[c]*probsd[d]
    return phenprobs
    
def probOne(g1, g2):
    phenprobs = {}
    pdom1 = sum(1 for c in g1 if c.isupper())/2.0
    pdom2 = sum(1 for c in g2 if c.isupper())/2.0
    phenprobs['2']=pdom1*pdom2 + pdom1*(1-pdom2) + pdom2*(1-pdom1)
    phenprobs['0']=(1-pdom1)*(1-pdom2)
    return phenprobs

def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data):
    colors = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    j = 0
    c= [0,0,0]
    for row in data:
        for box in row:
            if len(box) == 4:
                colors[j].append('0.45')
            else:
                for i in range(0,3):
                    if box[0+2*i:2+2*i].isupper():
                        c[i] = 0.5
                    elif box[0+2*i:2+2*i].islower():
                        c[i] = 1
                    else: 
                        c[i] = 0.5
                if box[6:8].isupper():
                    c[0]-=0.3
                    c[2]-=0.3
                elif box[6:8].islower():
                    c[0]-=0
                    c[2]-=0
                else:
                    c[0]-=0.3
                    c[2]-=0.3
                if c[0]==0.2 and c[1]==0.5 and c[2]==0.2:
                    colors[j].append((.4,.4,.4))
                else:
                    colors[j].append(tuple(c))
        j+=1
    return colors
    
def test(p1, p2):
    p1 = p1.upper()
    p2 = p2.upper()
    if re.sub('[^A-Za-x]','',p1) != p1 or re.sub('[^A-Za-x]','',p2) != p2:
        return '\nPlease input letters for alleles. Try again.'
    if len(p1)!=8 or len(p2) !=8:
        return '\nPlease input exactly eight alleles for each parent. Try again.'
    letters = {}
    for p in (p1, p2):
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
        if len(letters2) != 4:
            return '\nPlease use four different letters in each parent genotype.Try again.'
    if len(letters) != 4:
        return '\nPlease use the same four letters for both parent genotypes. Try again.'
    for letter in letters:
        if letters[letter] != 4 or letters2[letter] != 2:
            return '\nPlease provide two alleles for each gene. Try again.'
    if p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper():
        return '\nPlease group the alleles by gene. Try again.'
    if p1[2].upper() != p1[3].upper() or p2[2].upper() != p2[3].upper():
        return '\nPlease group the alleles by gene. Try again.'
    if p1[4].upper() != p1[5].upper() or p2[4].upper() != p2[5].upper():
        return '\nPlease group the alleles by gene. Try again.'
    return ''