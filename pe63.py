#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self):
        total = 0
        for i in range(1, 100):
            for j in range(1, 100):
                num_pow = i**j
                if len(str(num_pow)) == j:
                    total += 1
        print('Solve problem {}'.format(self.number))
        print(total)

if __name__ == '__main__':
    solution = Solution(63)
    solution.solve()
