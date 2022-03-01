from math import log2, floor
from grid import Grid
from funcs import binary_digit_value, limit2


def table_sum(w, h, L, p=False):
    if w in [0, 1] and h in [0, 1]:
        return 0, True

    g = Grid(w, h, L)
    if p:
        g.print_f()
        g.print()

    # max bits to split the function (into bit-frames)
    mx = limit2(max(w-1, h-1))
    lx = limit2(L) if not L == 0 else 0
    res = 0

    subtract_digits = [binary_digit_value(L, mx, i) for i in range(1, lx + 1)]
    subtract_digits = list(filter(lambda x: not x == 0, subtract_digits))
    start = floor(log2(min(subtract_digits))) if not len(subtract_digits) == 0 else 0

    for i in range(start, mx):
        d = 2 ** i

        dvi, ri = divmod(w, d)
        dvj, rj = divmod(h, d)

        dvim2 = dvi % 2
        dvjm2 = dvj % 2

        if dvim2 == dvjm2 == 1:
            squares = (dvi * dvj - 1) / 2
            remainders_i = (dvj + 1) * ri / 2
            remainders_j = (dvi + 1) * rj / 2
        else:
            squares = dvi * dvj / 2
            remainders_i = (dvj - dvjm2) * ri / 2
            remainders_j = (dvi - dvim2) * rj / 2

        remainders = (remainders_i + remainders_j) * d

        if not dvim2 == dvjm2:
            remainders += ri * rj

        # all cells
        c = squares * d * d + remainders

        # all cells valued d
        val = c * d if d not in subtract_digits else 0

        smaller_subtracts = list(filter(lambda x: x < d, subtract_digits))
        bigger_subtracts = list(filter(lambda x: x >= d, subtract_digits))

        for s in smaller_subtracts:
            deviation = squares * d + remainders_i + remainders_j
            if not dvim2 == dvjm2:
                deviation += min(ri, rj)
            val -= deviation * s

        for s in bigger_subtracts:
            for pi in range(0, i):
                pd = 2 ** pi
                squares0 = dvi * dvj - squares
                remainders_i0 = dvj * ri - remainders_i
                remainders_j0 = dvi * rj - remainders_j
                deviation = squares0 * s + remainders_i0 + remainders_j0
                if not dvim2 == dvjm2:
                    deviation += min(ri, rj)
                val += deviation * pd

        res += val

    s = g.sum()
    ir = int(res)
    if p:
        sr = g.raw.sum()
        print(f'theoretical: {s}, actual: {ir}, raw: {sr}')
    return ir, s == ir


if __name__ == '__main__':
    table_sum(1, 3, 2, True)

    exit(1)

    for l in range(0, 10):
        for i in range(1, 10):
            for j in range(1, 10):
                expected = Grid(i, j, l).sum()
                actual, _ = table_sum(i, j, l)
                if not expected == actual:
                    print(f'failed: {i}, {j}, {l}')
                    exit(-1)

    # g = Grid(11, 9, 1)
    # g.print()
    # for i in range(1, g.mx):
    #     g.print_bin_digit(i)
    # g.print_f()
