#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        n = 1
        for i in range(1, 100 + 1):
            n = n * i

        print('Solve problem {}'.format(self.number))
        print(self.digits_sum(n))

if __name__ == '__main__':
    solution = Solution(20)
    solution.solve(100)
