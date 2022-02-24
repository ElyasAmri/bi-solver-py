from math import ceil
from grid import Grid
from funcs import binary_digit_value, limit2, div_rem


def table_sum(w, h, L):
    g = Grid(w, h, L)
    g.print_f()
    g.print()

    # max bits to split the function (into bit-frames)
    mx = limit2(max(w, h))
    lx = limit2(L)
    res = 0

    subtract_digits = [binary_digit_value(L, mx, i) for i in range(1, lx + 1)]
    subtract_digits = list(filter(lambda x: not x == 0, subtract_digits))

    for i in range(0, mx):
        d = 2 ** i

        if d in subtract_digits:
            continue

        dvi, ri = div_rem(w, d)
        dvj, rj = div_rem(h, d)

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

        # all cells
        c = squares * d * d + remainders

        # all cells valued d
        val = c * d

        for s in subtract_digits:
            deviation = squares * d + (ri * ceil(dvj / 2) + rj * ceil(dvi / 2))
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
    table_sum(1, 2, 1)

    # for i in range(1, 10):
    #     for j in range(1, 10):
    #         if not table_sum(i, j, 1):
    #             print(f'failed, {i}, {j}')
    #             exit(-1)

    # g = Grid(11, 9, 1)
    # g.print()
    # for i in range(1, g.mx):
    #     g.print_bin_digit(i)
    # g.print_f()
