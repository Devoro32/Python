# s= "Hacker"- test the initial while loop
# i=0
# even=""
# odd=""


# first input to indicate how many more input will be needed
f = int(input())
y = 0
while (y < f):
    # Other inputs

    s = str(input())
    # print(s)
    i = 0
    even = ""
    odd = ""
    # while loop to sepearate odd and even letters
    while (i < len(s)):
        if (i % 2 == 1):
            odd += s[i]
        else:
            even += s[i]
        i += 1
    print(even + " " + odd)

    y += 1



