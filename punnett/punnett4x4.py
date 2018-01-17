import matplotlib.pyplot as plt

def makeSquare4():
    p1 = raw_input("Please enter the alleles of the father.")
    p2 = raw_input("Please enter the alleles of the mother.")
    global inherit
    inherit = inheritlist(raw_input("Please enter autd for autosomal, inc for incomplete dominance, cod for codominance, and xl for x-linked."))
    go = test(p1, p2)
    if go == 1:
        print "You inputted more than four alleles for each parent. Please try again."
    elif go == 2:
        print "You used more than two letters to represent alleles. Please try again."
    elif go ==3:
        print "You used fewer than two letters to represent alleles. Please try again."
    else:
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
        print phenprobs
        colors = setColors(data)
        #text = analyzeData(data)
        table = plt.table(
            cellText=data,
            cellColours=colors,
            cellLoc='center',
            colWidths=[0.2,0.2,0.2,0.2,0.2],
            rowLabels=['','','',''],
            colLabels=['']+gametes1,
            colColours= ['0.45','0.45','0.45','0.45','0.45'],
            colLoc='center',
            loc='center',bbox=None)
        table.scale(1, 4)
        plt.title(inheritance)
        plt.axis('off')
        plt.show()
        plt.savefig('image.png',dpi=750)
        
def inheritlist(x):
        return {
            'autd': "Autosomal Dominance",
            'inc': "Incomplete Dominance",
            'cod': "Codominance",
            'xl': 'X-Linked',
            }.get(x, "defaulted to Autosomal Dominant")

def prob(g1,g2):
    g1a = g1[0:2]
    g1b = g1[2:4]
    g2a = g2[0:2]
    g2b = g2[2:4]
    probsa = probOne(g1a,g2a)
    probsb = probOne(g1b,g2b)
    phenprobs = {}
    phenprobs['22'] = probsa['2']*probsb['2']
    phenprobs['20'] = probsa['2']*probsb['0']
    phenprobs['02'] = probsa['0']*probsb['2']
    phenprobs['00'] = probsa['0']*probsb['0']
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
    text = [['','','',''],['','','',''],['','','',''],['','','','']]
    for i in range(0,4):
        for j in range(1,5):
            if data[i][j][:2].isupper():
                text[i][j-1]+="Trait 1: Homozygous dominant. Dominant phenotype."
            elif data[i][j][:2].islower():
                text[i][j-1]+="Trait 1: Homozygous recessive. Recessive phenotype."
            else:
                text[i][j-1]+="Trait 1: Heterozygous. Dominant phenotype."
            if data[i][j][2:4].isupper():
                text[i][j-1]+="Trait 2: Homozygous dominant. Dominant phenotype."
            elif data[i][j][2:4].islower():
                text[i][j-1]+="Trait 2: Homozygous recessive. Recessive phenotype."
            else:
                text[i][j-1]+="Trait 2: Heterozygous. Dominant phenotype."
    return text

def test(p1, p2):
    notEnough = False
    tooMuch = False
    letters = []
    for p in (p1, p2):
        letters2 = []
        for letter in p:
            if letter.upper() not in letters2:
                letters2.append(letter.upper())
            if letter.upper() not in letters:
                letters.append(letter.upper())
        if len(letters2) < 2:
            notEnough = True
        if len(letters2) > 2:
            tooMuch = True
    if len(letters) < 2:
        notEnough = True
    if len(letters) > 2:
        tooMuch = True
    if len(p1) != 4 or len(p2) !=4:
        return 1
    elif tooMuch:
        return 2
    elif notEnough:
        return 3
    else:
        return 4