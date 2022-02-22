from math import *

from funcs import *


class Grid:
    def __init__(self, w, h, L):
        self.w = w
        self.h = h
        self.L = L
        self.mx = ceil(log2(max(w, h))) + 1

        if not L == 0:
            self.data = {(i, j): max((i ^ j) - L, 0) for i in range(0, h) for j in range(0, w)}
            self.raw = Grid(w, h, 0)
        else:
            self.data = {(i, j): i ^ j for i in range(0, h) for j in range(0, w)}

    def print(self):
        print(f'0         {list_format([j for j in range(0, self.w)])}\n')
        for i in range(0, self.h):
            l = [self.data[(i, j)] for j in range(0, self.w)]
            print(f'{i}         {list_format(l)}')
        print()

    def print_bin(self):
        print(f'{binary(0)}         {list_format([binary(j) for j in range(0, self.w)])}\n')
        for i in range(0, self.h):
            l = [binary(self.data[(i, j)]) for j in range(0, self.w)]
            print(f'{binary(i)}         {list_format(l)}')
        print()

    def print_bin_digit(self, digit):
        for i in range(0, self.h):
            l = [binary_digit(self.data[(i, j)], 8, digit) for j in range(0, self.w)]
            print(f'{binary(i)}         {list_format(l)}')
        print()

    def print_frames(self, frame=None):
        subtract_digits = list(
            filter(lambda x: not x == 0, [binary_digit_value(self.L, self.mx, i) for i in
                                          range(1, ceil(log2(self.L)) + 2)]))
        subtracters = {d: [[0 for _ in range(0, self.w)] for _ in range(0, self.h)] for d in subtract_digits}
        last_d = None
        for d in range(1, self.mx):
            if frame is not None and not d == frame:
                continue
            d2 = 2 ** (d - 1)
            new_s = False
            for i in range(0, self.h):
                lp = [binary_digit(self.raw.data[(i, j)], self.mx, d) for j in range(0, self.w)]

                if d2 in subtract_digits:
                    last_d = d2
                    if not new_s:
                        print('\n--------------------\n')
                        new_s = True
                    last_s = subtracters[d2]
                    lpr = [0 if i == 1 else 1 for i in lp]
                    last_s[i] = list_add_list(last_s[i], lpr)
                    ld = [0 for _ in lp]
                    print(combine_lists('    ', lp, ld, lpr))
                else:
                    new_s = False
                    if last_d is None:
                        continue
                    lp_s = list_sub_list_bitwise(lp, subtracters[last_d][i])
                    subtracters[last_d][i] = list_sub_list_bitwise_rev(subtracters[last_d][i], lp)
                    print(combine_lists('    ', lp, lp_s, subtracters[last_d][i]))
            print()

    def sum(self):
        return sum(self.data.values())
