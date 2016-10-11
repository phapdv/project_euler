#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def prime_sum(self, number_limit):
        if number_limit < 2:
            return 0
        if number_limit == 2:
            return 2
        if number_limit % 2 == 0:
            number_limit += 1
        primes = [True] * number_limit
        primes[0], primes[1] = [None] * 2
        p_sum = 0
        for idx, value in enumerate(primes):
            if value is True and idx > number_limit**0.5 + 1:
                p_sum += idx
            elif value is True:
                primes[idx * 2::idx] = [False] * (((number_limit - 1) // idx) - 1)
                p_sum += idx
        return p_sum

    def solve(self, input_):
        print('Solve problem {}'.format(self.number))
        print(self.prime_sum(input_))

if __name__ == '__main__':
    solution = Solution(10)
    solution.solve(2000000)
