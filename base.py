#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Problem(object):
    """docstring for Problem."""

    def __init__(self, number):
        self.number = number

    def fibo_number(self, n):
        try:
            if n < 1:
                raise ValueError('n must be positive')
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return self.fibo_number(n - 2) + self.fibo_number(n - 1)
        except TypeError as e:
            print(e)

    def gcd(self, a, b):
        # GCD = UCLN find UCLL of 2 natural numbers
        t = b
        b = a % b

        if b == 0:
            return t
        else:
            return self.gcd(t, b)

    def is_prime(self, n):
        if n == 2:
            return 1
        if n == 1 or n % 2 == 0:
            return 0
        m = int(n**1 / 2)
        for i in range(3, m + 1):
            if n % i == 0:
                return 0
            return 1

    def digits_sum(self, n):
        s = 0
        while n > 0:
            s = s + (n % 10)
            n = n // 10
        return s

    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def solve(self):
        return 'No sulution given yet!'
