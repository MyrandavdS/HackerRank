if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # empty list to fill it up with results of list in for statement
    results = []
    # in range +1 because in range doesn't take the value, for example value is 5 it will only use 1,2,3,4. With +1 it will use the actual value of x y z
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                # fill the list with i j k
                l = []
                l.append(i)
                l.append(j)
                l.append(k)
                # if total is not n in this case 3 it will append the result to the results list. this way we get all the possibilities of i j k that doesn't total 3
                # != is ongelijk aan, sum() is totaal van een variabel etc.
                if sum(l) != n:
                    results.append(l)

    print(results)