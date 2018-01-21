''' ped_main.py

an interactive command-line client for pedigree graphing
'''
import ped_draw as pd
import ped_solve as ps

# individual nodes are stored in a list and linked together
pedigree = []


###########################
# FUNCTIONS EXPOSED TO USER
###########################

# adds a person to the pedigree
def add(args):
    global pedigree
    if len(args) < 2 or len(args) > 3:
        print 'error: add: requires 2 or 3 args'
    elif args[1] not in ['m', 'f']:
        print 'error: add: sex must be \'m\' or \'f\''
    elif args[0] in [i.name for i in pedigree]:
        print 'error: add: individual already exists'
    else:
        sex = ps.Sex.m
        if args[1] == 'f':
            sex = ps.Sex.f
        prob = -1.0
        if len(args) == 3:
            try:
                prob = float(args[2])
            except:
                print 'error: add: infection probability must be number'
                return
            if prob < 0 or prob > 1:
                print 'error: add: infection probability must between 0 and 1'
                return
        pedigree += [ps.Person(args[0], sex, prob)]
        return

# lists all the people in the pedigree
def list_ped(args):
    longest = max([len('name')]+[len(i.get()[0]) for i in pedigree])
    print 'name '+' '*(longest-len('name'))+'sex    prob parent'
    print '='*(20+longest)
    for i in pedigree:
        parent = ''
        if i.father != None:
            parent = i.father.name + ', ' + i.mother.name
        print '%*s %-6s %-3.2f %s' % ((-longest,)+i.get()+(parent,))

# calculates the probability that an individual is infected
def calc(args):
    if len(args) == 0:
        print 'error: calc: takes one or more arguments'
        return
    no_error = True
    for i in args:
        if i not in [j.name for j in pedigree]:
            print 'error: calc: individual %s not found in pedigree' % i
            no_error = False
        else:
            person = [j for j in pedigree if j.name == i][0]
            res = ps.find_prob(person)
            if res > 0:
                print '%s has a %.4f chance of being infected' % (i, res)
            else:
                # error message provided by ped_solve.py
                no_error = False
    return no_error

# quits the program
def quit_ped(args):
    print 'quitting the interactive pedigree solver...'
    return  # quit handled in the loop

# displays help information
def help_ped(args):
    if len(args) == 0:
        print 'available commands:'
        for i in cases.keys():
            print '  ' + i
        print 'for specific help, try: \'? <func>\''
        return
    if args[0] == 'add':
        print 'adds a person to the pedigree'
        print 'arguments:'
        print '  [String] name'
        print '  [char] sex: either \'m\' or \'f\''
        print '  [float] prob: probability that this person is infected'
        print 'example:'
        print '  ped> add Nelson m 0.65'
    elif args[0] == 'list':
        print 'lists all people currently in the pedigree'
    elif args[0] == 'show':
        print 'shows the pedigree diagram'
        print 'calling show automatically solves the entire pedigree'
        print 'this is still in development and may have overlapping lines'
    elif args[0] == 'calc':
        print 'calculates the chance that each given individual is affected'
        print 'accepts a list of individuals'
        print 'if parent probabilities not know, recursively calc parents'
        print 'if a founder has no probability, an error occurs'
        print 'arguments:'
        print '  [String] name of individual to solve for'
        print '  (additional names may be given)'
        print 'example:'
        print '  ped> calc Nelson Karena'
    elif args[0] == 'set':
        print 'set a parents-child relationship'
        print 'arguments:'
        print '  [String] child name'
        print '  [String] first parent name'
        print '  [String] second parent name'
        print 'example:'
        print '  set Bob Nelson Karena'  # hehe...
    elif args[0] == 'unset':
        print 'removes a parents-child relationship'
        print 'arguments:'
        print '  [String] name'
        print 'example:'
        print '  unset Bob'
    elif args[0] == 'del':
        print 'delete a list of people from the pedigree'
        print 'WARNING: this will delete all the individual\'s children'
        print 'arguments:'
        print '  [String] name'
        print '  (additional names may be given)'
        print 'example:'
        print '  del Nelson Karena'
    elif args[0] == '?':
        print 'provides general or specific help'
        print 'arguments (optional):'
        print '  [String] func: the function on which you want help'
        print 'example:'
        print '  ? add'
    elif args[0] == 'quit':
        print 'exits the pedigree program'
    else:
        print '?: no help entry for this command'

# utilizes ped_draw.py to graph the pedigree with Graphviz
def draw_ped(args):
    # solve whole pedigree first
    not_solved = []
    for i in pedigree:
        if i.get()[2] < 0:
            not_solved += [i.name]
    if len(not_solved) > 0 and calc(not_solved) == False:
        # yay for short-circuiting!
        print 'error: show: unable to solve pedigree'
        print 'make sure all founders have independent probabilities'
        return

    # draw the pedigree
    print 'plotting pedigree...'
    graph = pd.Draw('Pedigree Drawing')
    # loop through pedigree and find the marriages
    # for now, we are assuming that it is monogamous and generational
    marriages = []
    for individual in pedigree:
        if individual.father != None:
            # has this marriage already been found?
            # i.e. is this a sibling of an already found child?
            for union in marriages:
                if (union[0] == individual.father and
                    union[1] == individual.mother):
                    union[2] += [individual]
                    break
            else:
                marriages += [[individual.father, individual.mother,
                              [individual]]]
    if len(marriages) == 0:
        print 'warning: no marriages found'
    for i in marriages:
        graph.draw_marriage(i[0], i[1], i[2])
    graph.show()

# define a parent-child relationship
def set_relationship(args):
    if len(args) != 3:
        print 'error: set: takes exactly three arguments'
        return
    if not set(args).issubset([i.name for i in pedigree]):
        print 'error: set: individual(s) not found in pedigree'
        return
    ped_get = lambda name: [i for i in pedigree if i.get()[0] == name][0]
    child = ped_get(args[0])
    father = ped_get(args[1])
    mother = ped_get(args[2])
    if father.sex != ps.Sex.m or mother.sex != ps.Sex.f:
        print 'error: set: father and mother must have natural sexes'
        return
    child.add_parents(father, mother)

# remove a parent-child relationship
def unset(args):
    if len(args) != 1:
        print 'error: unset: takes exactly one argument'
        return
    if args[0] not in [i.name for i in pedigree]:
        print 'error: unset: individual not found in pedigree'
        return
    [i for i in pedigree if i.name == args[0]][0].add_parents(None, None)

# remove and individual and all his or her children
def delete(args):
    if len(args) == 0:
        print 'error: del: takes one or more arguments'
        return
    for i in args:
        if i not in [j.name for j in pedigree]:
            print 'error: del: individual %s not found in pedigree' % i
        else:
            person = [j for j in pedigree if j.name == i][0]
            for j in range(len(pedigree)-1, -1, -1):
                k = pedigree[j]
                if k.father == person or k.mother == person:
                    del pedigree[j]
            pedigree.remove(person)


###################
# HANDLE USER INPUT
###################

# map user input strings to correct functions
cases = {
    'add': add,
    'list': list_ped,
    'calc': calc,
    'quit': quit_ped,
    'show': draw_ped,
    'set': set_relationship,
    'unset': unset,
    'del': delete,
    '?': help_ped
}
def switch(case):
    return cases.get(case)


''' pre-define some people to make debugging easier
add(['Nelson', 'm', '0.65'])
add(['Karena', 'f', '0.99'])
add(['Bob', 'm'])
add(['John', 'm'])
add(['Joe', 'm'])
set_relationship(['Bob', 'Nelson', 'Karena'])
set_relationship(['John', 'Nelson', 'Karena'])
set_relationship(['Joe', 'Nelson', 'Karena'])
'''

print 'Welcome to Linnaeus: the interactive pedigree program!'
print '    HTHS CSE Software Design Project'
print '    (c) 2018 Eric, Nelson, Karena'
print '    Try \'?\' for more information.'
cmd = ''
while cmd != 'quit':
  cmd = raw_input('ped> ')
  try:
    switch(cmd.split()[0])(cmd.split()[1:])
  except:
    print 'error: illegal instruction'
    print '  enter \'?\' for help'
    print '  try \'? <func>\' for specific help'
