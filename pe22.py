#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from string import ascii_uppercase

from base import Problem


class Solution(Problem):

    def point(self, word_):
        return sum(ascii_uppercase.index(c) + 1
                   for c in word_.strip('"\n'))

    def solve(self):
        with open('names.txt') as f:
            lines = f.read()
            lst_words = lines.split(',')

        print('Solve problem {}'.format(self.number))
        print(sum(self.point(word) * i for i, word in enumerate(lst_words, 1)))

if __name__ == '__main__':
    solution = Solution(22)
    solution.solve()
