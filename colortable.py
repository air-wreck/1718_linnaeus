''' MODULE: colortable.py

This is a custom implementation of a table with matplotlib.pyplot, since the
original seems to not have the ability to set a cell to a half-color.

See the file colortable_example.py for an example of how to use this class.
'''

import matplotlib.pyplot as plt

class colortbl():
    header_color = '#c6c6c6'

    def __init__(self, data):
        # save a copy of the data
        self.data = data

        # init axes
        ncols, nrows = len(data[0]), len(data)
        self.fig, self.axes = plt.subplots(ncols=ncols, nrows=nrows,
                                           figsize=(ncols, 0.75*nrows))
        self.fig.subplots_adjust(0.05, 0.05, 0.95, 0.95, wspace=0, hspace=0)

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

    def add_text(self, text, row, col):
        # in case manual override of text is needed
        self.axes[row][col].text(0.5, 0.5, text,
                                 transform=self.axes[row][col].transAxes,
                                 ha='center', va='center')

    def color(self, row, col, c1='#fcaba4', c2=None):
        # colorize cell
        if c2 == None:
            # if only one color given, set whole cell to that color
            self.axes[row][col].set_facecolor(c1)
        else:
            # if two colors given, split the cell
            self.axes[row][col].add_patch(
                plt.Polygon([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5]], color=c1)
            )
            self.axes[row][col].add_patch(
                plt.Polygon([[-1.5, -1.5], [-1.5, 1.5], [1.5, 1.5]], color=c2)
            )

    def show(self):
        plt.show()
