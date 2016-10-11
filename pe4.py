#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self):
        n = 0
        for i in range(100, 1000):
            for j in range(100, 1000):
                k = i * j
                if str(k) == str(k)[::-1] and k > n:
                    n = k
        print('Solve problem {}'.format(self.number))
        print(str(n))

if __name__ == '__main__':
    solution = Solution(4)
    solution.solve()
