from bits import listformat


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
            print(f'i         {listformat(l)}')

    def sum(self):
        return sum(self.data.values())
