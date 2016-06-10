#!/bin/python3

import sys

N = int(input().strip())
i = 1
while (i <= 10):
    print(str(N) + " x " + str(i) + " = " + str(N * i))
    i += 1
