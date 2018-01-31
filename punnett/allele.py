''' MODULE: allele.py

provides some basic definitions and routines for solving punnett squares

This is not really the main Punnett square solver. Karena's main.py script is
the general solver. This is just a quick solver for proof-of-concept for the
website.
'''
import numpy as np
import colortable as ct

class allele:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return allele(self.name + other.name)
    def __mul__(self, other):
        # WARNING: two alleles being multiplied MUST have same length
        # use addition if untrue
        return allele(''.join([self.name[i]+other.name[i] for i, _ in
                               enumerate(self.name)]))
    def __repr__(self):
        return self.name

def str2geno(string):
    res = []
    for i in range(0, len(string), 2):
        res += [[allele(string[i]), allele(string[i+1])]]
    return res

def combine(arr, depth):
    if depth == len(arr):
        return [allele('')]
    return [i+j for i in arr[depth] for j in combine(arr, depth+1)]

def solve(f, m):
    f_arr, m_arr = combine(str2geno(f), 0), combine(str2geno(m), 0)
    sol_arr = np.outer(m_arr, f_arr).tolist()
    square = [[allele('')] + f_arr]
    nrows = len(f_arr) + 1
    for i in range(nrows-1):
        square += [[m_arr[i]] + sol_arr[i]]
    return square

def colorize(data):
    # in this future, this will actually use codominance or whatever
    # right now, all this does is colorize the first four cells and leave the
    # rest blank
    colorized = []
    for r, _ in enumerate(data):
        colorized += [[]]
        for c, _ in enumerate(data[r]):
            colorized[r] += [[]]
    colorized[1][1] = ['#a4c4fc']
    colorized[2][2] = ['#fcaba4']
    colorized[1][2] = ['#fcaba4', '#a4c4fc']
    colorized[2][1] = ['#fcaba4', '#a4c4fc']
    return colorized

def to_html(data, colors):
    html_str = '<table>'
    for r, row in enumerate(data):
        html_str += '<tr>'
        for c, cell in enumerate(row):
            if r == 0 or c == 0:
                html_str += '<th>'+str(cell)+'</th>'
            else:
                style = ''
                if len(colors[r][c]) == 1:
                    style = 'background-color: '+str(colors[r][c][0])+';'
                elif len(colors[r][c]) == 2:
                    style = 'background: linear-gradient(-45deg,'+str(colors[r][c][0])+' 50%,'+str(colors[r][c][1])+' 51%);'
                html_str += '<td style="'+style+'">'+str(cell)+'</td>'
        html_str += '</tr>'
    html_str += '</table>'
    return html_str

def plot(f, m, title=''):
    square = solve(f, m)
    table = ct.colortbl(square)
    table.title(title)
    return table
