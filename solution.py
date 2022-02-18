from math import *
from grid import Grid


def table_sum(w, h):
    g = Grid(w, h)
    # g.print()
    # g.print_bin()

    mx = ceil(log2(max(w, h)))
    res = 0
    for i in range(0, mx):
        g.print_bin_digit(i+1)

        d = 2 ** i
        dvi = floor(w / d)
        dvj = floor(h / d)
        ri = w % d
        rj = h % d

        if dvi % 2 == 0 or dvj % 2 == 0:
            squares = dvi * dvj / 2
        else:
            squares = (dvi * dvj - 1) / 2

        if dvi % 2 == 1 and dvj % 2 == 1:
            remainders = ((dvi + 1) * rj + (dvj + 1) * ri) / 2 * d
        else:
            remainders = ((dvi - dvi % 2) * rj + (dvj - dvj % 2) * ri) / 2 * d

        if not dvi % 2 == dvj % 2:
            remainders += ri * rj

        c = squares * d * d + remainders
        val = c * d
        print(f'd: {d}, count: {c}, dvi: {dvi}, ri: {ri}, dvj: {dvj}, rj: {rj} val:{val}')
        print(f'      squares: {squares}, remainders: {remainders}')
        print()
        res += val

    print(g.sum())
    print(res)


def main():
    w = 16
    h = 16

    table_sum(w, h)


if __name__ == '__main__':
    main()
