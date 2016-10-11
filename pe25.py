#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        a = 1
        b = 1
        count = 2
        while len(str(b)) < input_:
            a, b = b, a + b
            count += 1

        print('Solve problem {}'.format(self.number))
        print(count)


if __name__ == '__main__':
    solution = Solution(25)
    solution.solve(1000)
