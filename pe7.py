#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def prime_th(self, n_th):
        primes = [2]
        i = 3
        while len(primes) < n_th:
            if all(i % prime != 0 for prime in primes):
                primes.append(i)
            i += 2
        return primes[-1]

    def solve(self, input_):
        print('Solve problem {}'.format(self.number))
        print(self.prime_th(input_))

if __name__ == '__main__':
    solution = Solution(7)
    solution.solve(10001)
