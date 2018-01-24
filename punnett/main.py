''' main.py

The main program for Linnaeus's punnett square functionality.

This program calls upon the other programs and is able to create Punnett squares for each size.
To use interactively, just run the program.
'''
#import other programs
import punnett2x2
import punnett4x4
import punnett8x8
import punnett16x16
import os

def help(): #opens help documentation upon user request
    os.system('notepad.exe help.txt')
    return 
    
def probTable(probs): #prints table of probabilities for offspring phenotypes
    global xl
    print '\n\nOffspring Phenotype Probabilities\n'
    header = '\t'
    if xl: #print separate cols based on the sex of the individual
        header+='%-30s' %'Gender'
    for i in range(1,(int(command)+1)):
        header+='%-30s' %('Trait '+str(i) + ':')
    header+='Probability:'
    print header
    for key in reversed(sorted(probs.keys())): #parses through each possible phenotype
        line = '\t'
        if not xl: #prints phenotype headings if not x-linked
            for x in key:
                if x=='2':
                    if cod: #dominant and recessive phenotypes do not exist in codominance
                        line+='%-30s' %'Phenotype 1'
                    else:
                        line+='%-30s' %'Dominant'
                elif x=='1':
                    if cod:
                        line+='%-30s' %'Both phenotypes'
                    else:
                        line+='%-30s' %'Intermediate'
                elif x=='0':
                    if cod:
                        line+='%-30s' %'Phenotype 2'
                    else:
                        line+='%-30s' %'Recessive'
        else: #prints phenotype headings if x-linked
            if key[0]=='F': 
                line+='%-30s' %'Female'
            else:
                line+='%-30s' %'Male'
            if key[1]=='2':
                line+='%-30s' %'Dominant'
            elif key[1]=='1':
                line+='%-30s' %'Carrier'
            elif key[1]=='0':
                line+='%-30s' %'Recessive'
        line+='%9s' %(str(round(probs[key]*100,4))+'%')
        print line
    
#user interface
print ('\n\nPunnett Square Creator\n')
print ('Note: For all functions to run properly, Canopy cannot be in interactive mode.')
print ('Please also ensure that the folder \'punnett\' is selected as the working directory.')
print ('Enter \'help\' at any time for more detailed instructions/information.')
print ('\nThis program can support the following square sizes:\n')
print ('\tEnter \'1\' for 2x2')
print ('\tEnter \'2\' for 4x4')
print ('\tEnter \'3\' for 8x8')
print ('\tEnter \'4\' for 16x16')
global command
global make
make = True
global xl
xl = False
global cod
cod = False

while make: #program loops so user can continue to generate punett squares
    while True:
        command = raw_input('Please enter a square size: ').strip() #input size of punnett square
        #call appropriate punnett square function
        if command == '1':
            probs, xlink, codom= punnett2x2.makeSquare2() 
            xl = xlink
            cod = codom
            probTable(probs)
            break
        elif command == '2':
            probs= punnett4x4.makeSquare4()
            probTable(probs)
            break
        elif command == '3':
            probs= punnett8x8.makeSquare8()
            probTable(probs)
            break
        elif command == '4':
            probs= punnett16x16.makeSquare16()
            probTable(probs)
            break
        elif command.lower() == 'help': #call help function
            help()
            print '\n'
        else:
            print ('Command not recognized. Please try again.') #error checking
            
    while True: #can leave program here
        cont = raw_input('Is this the desired Punnett Square?\n\tEnter \'Y\' for yes\n\tEnter \'N\' for no\n\n\t')
        if cont == 'N' or cont == 'n':
            break
        elif cont == 'Y' or cont == 'y':
            make = False
            break 
        elif cont.lower() == 'help':
            help()
        else:
            print ('\nCommand not recognized. Please try again.')

print '\nGoodbye!'