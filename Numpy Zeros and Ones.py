import numpy

# a, b, c = map(int, input().split())
#
# for i in range(a):
#     print(numpy.zeros((b,c), dtype= int), end='\n')
#     #print("\n")
#
# for i in range(a):
#     print(numpy.ones((b,c), dtype= int), sep='\n')

sizes = list(map(int, input().split()))

#print(sizes)

print(numpy.zeros(sizes, dtype=int), numpy.ones(sizes, dtype=int),  sep='\n')


