import copy
import pprint

from funcs import *


class Grid:
    def __init__(self, w, h, L):
        self.w = w
        self.h = h
        self.L = L
        self.mx = limit2(max(w, h))

        if not L == 0:
            self.data = {(i, j): max((i ^ j) - L, 0) for i in range(0, h) for j in range(0, w)}
            self.raw = Grid(w, h, 0)
        else:
            self.data = {(i, j): i ^ j for i in range(0, h) for j in range(0, w)}
            return

        self.subtract_digits = list(filter(
            lambda x: not x == 0,
            [binary_digit_value(self.L, self.mx, i)
             for i in range(1, limit2(self.L) + 2)]
        ))

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
            print(f'{list_format(l)}')
        print()

    def print_frames(self, frame=None):
        """

        subtract_digits = list(
            filter(lambda x: not x == 0, [binary_digit_value(self.L, self.mx, i) for i in
                                          range(1, ceil(log2(self.L)) + 2)]))
        subtracters = {d: [[0 for _ in range(0, self.w)] for _ in range(0, self.h)] for d in subtract_digits}
        last_d = None

        def func(d, self):
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

        if frame is not None:
            func(frame, self)
            return

        for i in range(1, self.mx):
            func(i, self)

        """

    def print_f(self, frame=None, display_bit=True):
        subtracts = {
            d: [[d for _ in range(0, self.w)] for _ in range(0, self.h)]
            for d in self.subtract_digits
        }

        target = range(0, self.mx) if frame is None else [frame]

        # every frame (or just the target)
        for d in target:
            # 2 pow d
            d2 = 2 ** d
            if not display_bit:
                print(d2)

            show_option = d2 if display_bit else 1

            # every row
            for i in range(0, self.h):
                frame_previous = [binary_digit(self.raw.data[(i, j)], self.mx, d + 1) * show_option
                                  for j in range(0, self.w)]
                frame_current = [binary_digit(self.data[(i, j)], self.mx, d + 1) * show_option
                                 for j in range(0, self.w)]

                if d2 in self.subtract_digits:
                    subtracts[d2][i], frame_result = list_sub_list_limited_hard(subtracts[d2][i], frame_previous)
                    print(combine_lists('    ', frame_previous, frame_current, frame_result))
                else:
                    smaller_subtracts = list(filter(lambda x: x < d2, self.subtract_digits))

                    frame_result = frame_previous.copy()
                    for s in smaller_subtracts:
                        # frame_result = list_sub_list_limited(frame_result, subtracts[s][i])
                        subtracts[s][i], frame_result = list_sub_list_limited_hard(subtracts[s][i], frame_result)

                    print(combine_lists('    ', frame_previous, frame_current, frame_result))

            pprint.pp(subtracts)
            print()

    def sum(self):
        return sum(self.data.values())
