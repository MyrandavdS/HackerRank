n, m = map(int, input().split())
print(n)
print(m)

# making sure n is an odd number
if n % 2 != 0 and n >= 1:
    # making sure m is 3 times bigger than n
    m = n * 3
    # for loop in range of 0 index till "halfway" n / 2
    for i in range(0,int(n / 2)):
        # first pattern at index 0 * 2 + 1 will be showed once, at index 1 * 2 + 1 will be showed 3 times.
        # This way the pattern will be build up towards the center of n
        pattern = '.|.' * ((i * 2) + 1)
        print(pattern)
        # pattern will be printed in the middle by .center, the width of m will be filled with '-'
        print(pattern.center(m,'-'))
    # welcome will be printed in the middle by .center, the width of m will be filled with '-'
    print('WELCOME'.center(m,'-'))

    # parameters start stop step
    # starts at n / 2, stops at 0, takes steps of -1, going halfway and doing the opposite of for i range loop
    # this way we run through the same index numbers as for i range but doing the opposite
    for j in range(int(n / 2), 0, -1):
        # index 4 * 2 - 1 makes the pattern be printed 7 times on index 4
        # index 3 * 2 - 1 makes the pattern be printed 5 times on index 3 etc
        pattern = '.|.' * ((j * 2) - 1)
        #print(pattern)
        print(pattern.center(m,'-'))
