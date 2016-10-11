#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        pow_digit = pow(2, 1000)
        print('Solve problem {}'.format(self.number))
        print(self.digits_sum(pow_digit))


if __name__ == '__main__':
    solution = Solution(16)
    solution.solve(1000)
