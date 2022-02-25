from grid import Grid
from funcs import binary_digit_value, limit2


def table_sum_noprint(w, h, L):
    mx = limit2(max(w, h))
    lx = 0 if L == 0 else limit2(L)
    res = 0

    subtract_digits = [binary_digit_value(L, mx, i) for i in range(1, lx + 1)]
    subtract_digits = list(filter(lambda x: not x == 0, subtract_digits))

    for i in range(0, mx):
        d = 2 ** i

        if d in subtract_digits:
            continue

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

        c = squares * d * d + remainders

        val = c * d

        for s in subtract_digits:
            deviation = squares * d + remainders_i + remainders_j
            if not dvim2 == dvjm2:
                deviation += min(ri, rj)
            if s <= d:
                val -= deviation * s
            # else:
            #     val += deviation

        res += val

    return int(res)


def table_sum(w, h, L):
    g = Grid(w, h, L)
    g.print_f()
    g.print()

    # max bits to split the function (into bit-frames)
    mx = limit2(max(w, h))
    if not L == 0:
        lx = limit2(L)
    else:
        lx = 0
    res = 0

    subtract_digits = [binary_digit_value(L, mx, i) for i in range(1, lx + 1)]
    subtract_digits = list(filter(lambda x: not x == 0, subtract_digits))

    for i in range(0, mx):
        d = 2 ** i

        if d in subtract_digits:
            continue

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
        val = c * d

        for s in subtract_digits:
            deviation = squares * d + remainders_i + remainders_j
            if not dvim2 == dvjm2:
                deviation += min(ri, rj)
            if s <= d:
                val -= deviation * s
            else:
                val += deviation

        res += val

    s = g.sum()
    sr = g.raw.sum()
    ir = int(res)
    print(f'theoretical: {s}, actual: {ir}, raw: {sr}')
    return s == ir


if __name__ == '__main__':
    table_sum(1, 2, 2)

    # for i in range(1, 10):
    #     for j in range(1, 10):
    #         for l in range(0, 10):
    #             if not table_sum_noprint(i, j, l) == Grid(i, j, l).sum():
    #                 print(f'failed, {i}, {j}, {l}')
    #                 exit(-1)

    # g = Grid(11, 9, 1)
    # g.print()
    # for i in range(1, g.mx):
    #     g.print_bin_digit(i)
    # g.print_f()
