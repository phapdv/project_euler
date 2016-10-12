#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def check_in(self, n, nx):
        return all(c in set(str(n)) for c in set(str(nx)))

    def solve(self):
        found = False
        n = 1
        while not found:
            if all(self.check_in(n, n * i) for i in range(2, 7)):
                print(n)
                found = True
            else:
                n += 1
        print('Solve problem {}'.format(self.number))

if __name__ == '__main__':
    solution = Solution(52)
    solution.solve()
    # print(solution.check_in(125874, 251748))
