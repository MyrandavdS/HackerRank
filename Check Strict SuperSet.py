a = set(map(int, input().split()))
n = int(input())
result = []

for i in range(n):
    sets = set(map(int, input().split()))
    super = a.issuperset(sets)
    result.append(super)

if False in result:
    print(False)
else:
    print(True)