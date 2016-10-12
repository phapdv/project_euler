#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def is_proper(self, n):
        return sum([i for i in range(1, n // 2 + 1) if n % i == 0])

    def solve(self, input_):
        print('Solve problem {}'.format(self.number))
        print(sum(a for a in range(1, input_) if
                  a == self.is_proper(self.is_proper(a)) and
                  self.is_proper(a) < input_ and
                  a != self.is_proper(a)))

if __name__ == '__main__':
    solution = Solution(21)
    solution.solve(10000)
    # print(solution.is_proper(solution.is_proper(284)))
