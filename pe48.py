#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        s = 0
        for i in range(1, input_ + 1):
            s = s + i**i
        print('Solve problem {}'.format(self.number))
        print(str(s)[-10:])
if __name__ == '__main__':
    solution = Solution(48)
    solution.solve(1000)
