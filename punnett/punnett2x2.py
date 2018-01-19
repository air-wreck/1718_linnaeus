import matplotlib.pyplot as plt
import re
import colortable as ct

inc = False
cod = False
xl = False

def makeSquare2():
    while True:
        print 'Please enter \'aut\' for autosomal,', \
        '\'inc\' for incomplete dominance, \'cod\' for codominance, and xl for x-linked.'
        global inherit
        inherit = inheritlist(raw_input('(If the input is invalid, autosomal will be used as a default)\n'))
        p1 = raw_input("Please enter the alleles of the father: ")
        p2 = raw_input("Please enter the alleles of the mother: ")
        go = test(p1, p2)
        if go == '':
            break
        else:
            print go
            
    data=[[],[]]
    count = 0
    for i in p2:
        data[count].append(i)
        for j in p1:
            data[count].append(formatS(j+i))
        count+=1
    
    if cod:
        data.insert(0,['',p2[0],p2[1]])
        table = ct.colortbl(data)
        for i in (1,2):
            for j in (1,2):
                if str(data[i][j])[0] != str(data[i][j])[1]:
                    table.color(i, j, c1='#ffffff', c2='#ff4059')
                elif data[i][j].isupper():
                    table.color(i, j, '#ff4059')
                else:
                    table.color(i, j, '#ffffff')
        phenprobs = prob(p1,p2)
        table.show()
    else:
        phenprobs = prob(p1,p2)
        colors = setColors(data)
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
        plt.title(inherit)
        plt.axis('off')
        plt.show()
        
    #plt.savefig('image.png',dpi=750)
    return phenprobs
        
def prob(g1, g2):
    phenprobs = {}
    pdom1 = sum(1 for c in g1 if c.isupper())/2.0
    pdom2 = sum(1 for c in g2 if c.isupper())/2.0
    phenprobs['2']=pdom1*pdom2
    if inc or cod:
        phenprobs['1']=pdom1*(1-pdom2) + pdom2*(1-pdom1)
    else:
        phenprobs['2']+= pdom1*(1-pdom2) + pdom2*(1-pdom1)
    phenprobs['0']=(1-pdom1)*(1-pdom2)
    return phenprobs
    
        
def inheritlist(x):
    global inc
    global cod
    global xl
    if x == 'inc':
        inc = True
    elif x == 'cod':
        cod = True
    elif x == 'xl':
        xl = True
    else:
        inc, cod, xl = False, False, False
    
    return {
        'aut': "Autosomal Dominance",
        'inc': "Incomplete Dominance",
        'cod': "Codominance",
        'xl': 'X-Linked',
        }.get(x, "Defaulted to Autosomal Dominant")

def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]

def setColors(data):
    colors = [[],[]]
    i = 0
    for row in data:
        for box in row:
            if len(box) == 1:
                colors[i].append('0.45')
            elif box.isupper():
                colors[i].append((1,.25,.35))
            elif box[0].upper() in box:
                if inc:
                    colors[i].append((1,.35,.65))
                else:
                    colors[i].append((1,.25,.35))
            else:
                colors[i].append('w')
        i+=1
    return colors 

def analyzeData(data):
    text = [[],[]]
    for i in range(0,2):
        for j in range(1,3):
            if data[i][j].isupper():
                text[i].append("Homozygous dominant. Dominant phenotype.")
            elif data[i][j].islower():
                text[i].append("Homozygous recessive. Recessive phenotype")
            else:
                if inc:
                    text[i].append("Heterozygous. Intermediate phenotype.")
                else:
                    text[i].append("Heterozygous. Dominant phenotype.")
    return text
    
def test(p1, p2):
    p1 = p1.upper()
    p2 = p2.upper()
    if re.sub('[^A-Za-x]','',p1) != p1 or re.sub('[^A-Za-x]','',p2) != p2:
        return '\nPlease input letters for alleles. Try again.'
    if len(p1)!=2 or len(p2) !=2:
        return '\nPlease input exactly two alleles for each parent. Try again.'
    if p1[0].upper() != p1[1].upper() or p2[0].upper() != p2[1].upper():
        return '\nPlease use the same letter in each parent genotype.Try again.'
    if p1[0].upper() != p1[1].upper():
        return '\nPlease use the same letter for both parent genotypes. Try again.'
    return ''