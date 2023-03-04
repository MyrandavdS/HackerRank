if __name__ == '__main__':
    # N is how many times are we going through the loop
    N = int(input())
    # empty list we are going to fill with the for loop
    arr = []
    # the loop with the number of amounts we are going to run it with the N amount
    for i in range(N):
        # inp will be the actual input to fill the list and what to do
        inp = input().split()
        # here we have the first input equal to the options down below like insert
        # second input will be for the index like with the insert
        # third input will be the value
        # dont forget the input starts at 0 just like a list (thats why we have inp 0 and inp 1 for example)
        if inp[0] == 'insert':
            arr.insert(int(inp[1]), int(inp[2]))
        elif inp[0] == 'print':
            print(arr)
        elif inp[0] == 'remove':
            if int(inp[1]) in arr:
                arr.remove(int(inp[1]))
        elif inp[0] == 'append':
            arr.append(int(inp[1]))
        elif inp[0] == 'sort':
            arr.sort()
        elif inp[0] == 'pop':
            arr.pop()
        elif inp[0] == 'reverse':
            arr.reverse()