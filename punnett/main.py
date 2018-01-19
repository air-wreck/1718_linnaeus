import punnett2x2
import punnett4x4
import punnett8x8
import punnett16x16
import matplotlib.pyplot as plt

xl = False

def probTable(probs):
    print '\n\nOffspring Phenotype Probabilities\n'
    header = '\t'
    global xl
    if xl:
        header+='%-30s' %'Gender'
    for i in range(1,(int(command)+1)):
        header+='%-30s' %('Trait '+str(i) + ':')
    header+='Probability:'
    print header
    for key in reversed(sorted(probs.keys())):
        line = '\t'
        if not xl:
            for x in key:
                if x=='2':
                    line+='%-30s' %'Dominant'
                elif x=='1':
                    line+='%-30s' %'Intermediate/Codominant'
                elif x=='0':
                    line+='%-30s' %'Recessive'
        else:
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
    
print ('\n\nPunnett Square Creator\n')
print ('This program can support the following square sizes:\n')
print ('\tEnter \'1\' for 2x2')
print ('\tEnter \'2\' for 4x4')
print ('\tEnter \'3\' for 8x8')
print ('\tEnter \'4\' for 16x16')
global command
global make
make = True

while make:
    while True:
        command = raw_input('Please enter a square size: ')
        if command == '1':
            probs, xlink= punnett2x2.makeSquare2() 
            global xl
            xl = xlink
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
        else:
            print ('Command not recognized. Please try again.')
            
    while True:
        cont = raw_input('Create another Punnett square?\n\tEnter \'Y\' for yes\n\tEnter \'N\' for no\n\n\t')
        if cont == 'Y' or cont == 'y':
            break
        elif cont == 'N' or cont == 'n':
            make = False
            break 
        else:
            print ('\nCommand not recognized. Please try again.')

print '\nGoodbye!'