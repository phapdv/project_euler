#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import Problem


class Solution(Problem):

    def fact_1_to_9(self):
        n = [1]
        for i in range(1, 10):
            n.append(self.factorial(i))
        return n

    def sum_fact(self, n):
        s = 0
        num_fact = self.fact_1_to_9()
        while n > 0:
            remain = n % 10
            s = s + num_fact[remain]
            n = n // 10
        return s

    def solve(self, input_):
        total = 0
        for i in range(10, input_):
            if i == self.sum_fact(i):
                total += i

        print('Solve problem {}'.format(self.number))
        print(sum(i for i in range(3, 100000) if i == self.sum_fact(i)))


if __name__ == '__main__':
    solution = Solution(34)
    solution.solve(100000)
