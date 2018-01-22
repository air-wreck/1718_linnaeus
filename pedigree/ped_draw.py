''' MODULE: ped_draw.py

This is a pedigree plotter implemented with Graphviz. It needs some serious
work.

The output first goes to an intermediate file *.dot and then to the final *.pdf
It currently cannot handle multiple generations and has a slight bug for
exactly 2 or 3 children. It looks great for a single marriage with 6 children!

See file ped_draw_example.py for an example of how to use this module
'''

from graphviz import Graph
import ped_solve as ps

class Draw():
    def __init__(self, name, format='pdf'):
        self.name = name
        self.next_hidden = 0  # next available hidden node ID
        self.nodes = []  # list of currently existing named nodes

        # create the graph and set attributes for pedigree
        self.dot = Graph(comment=name, format=format)
        self.dot.graph_attr['splines'] = 'ortho'
        self.dot.node_attr['fontname'] = 'helvetica'
        self.dot.node_attr['fixedsize'] = 'true'
        self.dot.node_attr['style'] = 'filled'
        self.dot.node_attr['height'] = '0.5'
        self.dot.body.append('\tlabelloc="t";')
        self.dot.body.append('\tlabel="'+name+'";')


    #########################
    # BASIC DRAWING FUNCTIONS
    #########################

    def hidden(self, names):
        # define hidden nodes from a list
        for name in names:
            self.dot.node(name, width='0', shape='point', style='invis')

    def indiv(self, person):
        # define an individual node from a Person
        shape = 'square'
        if person.sex == ps.Sex.f:
            shape = 'circle'

        # shade the node based on infection probability
        R = 255
        G = int(119 + 136*(1-person.infected))
        B = int(86 + 169*(1-person.infected))
        color = '#'+hex(R)[2:]+hex(G)[2:]+hex(B)[2:]

        self.dot.node(person.name, shape=shape, fillcolor=color)

    def srank(self, nodes):
        # places a list of nodes in the same rank
        self.dot.body.append(
            '\t{rank=same; ' +
            ' -- '.join([n for n in nodes]) +
            ';}'
        )

    def edges(self, edgelist, constraint='true'):
        # makes a bunch of edges in 2D list
        for pair in edgelist:
            self.dot.edge(pair[0], pair[1], constraint=constraint)

    def render(self):
        # render self to DOT, but do not display
        return self.dot.source

    def show(self):
        # render and display self
        # return generated DOT source for convenience
        self.dot.render(self.name+'.dot', view=True)
        return self.dot.source


    ###########################
    # FAMILY PLOTTING FUNCTIONS
    ###########################

    def draw_marriage(self, father, mother, children, silent=False):
        # accepts two Person objects and draws the marriage between them
        # takes a list of children as arg until i figure out how to do that
        # silent allows no stdout printing for CGI script

        # if unknown, find the probability
        # reject the probability if invalid
        for p in [father, mother]+children:
            if ps.find_prob(p) < 0:
                if not silent:
                    print 'err: unable to determine probability for individual %s'\
                       % p.get()[0]
                return -1  # failure

        # append these people to our list of nodes
        if father.name not in self.nodes:
            self.indiv(father)
            self.nodes += [father.name]
        if mother.name not in self.nodes:
            self.indiv(mother)
            self.nodes += [mother.name]
        self.nodes += [c.name for c in children]

        if len(children) == 0:
            # no children = no tricky stuff with hidden nodes!
            self.srank([father.name, mother.name])
        else:
            # make a hidden node in the middle to connect to children
            self.hidden([str(self.next_hidden)])
            self.srank([father.name, str(self.next_hidden), mother.name])
            self.next_hidden += 1

        if len(children) == 1:
            # there is only one child, so no branching for children
            self.indiv(children[0])
            self.nodes += children[0].name
            self.edges([[str(self.next_hidden-1), children[0].name]])
        elif len(children) > 1:
            # general branching required for children
            N = len(children) - (len(children)%2) - 1  # hidden nodes needed
            hnodes = [str(h) for h in range(self.next_hidden,
                                            self.next_hidden+N)]
            self.hidden(hnodes)
            self.srank(hnodes)

            # link center node to marriage node
            self.edges([[str(self.next_hidden-1), str(self.next_hidden+N/2)]])
            for c in children:
                self.indiv(c)

            # link the first child to the correct node
            self.edges([[str(self.next_hidden), children[0].name]])

            # link subsequent children to the corresponding nodes
            edgelist = []
            for i, c in enumerate(children[1:-1]):
                add = 0
                if len(children)%2 == 0 and i >= N/2:
                    add = 1
                edgelist += [[str(self.next_hidden+i+add), c.name]]
            self.edges(edgelist)

            # link the final child to the correct node
            self.edges([[str(self.next_hidden+N-1), children[-1].name]])
            self.next_hidden += N

            return 1  # success
