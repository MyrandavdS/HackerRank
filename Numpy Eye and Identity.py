import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())


print(numpy.eye(n, m))
# Dimensional array with first upper diagonal 1 (index)
print(numpy.eye(n, m, k = 1))
# Dimensional array with second lower diagonal 1 (index)
print(numpy.eye(n, m, k= -2))
