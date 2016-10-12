#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        total = 0
        for i in range(2, input_):
            Sum = 0
            for j in str(i):
                Sum += int(j)**5
            if Sum == i:
                total += Sum
        print('Solve problem {}'.format(self.number))
        print(total)

if __name__ == '__main__':
    solution = Solution(30)
    solution.solve(1000000)
