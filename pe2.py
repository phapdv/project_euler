#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):
    """docstring for Solution."""

    def sum_(self, num):
        sum_ = 0
        i = 1
        if num < 0:
            raise ValueError('Num must be greater than 0')
        elif isinstance(num, str):
            raise TypeError('Num must be integer greater than 0')
        while self.fibo_number(i) <= num:
            if self.fibo_number(i) % 2 == 0:
                sum_ += self.fibo_number(i)
            i += 1
        return sum_

    def solve(self, input_):
        print('Solve problem {}'.format(self.number))
        print(self.sum_(input_))

if __name__ == '__main__':
    solution = Solution(2)
    solution.solve(4 * 10**6)
