#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def solve(self, input_):
        powers = []
        for a in range(2, input_ + 1):
            for b in range(2, input_ + 1):
                powers.append(a**b)
        result = len(list(set(powers)))

        print('Solve problem {}'.format(self.number))
        print(result)


if __name__ == '__main__':
    solution = Solution(29)
    solution.solve(100)
