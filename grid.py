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
            l = [binary_digit(self.data[(i, j)], 8, -digit) for j in range(0, self.w)]
            print(f'{binary(i)}         {list_format(l)}')
        print()

    def print_frames(self):
        subtract_digits = [int(i) for i in binary(self.L, 8)]
        last_s = None
        for d in range(1, self.mx):
            new_s = False
            for i in range(0, self.h):
                lp = [binary_digit(self.raw.data[(i, j)], self.mx, -d) for j in range(0, self.w)]
                la = [binary_digit(self.data[(i, j)], self.mx, -d) for j in range(0, self.w)]

                if d in subtract_digits:
                    if not new_s:
                        print('\n--------------------\n')
                        last_s = [[0 for _ in range(0, self.w)] for _ in range(0, self.h)]
                        new_s = True

                    lpr = [0 if i == 1 else 1 for i in lp]
                    last_s[i] = list_add_list(last_s[i], lpr)
                    ld = [0 for _ in lp]
                    print(combine_lists('    ', lp, la, ld, lpr))
                else:
                    new_s = False
                    lp_s = list_sub_list_bitwise(lp, last_s[i])
                    last_s[i] = list_sub_list_bitwise_rev(last_s[i], lp)
                    print(combine_lists('    ', lp, la, lp_s, last_s[i]))
            print()

    def sum(self):
        return sum(self.data.values())
