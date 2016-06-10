#!/bin/python3

import sys

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20 , print Not Weird

N = int(input().strip())

if (N % 2 == 0):
    # additional test require
    if (N == 2 or N == 4):
        print("Not Weird")
    elif (N > 20):
        print("Not Weird")
    else:
        print("Weird")

else:
    print("Weird")

