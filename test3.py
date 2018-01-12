import matplotlib.pyplot as plt

fig, axes = plt.subplots(ncols=3, nrows=3, figsize=(2, 1.5))
fig.subplots_adjust(0.05,0.05,0.95,0.95, wspace=0, hspace=0)

for ax in axes.flatten():
    ax.tick_params(labelbottom=0, labelleft=0, bottom=0, top=0, left=0, right=0)
    ax.axis('tight')

def add_text(text, row, col):
    axes[row][col].text(0.5, 0.5, text, transform=axes[row][col].transAxes,
                        ha='center', va='center')

def add_color(color, row, col):
    axes[row][col].set_facecolor(color)

def add_half_color(color1, color2, row, col):
    axes[row][col].add_patch(
        plt.Polygon([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5]], color=color1)
    )
    axes[row][col].add_patch(
        plt.Polygon([[-1.5, -1.5], [-1.5, 1.5], [1.5, 1.5]], color=color2)
    )

# manually add cell text
add_text('A', 0, 1)
add_text('a', 0, 2)
add_text('a', 1, 0)
add_text('a', 2, 0)
add_text('Aa', 1, 1)
add_text('aa', 1, 2)
add_text('Aa', 2, 1)
add_text('aa', 2, 2)

# manually color cells
for i, _ in enumerate(axes):
    add_color('#c6c6c6', i, 0)
for i, _ in enumerate(axes[0]):
    add_color('#c6c6c6', 0, i)

add_half_color('#fcaba4', '#a4c4fc', 1, 1)

plt.show()