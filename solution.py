from math import *
from grid import Grid


def table_sum(w, h):
    mx = floor(log2(max(w, h)))
    res = 0
    for i in range(0, mx):
        d = 2 ** i
        dvi = floor(w / d)
        dvj = floor(h / d)
        ri = w % d
        rj = h % d

        im = dvi % 2 == 0
        jm = dvi % 2 == 0

        if im or jm:
            squares = dvi * dvj / 2
        else:
            squares = (dvi * dvj + 1) / 2

        if im:
            remainders = dvi * rj / 2
        elif jm:
            remainders = dvj * ri / 2
        else:
            remainders = ((dvi - 1) * rj + (dvj - 1) * ri) / 2

        res += (squares * d + remainders) * (d ** 2)

    return int(res)


def main():
    w = 16
    h = 16
    g = Grid(w, h)

    print(g.sum())
    print(table_sum(w, h))


if __name__ == '__main__':
    main()
