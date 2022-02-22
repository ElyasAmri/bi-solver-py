from math import *
from grid import Grid


def table_sum(w, h, L):
    g = Grid(w, h, L)
    # g.print_bin()

    mx = ceil(log2(max(w, h)))
    res = 0
    ignore_digits = [False if i == '0' else True for i in bin(L).zfill(mx + 2).replace('0b', '')]
    ignore_digits.reverse()

    g.print_frames()

    for i in range(0, mx):
        g.print_bin_digit(i + 1)
        # if ignore_digits[i]:
        #     continue

        d = 2 ** i
        dvi = floor(w / d)
        dvj = floor(h / d)
        ri = w % d
        rj = h % d

        dvim2 = dvi % 2
        dvjm2 = dvj % 2

        squares = dvi * dvj / 2
        if dvim2 == dvjm2 == 1:
            squares -= 0.5  # squares = (dvi * dvj - 1) / 2
            remainders = ((dvi + 1) * rj + (dvj + 1) * ri) / 2 * d
        else:
            remainders = ((dvi - dvim2) * rj + (dvj - dvjm2) * ri) / 2 * d

        if not dvim2 == dvjm2:
            remainders += ri * rj

        c = squares * d * d + remainders
        val = c * d
        print(f'd: {d}, count: {c}, dvi: {dvi}, ri: {ri}, dvj: {dvj}, rj: {rj} val:{val}')
        print(f'      squares: {squares}, remainders: {remainders}\n')
        res += val

        for s in range(0, i+1):
            if ignore_digits[s]:
                pieces = squares * d * d
                res -= pieces * (2 ** s) / d

    s = g.sum()
    sr = g.raw.sum()
    ir = int(res)
    print(f'{s} == {ir}, {sr} == {ir}')


if __name__ == '__main__':
    table_sum(4, 4, 2)
    # Grid(13, 15, 2).print_frames()
