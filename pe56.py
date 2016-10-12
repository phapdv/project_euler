#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        numberLargest = 0
        for a in range(1, 100):
            if a % 10 != 0:
                for b in range(1, 100):
                    num_pow = a**b
                    number_sum = self.digits_sum(num_pow)
                    if number_sum > numberLargest:
                        numberLargest = number_sum

        print('Solve problem {}'.format(self.number))
        print(numberLargest)


if __name__ == '__main__':
    solution = Solution(56)
    solution.solve(100)
