from bokeh.plotting import figure, show, row, gridplot


def generate(x, y):
    return sum((i ^ j) for i in range(1, x) for j in range(1, y))


plots = []
ys = [i for i in range(1, 10)]
width = 10
for y in ys:
    plot = figure(title=f'Sum of xor tables cols x and row {y}',
                  x_axis_label='X value', y_axis_label='Value')
    for i in range(1, width):
        plot.dot(x=i, y=((generate(i, y)) / 50), size=50)
    plots.append(plot)
print("Done")
show(row(plots))

if __name__ == '__main__':
    pass
