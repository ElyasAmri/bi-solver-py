import pprint


def grid(rx, ry):
    ret = {}
    for i in range(rx):
        for j in range(ry):
            ret[(i, j)] = i ^ j
    return ret

def binary(n, zf = 8):
    return bin(n).zfill(zf).replace('b', '')

def binaryx(n, zf = 8):
    return bin(n).zfill(zf).replace('b', '')[-3]

def listformat(l: list):
    return str(l).strip('[]').replace("'", '').replace(',', '')

if __name__ == '__main__':
    x = 13
    y = 16
    g = grid(y, x)
    print(f'{binary(0)}         {listformat([binary(j) for j in range(0, x)])}')
    print()
    for i in range(0, y):
        l = [binaryx(g[(i, j)]) for j in range(0, x)]
        print(f'{binary(i)}         {listformat(l)}')
    pass

if __name__ == '__main__.':
    g = grid(1, 10)
    print(sum(g.values()))
    print(sum([g[(0, i)] ^ 2 for i in range(0, 10)]))
    print(2 ^ sum([g[(0, i)] for i in range(0, 10)]))

    print(sum([g[(0, i)] ^ 7 for i in range(0, 10)]))
    print(7 ^ sum([g[(0, i)] for i in range(0, 10)]))

    pass