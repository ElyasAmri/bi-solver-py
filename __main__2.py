from bokeh.plotting import figure, show, row

width = 20
height = 20

sums = figure(title='Sum of xor tables', x_axis_label='cols', y_axis_label='rows')


# sums.dot(x, y, legend_label="Temp.", line_width=2)


def generate(x, y):
    return sum((i ^ j) for i in range(1, x) for j in range(1, y))

# sums.circle(x=[10], y=[10], size=generate(10, 10) / 50)

for i in range(1, height):
    for j in range(1, width):
        sums.circle(x=j, y=i, size=((generate(i, j)) / 50))
    # sums.circle(x=rangex, y=[i for _ in rangex])

# sums.dot(x=x, y=y, size=20, color="#00FF00", legend_label='Value')
# sums.vbar(x=x, top=y2, legend_label="Rate", width=0.5, bottom=0, color="red")

# sums.legend.location = "top_left"
# sums.legend.title = "Info"

show(row(sums))

if __name__ == '__main__':
    pass
