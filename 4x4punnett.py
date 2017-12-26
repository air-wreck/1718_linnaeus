import matplotlib.pyplot as plt

def makeSquare4(p1, p2, incDom=False):
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
        colors = setColors(data, incDom)
        text = analyzeData(data, incDom)
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
        plt.show()
        print text

def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data, incDom):
    colors = [[],[],[],[]]
    i = 0
    for row in data:
        for box in row:
            if len(box) == 2:
                colors[i].append('0.45')
            elif box.isupper():
                colors[i].append('m')
            elif (box[0].upper() in box) and (box[2].upper() in box):
                if incDom:
                    if box[0:2].isupper():
                        colors[i].append((1,.35,.65))
                    elif box[2:4].isupper():
                        colors[i].append((1,.25,.95))
                    else:
                        colors[i].append((1,.75,.85))
                else:
                    colors[i].append('m')
            elif box[0].upper() in box:
                if incDom:
                    if box[0:2].isupper():
                        colors[i].append('r')
                    else:
                        colors[i].append((1,.1,.3))
                else:
                    colors[i].append((1,.35,.65))
            elif box[2].upper() in box:
                if incDom:
                    if box[2:4].isupper():
                        colors[i].append((.1,.35,1))
                    else:
                        colors[i].append('c')
                else:
                    colors[i].append('c')
            else:
                colors[i].append('w')
        i+=1
    return colors

def analyzeData(data, incDom):
    text = [['','','',''],['','','',''],['','','',''],['','','','']]
    for i in range(0,4):
        for j in range(1,5):
            if data[i][j][:2].isupper():
                text[i][j-1]+="Trait 1: Homozygous dominant. Dominant phenotype."
            elif data[i][j][:2].islower():
                text[i][j-1]+="Trait 1: Homozygous recessive. Recessive phenotype."
            else:
                if incDom:
                    text[i][j-1]+="Trait 1: Heterozygous. Intermediate phenotype."
                else:
                    text[i][j-1]+="Trait 1: Heterozygous. Dominant phenotype."
            if data[i][j][2:4].isupper():
                text[i][j-1]+="Trait 2: Homozygous dominant. Dominant phenotype."
            elif data[i][j][2:4].islower():
                text[i][j-1]+="Trait 2: Homozygous recessive. Recessive phenotype."
            else:
                if incDom:
                    text[i][j-1]+="Trait 2: Heterozygous. Intermediate phenotype."
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