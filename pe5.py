#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self):
        n = 1
        for i in range(1, 21):
            n *= i // self.gcd(i, n)
        print('Solve problem {}'.format(self.number))
        print(str(n))
if __name__ == '__main__':
    solution = Solution(5)
    solution.solve()
