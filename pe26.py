#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def cal_decimal(self, n):
        i = 10
        j = 0
        while (i != 10) or (j < 1):
            i = (i % n) * 10
            j += 1
        return j

    def solve(self, input_):
        max_length = 0
        for i in range(2, input_):
            if (i % 2 != 0) and (i % 5 != 0):
                length = self.cal_decimal(i)
                if length > max_length:
                    max_length = length
                    result = i
        print('Solve problem {}'.format(self.number))
        print(result)

if __name__ == '__main__':
    solution = Solution(26)
    solution.solve(1000)
