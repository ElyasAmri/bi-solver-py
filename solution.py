from math import *
from grid import Grid


def table_sum(w, h):
    g = Grid(w, h)

    mx = ceil(log2(max(w, h)))
    res = 0
    for i in range(0, mx):
        g.print_bin_digit(i+1)

        d = 2 ** i
        dvi = floor(w / d)
        dvj = floor(h / d)
        ri = w % d
        rj = h % d

        dvim2 = dvi % 2
        dvjm2 = dvj % 2

        squares = dvi * dvj / 2
        if dvim2 == dvjm2 == 1:
            squares -= 0.5 # squares = (dvi * dvj - 1) / 2
            remainders = ((dvi + 1) * rj + (dvj + 1) * ri) / 2 * d   
        else:
            remainders = ((dvi - dvim2) * rj + (dvj - dvjm2) * ri) / 2 * d

        if not dvim2 == dvjm2:
            remainders += ri * rj

        c = squares * d * d + remainders
        val = c * d
        print(f'd: {d}, count: {c}, dvi: {dvi}, ri: {ri}, dvj: {dvj}, rj: {rj} val:{val}')
        print(f'      squares: {squares}, remainders: {remainders}')
        print()
        res += val


    s = g.sum()
    ir = int(res)
    print(f'{s} == {ir} : {s == ir}')


if __name__ == '__main__':
    table_sum(13, 7)