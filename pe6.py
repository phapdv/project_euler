#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        print('Solve problem {}'.format(self.number))
        print(str(sum(i for i in range(1, input_ + 1))**2 -
                  sum(i**2 for i in range(1, input_ + 1))))
if __name__ == '__main__':
    solution = Solution(6)
    solution.solve(10)
