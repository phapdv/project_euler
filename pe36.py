#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def is_palindromic(self, number):
        return str(number) == str(number)[::-1]

    def solve(self, input_):
        total = 0
        for i in range(1, input_ + 1):
            if self.is_palindromic(i) and self.is_palindromic(bin(i)[2:]):
                total += i

        print('Solve problem {}'.format(self.number))
        print(total)

if __name__ == '__main__':
    solution = Solution(36)
    solution.solve(1000000)
