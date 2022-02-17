def grid(rx, ry):
    ret = {'s': i for i in []}
    for i in range(rx):
        for j in range(ry):
            ret[(i, j)] = i ^ j
    return ret

if __name__ == '__main__':
    rx = 10
    ry = 10
    g = grid(rx, ry)

    for i in range(0, rx):
        print([g[i, j] for j in range(0, ry)])

    for i in range(0, rx):
        print(sum([g[(i, j)] for j in range(0, i)]))
    for i in range(0, rx):
        print(sum([g[(i, j)] for j in range(i, ry)]))
    print(bin(rx))