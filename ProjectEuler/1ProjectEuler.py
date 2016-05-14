# Taken from projecteuler: https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Plan of attach: find the multiple of 3, then 5  that is below
# 1000, then add the numbers together

sumThree = 0
sumFive = 0
threeMultiple = 0
fiveMultiple = 0
multiplier = 1
limit = 1000

while (threeMultiple <= limit):
    # get the multiple of 3 times the multipler
    threeMultiple = (multiplier * 3)

    # within the while loop break if at any point the
    # multiple is greater than the limit
    if (threeMultiple <= limit):
        # sum the previous aggregate with the new multipler
        sumThree += threeMultiple
        print(sumThree)
        multiplier += 1
    else:
        break

multiplier = 1
print("-------------------------5 section-------------------------------")
while (fiveMultiple < limit):
    # get the multiple of 3 times the multipler
    fiveMultiple = (multiplier * 5)

    # within the while loop break if at any point the
    # multiple is greater than the limit
    if (fiveMultiple < limit):
        # sum the previous aggregate with the new multipler
        sumFive += fiveMultiple
        print(sumFive)
        multiplier += 1

print(sumFive + sumThree)