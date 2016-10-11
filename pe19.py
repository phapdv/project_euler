#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

from base import Problem


class Solution(Problem):

    def solve(self):
        sundays = 0

        for year in range(1901, 2000 + 1):
            for month in range(1, 13):
                day = datetime.date(year, month, 1)
                if day.weekday() == 6:
                    sundays = sundays + 1
        print('Solve problem {}'.format(self.number))
        print(sundays)


if __name__ == '__main__':
    solution = Solution(19)
    solution.solve()
