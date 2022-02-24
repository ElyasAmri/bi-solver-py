from math import *
from grid import Grid
from funcs import binary_digit_value


def table_sum(w, h, L):
    g = Grid(w, h, L)
    # g.print_bin()

    # max bits to split the function (into bit-frames)
    mx = floor(log2(max(w, h))) + 1
    lx = floor(log2(L)) + 1
    res = 0

    subtract_digits = [binary_digit_value(L, mx, i) for i in range(1, lx + 1)]
    subtract_digits = list(filter(lambda x: not x == 0, subtract_digits))

    print(subtract_digits)

    g.print_frames()

    for i in range(0, mx):
        g.print_bin_digit(i + 1)
        # if subtract_digits[i]:
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
            # squares = (dvi * dvj - 1) / 2
            squares -= 0.5
            remainders = ((dvi + 1) * rj + (dvj + 1) * ri) / 2 * d
        else:
            remainders = ((dvi - dvim2) * rj + (dvj - dvjm2) * ri) / 2 * d

        if not dvim2 == dvjm2:
            remainders += ri * rj

        c = squares * d * d + remainders
        val = c * d
        print(f'd: {d}, count: {c}, dvi: {dvi}, ri: {ri}, dvj: {dvj}, rj: {rj} val:{val}')
        print(f'      squares: {squares}, remainders: {remainders}\n')

        if d in subtract_digits:
            continue

        for s in subtract_digits:
            deviation = squares * d + (ri * (dvj - dvjm2) + rj * (dvi - dvim2)) / 2
            if s <= d:
                val -= deviation * s
            # else:
            #     val += deviation

        res += val

    s = g.sum()
    sr = g.raw.sum()
    ir = int(res)
    print(f'theoretical: {s}, actual: {ir}, raw: {sr}')
    return s == ir


if __name__ == '__main__':
    table_sum(2, 3, 1)
    # g = Grid(11, 9, 1)
    # g.print()
    # for i in range(1, g.mx):
    #     g.print_bin_digit(i)
    # g.print_f()
