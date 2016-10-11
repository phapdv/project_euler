#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        print('Solve problem {}'.format(self.number))
        for a in range(1, input_ + 1):
            for b in range(a + 1, input_ + 1):
                c = input_ - a - b
                if a * a + b * b == c * c:
                    print(a * b * c)


if __name__ == '__main__':
    solution = Solution(9)
    solution.solve(1000)
