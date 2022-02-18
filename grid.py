from bits import listformat, binary, binaryx


class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = {(i, j): i ^ j for i in range(0, h) for j in range(0, w)}

    def print(self):
        print(f'0         {listformat([j for j in range(0, self.w)])}')
        print()
        for i in range(0, self.h):
            l = [self.data[(i, j)] for j in range(0, self.w)]
            print(f'{i}         {listformat(l)}')
        print()

    def print_bin(self):
        print(f'{binary(0)}         {listformat([binary(j) for j in range(0, self.w)])}')
        print()
        for i in range(0, self.h):
            l = [binary(self.data[(i, j)]) for j in range(0, self.w)]
            print(f'{binary(i)}         {listformat(l)}')
        print()

    def print_bin_digit(self, digit):
        for i in range(0, self.h):
            l = [binaryx(self.data[(i, j)], 8, -digit) for j in range(0, self.w)]
            print(f'{binary(i)}         {listformat(l)}')
        print()

    def sum(self):
        return sum(self.data.values())
