import matplotlib.pyplot as plt

def makeSquare16(p1, p2, incDom=False):
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
    colors = setColors(data, incDom)
    #text = analyzeData(data, incDom)
    table = plt.table(
        cellText=data,
        cellColours=colors,
        cellLoc='center',
        colWidths=[0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055,0.055],
        rowLabels=['','','','','','','','','','','','','','','',''],
        colLabels=['']+gametes1,
        colColours= ['0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45','0.45'],
        colLoc='center',
        loc='center',bbox=None)
    plt.show()
    #print text

def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data, incDom):
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
                        if incDom:
                            c[i] = 0.7
                        else:
                            c[i] = 0.5
                if box[6:8].isupper():
                    c[0]-=0.3
                    c[2]-=0.3
                elif box[6:8].islower():
                    c[0]-=0
                    c[2]-=0
                else:
                    if incDom:
                        c[0]-=0.2
                        c[2]-=0.2
                    else:
                        c[0]-=0.3
                        c[2]-=0.3
                if c[0]==0.2 and c[1]==0.5 and c[2]==0.2:
                    colors[j].append((.4,.4,.4))
                else:
                    colors[j].append(tuple(c))
        j+=1
    return colors

'''def analyzeData(data, incDom):
    text = [['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','','']]
    for i in range(0,8):
        for j in range(1,9):
            for k in range(0,3):
                if data[i][j][(0+2*k):(2+2*k)].isupper():
                    text[i][j-1]+="Trait " + str(k+1) + ": Homozygous dominant. Dominant phenotype." 
                elif data[i][j][(0+2*k):(2+2*k)].islower():
                    text[i][j-1]+="Trait " + str(k+1) + ": Homozygous recessive. Recessive phenotype."
                else:
                    if incDom:
                        text[i][j-1]+="Trait " + str(k+1) + ": Heterozygous. Intermediate phenotype."
                    else:
                        text[i][j-1]+="Trait " + str(k+1) + ": Heterozygous. Dominant phenotype."
    return text'''