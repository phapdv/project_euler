#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):
    """docstring for Solution."""

    def solve(self, input_):
        print('Solve problem {}'.format(self.number))
        print('Result: {}'.format(sum(i for i in range(input_) if i % 3 == 0 or i % 5 == 0)))

if __name__ == '__main__':
    solution = Solution(1)
    solution.solve(1000)
