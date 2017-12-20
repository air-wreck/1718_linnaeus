import matplotlib.pyplot as plt
import matplotlib.colors
def makeSquare(p1, p2):
    table = plt.table(
        cellText=[[p2[0],formatS(p1[0]+p2[0]),formatS(p1[1]+p2[0])], [p2[1],formatS(p1[0]+p2[1]),formatS(p1[1]+p2[1])]],
        cellColours=[['b','w','r'],['b','w','r']],
        cellLoc='center',
        colWidths=[0.25,0.25,0.25],
        rowLabels=['',''],
        #rowColours=None, rowLoc='left',
        rowLoc='center',
        colLabels=['',p1[0],p1[1]],
        colColours= ['b','w','r'],
        colLoc='center',
        loc='center',bbox=None)
    table.scale(1, 6)
    plt.show()

def formatS(string):
    if string[0]<=string[1]:
        return string[0]+string[1]
    else:
        return string[1]+string[0]