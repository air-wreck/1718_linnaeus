''' MODULE: colortable.py

This is a custom implementation of a table with matplotlib.pyplot, since the
original seems to not have the ability to set a cell to a half-color.

See the file colortable_example.py for an example of how to use this class.
'''

import matplotlib.pyplot as plt
import numpy as np

class colortbl():
    header_color = '#c6c6c6'

    def __init__(self, data):
        # save a copy of the data
        self.data = data

        # init axes
        ncols, nrows = len(data[0]), len(data)+1
        width, height = 0.1*(2*np.log2(ncols-1)+2), 0.3
        self.fig, self.axes = plt.subplots(ncols=ncols, nrows=nrows-1,
                                           figsize=(ncols*width, nrows*height))
        # may have to adjust margins for super large tables, but not an issue
        self.fig.subplots_adjust(0.05, 0.05, 0.95, 0.95, wspace=0, hspace=0)
        self.fig.subplots_adjust(top=1.0-(1.0/(len(self.data)+1)))

        # set styling
        for ax in self.axes.flatten():
            ax.tick_params(labelbottom=0, labelleft=0, bottom=0,
                           top=0, left=0, right=0)
            ax.axis('tight')

        # write in data and colorize headers
        for r, _ in enumerate(self.axes):
            self.color(r, 0, c1=self.header_color)
            for c, _ in enumerate(self.axes[0]):
                self.color(0, c, c1=self.header_color)
                self.add_text(str(data[r][c]), r, c)

    def title(self, text):
        self.fig.suptitle(text)

    def add_text(self, text, row, col):
        # in case manual override of text is needed
        self.axes[row][col].text(0.5, 0.5, text,
                                 transform=self.axes[row][col].transAxes,
                                 ha='center', va='center')

    def color(self, row, col, c1='#fcaba4', c2=None, c3=None, c4=None):
        # colorize cell; currently supports up to four colors
        cell = self.axes[row][col]
        lim1, lim2 = 0.06, 0.02
        if c2 == None:
            # if only one color given, set whole cell to that color
            cell.set_facecolor(c1)
        elif c3 == None:
            # if two colors given, split the cell
            cell.add_patch(
                plt.Polygon([[-lim1, -lim1], [lim1, -lim1], [lim1, lim1]],
                            color=c1)
            )
            cell.add_patch(
                plt.Polygon([[-lim1, -lim1], [-lim1, lim1], [lim1, lim1]],
                            color=c2)
            )
        elif c4 == None:
            # if three colors given, make a French flag
            cell.add_patch(
                plt.Polygon([[-lim1, -lim1], [-lim1, lim1], [-lim2, lim1],
                             [-lim2, -lim1]], color=c1)
            )
            cell.add_patch(
                plt.Polygon([[-lim2, lim1], [lim2, lim1], [lim2, -lim1],
                             [-lim2, -lim1]], color=c2)
            )
            cell.add_patch(
                plt.Polygon([[lim1, lim1], [lim1, -lim1], [lim2, -lim1],
                             [lim2, lim1]], color=c3)
            )
        else:
            # if four colors given, make an 'X' shape
            cell.add_patch(
                plt.Polygon([[-lim1, -lim1], [-lim1, lim1], [0, 0]], color=c1)
            )
            cell.add_patch(
                plt.Polygon([[-lim1, lim1], [lim1, lim1], [0, 0]], color=c2)
            )
            cell.add_patch(
                plt.Polygon([[lim1, lim1], [lim1, -lim1], [0, 0]], color=c3)
            )
            cell.add_patch(
                plt.Polygon([[lim1, -lim1], [-lim1, -lim1], [0, 0]], color=c4)
            )

    def show(self):
        plt.show()

    def to_png(self):
        plt.savefig('colortable.png')
        return file('colortable.png', 'r').read()
