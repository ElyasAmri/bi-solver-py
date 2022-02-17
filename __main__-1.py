def action(mx, my):
    grid = {}

    sums = []

    total = 0
    for i in range(0, mx):
        r = 0
        for j in range(0, my):
            s = grid[(i, j)] = i ^ j
            r += s
            total += s
        sums.append(r)

    for i in range(0, mx):
        for j in range(0, my):
            print(grid[(i, j)], end=' ')
        print(f' {sums[i]}')

    print(sums)

if __name__ == '__main__':
    pass
