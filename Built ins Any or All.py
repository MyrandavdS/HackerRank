n = int(input()); m = list(map(int, input().split()))

print(all([True if i>0 else False for i in m]) and any([True if str(i)==str(i)[::-1] else False for i in m]))