import os.path
import punnett2x2
import punnett4x4
import punnett8x8
import punnett16x16

print ('\n\nPunnett Square Creator\n')
print ('This program can support the follow square sizes:\n')
print ('\tEnter \'1\' for 2x2')
print ('\tEnter \'2\' for 4x4')
print ('\tEnter \'3\' for 8x8')
print ('\tEnter \'4\' for 16x16')

while True:
    command = raw_input('Please enter a square size: ')
    if command == '1':
        punnett2x2.makeSquare2()
        break
    elif command == '2':
        punnett4x4.makeSquare4()
        break
    elif command == '3':
        punnett8x8.makeSquare8()
        break
    elif command == '4':
        punnett16x16.makeSquare16()
        break
    else:
        print ('Command not recognized. Please try again.')
