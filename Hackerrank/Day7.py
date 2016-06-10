#!/bin/python3

import sys

aOutput = ""
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# print(arr)
# Need to strip the space from the last value
# Need to add space to the first value
aLen = len(arr)
i = 0
while (n > i):
    if (n == aLen):
        aOutput += str((arr[n - 1]))
    elif ((n - 1) == i):
        aOutput = aOutput + " " + str(arr[n - 1])
    else:
        aOutput = aOutput + " " + str(arr[n - 1])

    n -= 1
print(aOutput)

