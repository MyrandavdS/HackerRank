#import builtins

results = []
n = int(input())
arr = map(int, input().split())
l = list(arr)
l.sort()
lengtel = len(l)
li = 0

while li < lengtel:
    while l[li] < l[li+1]:
        print(l[li], "test")
        li += 1





#results.append(l[])
#print(results[0])