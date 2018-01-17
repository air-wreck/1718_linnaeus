import matplotlib.pyplot as plt

def makeSquare16(p1, p2):
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
    print phenprobs
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
    plt.savefig('image.png',dpi=750)

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
    phenprobs['2222'] = probsa['2']*probsb['2']*probsc['2']*probsd['2']
    phenprobs['2220'] = probsa['2']*probsb['2']*probsc['2']*probsd['0']
    phenprobs['2202'] = probsa['2']*probsb['2']*probsc['0']*probsd['2']
    phenprobs['2022'] = probsa['2']*probsb['0']*probsc['2']*probsd['2']
    phenprobs['0222'] = probsa['0']*probsb['2']*probsc['2']*probsd['2']
    phenprobs['2200'] = probsa['2']*probsb['2']*probsc['0']*probsd['0']
    phenprobs['2002'] = probsa['2']*probsb['0']*probsc['0']*probsd['2']
    phenprobs['0022'] = probsa['0']*probsb['0']*probsc['2']*probsd['2']
    phenprobs['2020'] = probsa['2']*probsb['0']*probsc['2']*probsd['0']
    phenprobs['0202'] = probsa['0']*probsb['2']*probsc['0']*probsd['2']
    phenprobs['0220'] = probsa['0']*probsb['2']*probsc['2']*probsd['0']
    phenprobs['0002'] = probsa['0']*probsb['0']*probsc['0']*probsd['2']
    phenprobs['0020'] = probsa['0']*probsb['0']*probsc['2']*probsd['0']
    phenprobs['0200'] = probsa['0']*probsb['2']*probsc['0']*probsd['0']
    phenprobs['2000'] = probsa['2']*probsb['0']*probsc['0']*probsd['0']
    phenprobs['0000'] = probsa['0']*probsb['0']*probsc['0']*probsd['0']
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