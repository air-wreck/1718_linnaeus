import matplotlib.pyplot as plt

def makeSquare2(p1, p2, incDom=False):
    go = test(p1, p2)
    if go == 1:
        print "You inputted more than two alleles for each parent. Please try again."
    elif go == 2:
        print "You used more than one letter to represent alleles. Please try again."
    else:
        text=[[],[]]
        count = 0
        for i in p2:
            text[count].append(i)
            for j in p1:
                text[count].append(formatS(j+i))
            count+=1
        colors = setColors(text, incDom)
        table = plt.table(
            cellText=text,
            cellColours=colors,
            cellLoc='center',
            colWidths=[0.25,0.25,0.25],
            rowLabels=['',''],
            colLabels=['',p1[0],p1[1]],
            colColours= ['0.45','0.45','0.45'],
            colLoc='center',
            loc='center',bbox=None)
        table.scale(1, 6)
        plt.show()

def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(text, incDom):
    colors = [[],[]]
    i = 0
    for row in text:
        for box in row:
            if len(box) == 1:
                colors[i].append('0.45')
            elif box.isupper():
                colors[i].append('r')
            elif box[0].upper() in box:
                if incDom:
                    colors[i].append('m')
                else:
                    colors[i].append('r')
            else:
                colors[i].append('w')
        i+=1
    return colors 
    
def test(p1, p2):
    if len(p1) != 2 or len(p2) !=2:
        return 1
    elif p1.upper() != p2.upper() or p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper():
        return 2
    else:
        return 3