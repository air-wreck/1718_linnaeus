import matplotlib.pyplot as plt

def makeSquare2(p1, p2, incDom=False):
    go = test(p1, p2)
    if go == 1:
        print "You inputted more than two alleles for each parent. Please try again."
    elif go == 2:
        print "You used more than one letter to represent alleles. Please try again."
    else:
        data=[[],[]]
        count = 0
        for i in p2:
            data[count].append(i)
            for j in p1:
                data[count].append(formatS(j+i))
            count+=1
        phenprobs = prob(p1,p2,incDom)
        print phenprobs
        #text = analyzeData(data, incDom)
        colors = setColors(data, incDom)
        table = plt.table(
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
        plt.axis('off')
        plt.show()
        plt.savefig('image.png',dpi=750)
        
def prob(g1, g2, incDom):
    phenprobs = {}
    pdom1 = sum(1 for c in g1 if c.isupper())/2.0
    pdom2 = sum(1 for c in g2 if c.isupper())/2.0
    phenprobs['2']=pdom1*pdom2
    if incDom:
        phenprobs['1']=pdom1*(1-pdom2) + pdom2*(1-pdom1)
    else:
        phenprobs['2']+= pdom1*(1-pdom2) + pdom2*(1-pdom1)
    phenprobs['0']=(1-pdom1)*(1-pdom2)
    return phenprobs
    
def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data, incDom):
    colors = [[],[]]
    i = 0
    for row in data:
        for box in row:
            if len(box) == 1:
                colors[i].append('0.45')
            elif box.isupper():
                colors[i].append((1,.25,.35))
            elif box[0].upper() in box:
                if incDom:
                    colors[i].append((1,.35,.65))
                else:
                    colors[i].append((1,.25,.35))
            else:
                colors[i].append('w')
        i+=1
    return colors 

def analyzeData(data, incDom):
    text = [[],[]]
    for i in range(0,2):
        for j in range(1,3):
            if data[i][j].isupper():
                text[i].append("Homozygous dominant. Dominant phenotype.")
            elif data[i][j].islower():
                text[i].append("Homozygous recessive. Recessive phenotype")
            else:
                if incDom:
                    text[i].append("Heterozygous. Intermediate phenotype.")
                else:
                    text[i].append("Heterozygous. Dominant phenotype.")
    return text
    
def test(p1, p2):
    if len(p1) != 2 or len(p2) !=2:
        return 1
    elif p1.upper() != p2.upper() or p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper():
        return 2
    else:
        return 3